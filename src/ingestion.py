import fitz  # PyMuPDF
import chromadb
from sentence_transformers import SentenceTransformer
import os

# --- Constantes ---
PDF_PATH = "data/CV_Alternance_DS_Chayane_KHA.pdf"
CHROMA_DIR = "chroma_db"
COLLECTION_NAME = "cv_collection"

# --- 1. Lire le PDF ---
def lire_pdf(path):
    doc = fitz.open(path)
    texte = ""
    for page in doc:
        texte += page.get_text()
    print(f"✅ PDF lu — {len(texte)} caractères extraits")
    return texte

# --- 2. Découper en chunks ---
def chunker(texte, taille=300, chevauchement=50):
    chunks = []
    debut = 0
    while debut < len(texte):
        fin = debut + taille
        chunk = texte[debut:fin]
        chunks.append(chunk)
        debut += taille - chevauchement
    print(f"✅ {len(chunks)} chunks créés")
    return chunks

# --- 3. Embedder et stocker dans ChromaDB ---
def stocker_chunks(chunks):
    # Charger le modèle d'embeddings
    modele = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = modele.encode(chunks).tolist()
    print(f"✅ Embeddings générés")

    # Connexion à ChromaDB
    client = chromadb.PersistentClient(path=CHROMA_DIR)

    # Supprimer la collection si elle existe déjà (pour éviter les doublons)
    try:
        client.delete_collection(COLLECTION_NAME)
    except:
        pass

    collection = client.create_collection(COLLECTION_NAME)

    # Stocker les chunks avec leurs embeddings
    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=[f"chunk_{i}" for i in range(len(chunks))]
    )
    print(f"✅ {len(chunks)} chunks stockés dans ChromaDB")

# --- Point d'entrée ---
if __name__ == "__main__":
    print("🚀 Démarrage de l'ingestion...")
    texte = lire_pdf(PDF_PATH)
    chunks = chunker(texte)
    stocker_chunks(chunks)
    print("🎉 Ingestion terminée !")