
from typing import TypedDict, List

from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_chroma import Chroma

from langgraph.graph import StateGraph, START, END


# --------------------------------
# 1. Initialize Ollama LLM
# --------------------------------

llm = ChatOllama(
    model="qwen3:8b",
    temperature=0
)

# --------------------------------
# 2. Initialize embeddings
# --------------------------------

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)


# 2. Load documents
loader = TextLoader(
    "documents/hr_policy.txt",
    encoding="utf-8"
)

documents = loader.load()

print("Total documents:", len(documents))

# 3. Split documents into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = text_splitter.split_documents(documents)


# 4. Store embeddings in ChromaDB
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./vectorstore",
    collection_name="hr_policies"
)

print("Documents successfully stored!")

# # --------------------------------
# # 3. Connect ChromaDB
# # --------------------------------

# vectorstore = Chroma(
#     collection_name="hr_policies",
#     embedding_function=embeddings,
#     persist_directory="./vectorstore"
# )

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 4}
)


# --------------------------------
# 4. Define Graph State
# --------------------------------

class RAGState(TypedDict):
    question: str
    context: List[str]
    sources: List[str]
    answer: str


# --------------------------------
# 5. Retrieve Documents
# --------------------------------

def retrieve_documents(state: RAGState):

    question = state["question"]

    print("\nRetrieving documents...")

    documents = retriever.invoke(question)

    context = [
        doc.page_content
        for doc in documents
    ]

    sources = list(set(
        doc.metadata.get("source", "Unknown")
        for doc in documents
    ))

    return {
        "context": context,
        "sources": sources
    }


# --------------------------------
# 6. Generate Answer
# --------------------------------

def generate_answer(state: RAGState):

    print("\nGenerating answer...")

    question = state["question"]

    context = "\n\n".join(state["context"])

    prompt = f"""
    You are an HR Policy Assistant.

    Answer the user's question using ONLY the
    provided context.

    If the answer is not available in the context,
    clearly say that the information is not available
    in the HR policy documents.

    Context:
    {context}

    User Question:
    {question}

    Answer:
    """

    response = llm.invoke(prompt)

    return {
        "answer": response.content
    }


# --------------------------------
# 7. Create LangGraph Workflow
# --------------------------------

workflow = StateGraph(RAGState)

workflow.add_node(
    "retrieve_documents",
    retrieve_documents
)

workflow.add_node(
    "generate_answer",
    generate_answer
)

workflow.add_edge(
    START,
    "retrieve_documents"
)

workflow.add_edge(
    "retrieve_documents",
    "generate_answer"
)

workflow.add_edge(
    "generate_answer",
    END
)


# --------------------------------
# 8. Compile Graph
# --------------------------------

rag_app = workflow.compile()


# --------------------------------
# 9. Execute RAG
# --------------------------------

def ask_question(question: str):

    result = rag_app.invoke({
        "question": question,
        "context": [],
        "sources": [],
        "answer": ""
    })

    return result


if __name__ == "__main__":

    question = "How many annual leaves does an employee get?"

    response = ask_question(question)

    print("\nQuestion:", question)

    print("\nAnswer:", response["answer"])

    print("\nSources:", response["sources"])
