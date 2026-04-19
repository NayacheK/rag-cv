# Analyseur de Documents PDF par RAG

Système de questions-réponses sur des documents PDF utilisant
l'architecture RAG (Retrieval-Augmented Generation).

## Description

Ce projet permet d'interroger n'importe quel document PDF en langage naturel.
Le système retrouve les passages pertinents et génère une réponse 
contextuelle grâce à un LLM.

## Architecture

PDF → Ingestion → ChromaDB → Retrieval → LLM → Réponse

## Stack technique

- Python
- ChromaDB — base de données vectorielle
- Sentence-Transformers — embeddings sémantiques
- Groq API (Llama 3.3) — génération de réponses
- PyMuPDF — extraction de texte PDF

## Installation

```bash
git clone https://github.com/ton-username/rag-cv
cd rag-cv
python -m venv .venv
.venv\Scripts\activate
pip install pymupdf sentence-transformers chromadb groq python-dotenv
```

## Configuration

Crée un fichier `.env` :

GROQ_API_KEY=ta-clé-api

## Utilisation

1. Ajoute ton PDF dans le dossier `data/`
2. Lance l'ingestion :
```bash
python src/ingestion.py
```
3. Lance l'interface :
```bash
python main.py
```

## Exemple

Question : Quelles sont les compétences techniques ?
Réponse : Python, Java, SQL, Pandas, Scikit-Learn, TensorFlow...

## Auteur

Chayane KHA