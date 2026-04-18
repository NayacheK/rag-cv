import os
from dotenv import load_dotenv
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.retrieval import rechercher
from groq import Groq

# Charger la clé API depuis .env
load_dotenv()

def generer_reponse(question):
    # --- 1. Récupérer les chunks pertinents ---
    chunks = rechercher(question)
    contexte = "\n\n".join(chunks)
    
    # --- 2. Construire le prompt ---
    prompt = f"""Tu es un assistant qui analyse des documents.
Réponds uniquement en te basant sur le contexte fourni.
Si la réponse n'est pas dans le contexte, dis-le clairement.

Contexte :
{contexte}

Question : {question}
"""
    
    # --- 3. Appeler Claude ---
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    # --- 4. Retourner la réponse ---
    reponse = response.choices[0].message.content
    return reponse

# --- Test rapide ---
if __name__ == "__main__":
    question = "Quelles sont les compétences techniques ?"
    print(f"❓ Question : {question}\n")
    reponse = generer_reponse(question)
    print(f"🤖 Réponse :\n{reponse}")