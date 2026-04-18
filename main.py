import warnings
warnings.filterwarnings("ignore")
import os
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.generation import generer_reponse

def main():
    print("=" * 50)
    print("🤖 Analyseur de CV — Posez vos questions !")
    print("=" * 50)
    print("💡 Tapez 'quitter' pour arrêter\n")

    while True:
        question = input("❓ Votre question : ").strip()
        
        if question.lower() == "quitter":
            print("👋 Au revoir !")
            break
        
        if question == "":
            print("⚠️  Veuillez entrer une question\n")
            continue
        
        print("\n⏳ Recherche en cours...\n")
        reponse = generer_reponse(question)
        print(f"🤖 Réponse :\n{reponse}")
        print("\n" + "-" * 50 + "\n")

if __name__ == "__main__":
    main()