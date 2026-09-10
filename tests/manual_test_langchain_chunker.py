from langchain_text_splitters import RecursiveCharacterTextSplitter

from ai_brain.documents.loader import DocumentLoader


loader = DocumentLoader()

# Carichiamo i documenti originali
documents = loader.load()

# Creiamo lo splitter LangChain
splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)

# Prendiamo il documento Java
document = next(
    document
    for document in documents
    if document.id == "java"
)

# Dividiamo il documento usando LangChain
chunks = splitter.split_text(
    document.content
)

print(f"Documento: {document.title}")
print(f"Numero chunk: {len(chunks)}")

for index, chunk in enumerate(chunks):
    print("\n---")
    print(f"Chunk index: {index}")
    print(f"Content:\n{chunk}")