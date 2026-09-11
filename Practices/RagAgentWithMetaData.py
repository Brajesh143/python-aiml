from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter


LLM_MODEL = "llama3:8b"
EMBED_MODEL = "nomic-embed-text:latest"

loader = TextLoader("engineering_policy.txt")
docs = loader.load()

for doc in docs:
    doc.metadata.update({
        "department": "Engineering",
        "document_type": "policy",
        "year": 2026,
        "source": "engineering_policy.txt"
    })


# Check metadata
print("Document Metadata:")
print(docs[0].metadata)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=20
)
splits = splitter.split_documents(docs)

embeddings = OllamaEmbeddings(model=EMBED_MODEL)

vector_store = Chroma.from_documents(
    documents=splits,
    embedding=embeddings,
    collection_name="rag-agent-demo"
)

filter = {
    "department": "Engineering"
}

retriever = vector_store.as_retriever(
    search_kwargs={
        "k": 3,
        "filter": filter
    }
)

question = "What is the Engineering leave policy?"

retriever_data = retriever.invoke(question)

print("Retrieved Data:")
for doc in retriever_data:
    print(doc.metadata)
    print(doc.page_content)
    print("\n\n")

context = "\n\n".join(
    doc.page_content for doc in retriever_data
)

prompt = f"""
Answer the {question} using only provided {context}.

If the answer is not available in the context,
say "I don't have enough information in the provided context."

"""

llm = ChatOllama(model=LLM_MODEL)

response = llm.invoke(prompt)

print("\nFinal Answer:")
print(response.content)