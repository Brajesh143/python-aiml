# import ollama
# import chromadb


# # --------------------------------
# # 1. Load document
# # --------------------------------

# with open("nodejs.txt", "r", encoding="utf-8") as file:
#     text = file.read()


# # --------------------------------
# # 2. Split document
# # --------------------------------

# def split_text(text, chunk_size=500):
#     chunks = []

#     for i in range(0, len(text), chunk_size):
#         chunk = text[i:i + chunk_size].strip()

#         if chunk:
#             chunks.append(chunk)

#     return chunks


# chunks = split_text(text)

# print("Total chunks:", len(chunks))


# # --------------------------------
# # 3. Generate embeddings
# # --------------------------------

# embedding_response = ollama.embed(
#     model="nomic-embed-text:latest",
#     input=chunks
# )

# embeddings = embedding_response["embeddings"]

# print("Embeddings generated.")


# # --------------------------------
# # 4. Store in Chroma
# # --------------------------------

# client = chromadb.Client()

# collection = client.get_or_create_collection(
#     name="nodejs_docs"
# )

# ids = [f"chunk-{i}" for i in range(len(chunks))]

# collection.add(
#     ids=ids,
#     documents=chunks,
#     embeddings=embeddings
# )

# print("Documents stored in Chroma.")


# # --------------------------------
# # 5. User question
# # --------------------------------

# question = "What is the Node.js event loop?"


# # --------------------------------
# # 6. Embed question
# # --------------------------------

# question_embedding_response = ollama.embed(
#     model="nomic-embed-text",
#     input=question
# )

# question_embedding = question_embedding_response["embeddings"][0]


# # --------------------------------
# # 7. Vector search
# # --------------------------------

# results = collection.query(
#     query_embeddings=[question_embedding],
#     n_results=2
# )

# retrieved_chunks = results["documents"][0]


# print("\nRetrieved Chunks:")

# for i, chunk in enumerate(retrieved_chunks):
#     print(f"\n--- Chunk {i} ---")
#     print(chunk)


# # --------------------------------
# # 8. Build prompt
# # --------------------------------

# context = "\n\n".join(retrieved_chunks)

# prompt = f"""
# Answer the question using only the provided context.

# Context:
# {context}

# Question:
# {question}

# If the answer is not available in the context,
# say "I don't have enough information in the provided context."

# Answer:
# """


# # --------------------------------
# # 9. Generate answer using Ollama
# # --------------------------------

# response = ollama.chat(
#     model="llama3:8b",
#     messages=[
#         {
#             "role": "user",
#             "content": prompt
#         }
#     ],
#     options={
#         "temperature": 0.2
#     }
# )


# # --------------------------------
# # 10. Print final answer
# # --------------------------------

# answer = response["message"]["content"]

# print("\nFinal Answer:")
# print(answer)

from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = TextLoader("nodejs.txt")

doc = loader.load()

# print(doc)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 500,
    chunk_overlap = 50
)

chunk = text_splitter.split_documents(doc)

embeddings = OllamaEmbeddings(model="nomic-embed-text:latest")

vectorstore = Chroma.from_documents(
    documents=chunk,
    embedding=embeddings,
    collection_name="nodejs_docs"
)

retriever = vectorstore.as_retriever(
    search_kwargs={
        "k": 2
    }
)

question = "What is the Node.js event loop?"


# -----------------------------------------
# 7. Retrieve Relevant Documents
# -----------------------------------------

retrieved_docs = retriever.invoke(question)

print("\nRetrieved Documents:")

for i, doc in enumerate(retrieved_docs):
    print(f"\n--- Document {i} ---")
    print(doc.page_content)

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