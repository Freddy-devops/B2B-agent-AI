# Autonomous B2B Support & Lead Qualification AI Suite

Une suite multi-agents IA conçue avec CrewAI pour automatiser le tri, la qualification de leads B2B et la génération de réponses support personnalisées en temps réel.

## 🚀 Fonctionnalités

* **Qualification Automatique (Agent Analyste)** : Analyse des messages entrants, extraction des métadonnées (Nom, Email), catégorisation de la demande (Devis, Support, Spam) et évaluation du niveau d'urgence.
* **Recherche Contextuelle (Agent Chercheur)** : Interrogation de la base de données interne ou de la documentation technique via un outil dédié (`@tool`) pour identifier la procédure exacte.
* **Rédaction Professionnelle (Agent Rédacteur)** : Traduction des procédures internes en e-mails rassurants et structurés, rédigés en anglais professionnel.
* **Architecture Serverless Ready** : Code asynchrone (`kickoff_async`), optimisé pour un déploiement Cloud (AWS Lambda, Render, Google Cloud Functions).

## 🛠️ Stack Technique

* **Framework Multi-Agents** : [CrewAI](https://github.com/joaomdmoura/crewai)
* **LLM Engine** : Gemini 3.5 Flash-lite (via `litellm`)
* **Langage** : Python 3.10+
* **Gestion des Environnements** : `python-dotenv` & `nest_asyncio`

## 📂 Structure du Projet

```text
b2b-support-agent/
├── .gitignore          # Exclusion des secrets et fichiers temporaires
├── requirements.txt    # Dépendances du projet
├── README.md           # Documentation du dépôt
└── main.py             # Script principal d'exécution des agents
