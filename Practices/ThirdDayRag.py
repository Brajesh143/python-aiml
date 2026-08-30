from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

CHUNK_SIZE = 200
CHUNK_OVERLAP = 20

LLM_MODEL = "llama3:8b"
EMBED_MODEL = "nomic-embed-text:latest"

TOP_K = 2

# Document Loader
loader = TextLoader("nodejs.txt")
docs = loader.load()

# print(len(docs))

# Document Spliiter

splitter = RecursiveCharacterTextSplitter(
    chunk_size= CHUNK_SIZE,
    chunk_overlap = CHUNK_OVERLAP
)

splitted_text = splitter.split_documents(docs)

print("=========\n ",len(splitted_text), splitted_text)

# Embedding

embeddings = OllamaEmbeddings(model=EMBED_MODEL)

# Vector Store
vector_store = Chroma.from_documents(
    documents=splitted_text,
    embedding=embeddings,
    collection_name="new-rag-demo"
)

# Retriver

retriver = vector_store.as_retriever(
    search_kwargs={
        "k": TOP_K
    }
)

question = "What is LangGraph do in Agentic AI?"

retriver_data = retriver.invoke(question)

print("-------- \n", len(retriver_data), retriver_data)

context = "\n\n".join(
   doc.page_content for doc in retriver_data
)

print("=============\n", context)

prompt = f"""
Answer the {question} using only provided {context}.

If the answer is not available in the context,
say "I don't have enough information in the provided context."

"""

llm = ChatOllama(model=LLM_MODEL)

response = llm.invoke(prompt)

print("\nFinal Answer:")
print(response.content)

# ⭐ Most Important Debugging Trick

# When debugging RAG, print these four things:

# Then you can visually inspect:

# Remember this rule

# Wrong retrieved chunks → Retrieval problem

# Correct chunks + wrong answer → Prompt/LLM problem

# Correct answer from manual context but wrong answer from retrieved context → Retrieval problem

# Correct RAG answer but occasionally different wording → Generation/model behavior