from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

# Document Loader
loader = PyPDFLoader("dl-curriculum.pdf")

docs = loader.load()

# Document Splitter

split_docs = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = split_docs.split_documents(docs)

# Embeddings

embeddings = OllamaEmbeddings(model="nomic-embed-text:latest")

# vector store

vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    collection_name="rag-basic"
)

# retriever
retriever = vector_store.as_retriever(
    search_kwargs={
        "k": 2
    }
)

# Retrieve docs

question = "What is the Node.js event loop?"

retrieved_docs = retriever.invoke(question)

# LLM
llm = ChatOllama(
    model="qwen3:0.6b",
    temperature=0.2
)

# -----------------------------------------
# 9. Create Prompt
# -----------------------------------------

context = "\n\n".join(
    doc.page_content for doc in retrieved_docs
) 

prompt = f"""
Answer the question using only the provided context.

Context:
{context}

Question:
{question}

If the answer is not available in the context,
say "I don't have enough information in the provided context."

Answer:
"""


# -----------------------------------------
# 10. Generate Answer
# -----------------------------------------

response = llm.invoke(prompt)

print("\nFinal Answer:")
print(response.content)