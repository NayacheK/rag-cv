import warnings
warnings.filterwarnings("ignore")
import os
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

import chromadb
from sentence_transformers import SentenceTransformer


# --- Constantes ---
CHROMA_DIR = "chroma_db"
COLLECTION_NAME = "cv_collection"
NB_RESULTATS = 3

def rechercher(question):
    # Charger le modèle d'embeddings
    modele = SentenceTransformer("all-MiniLM-L6-v2")
    
    # Transformer la question en vecteur
    vecteur_question = modele.encode([question]).tolist()
    
    # Connexion à ChromaDB
    client = chromadb.PersistentClient(path=CHROMA_DIR)
    collection = client.get_collection(COLLECTION_NAME)
    
    # Chercher les chunks les plus proches
    resultats = collection.query(
        query_embeddings=vecteur_question,
        n_results=NB_RESULTATS
    )
    
    # Retourner les textes trouvés
    chunks_pertinents = resultats["documents"][0]
    return chunks_pertinents

# --- Test rapide ---
if __name__ == "__main__":
    question = "Quelles sont les compétences techniques ?"
    print(f"❓ Question : {question}\n")
    
    chunks = rechercher(question)
    
    print("📄 Chunks trouvés :\n")
    for i, chunk in enumerate(chunks):
        print(f"--- Chunk {i+1} ---")
        print(chunk)
        print()