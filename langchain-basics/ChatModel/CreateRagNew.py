from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

model = ChatOllama(
    model = "qwen3:0.6b",
    temperature = 0.7,
)

loader = TextLoader("engineering_policy.txt")
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
texts = splitter.split_documents(documents)

embeddings = OllamaEmbeddings(model="nomic-embed-text:latest")

vector_store = Chroma.from_documents(
    documents=texts,
    embedding=embeddings,
)

retriever = vector_store.as_retriever(
    search_kwargs={
        "k": 3
    }
)

question = "What is the Engineering leave policy?"

retrieved_docs = retriever.invoke(question)

context = "\n\n".join(
    doc.page_content for doc in retrieved_docs
)

prompt = f"""
Answer the question using only the provided context.

context:
{context}

question:
{question}
"""

response = model.invoke(prompt)

print("Response:")
print(response.content)




