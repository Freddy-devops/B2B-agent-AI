# 1. Suppression des avertissements système (EN PREMIÈRE LIGNE)
import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)

# 2. Installation des dépendances (Commande Colab)
!pip install --upgrade crewai litellm google-generativeai python-dotenv -q

import os
import nest_asyncio
from crewai import Agent, Task, Crew, LLM
from crewai.tools import tool

# 3. Gestion universelle de l'environnement (Local/Colab/Cloud)
nest_asyncio.apply()

try:
    from google.colab import userdata
    os.environ["GEMINI_API_KEY"] = userdata.get('GEMINI_API_KEY')
    print("Environnement détecté : Google Colab")
except ImportError:
    from dotenv import load_dotenv
    load_dotenv()
    print("Environnement détecté : Serveur Cloud / Local (via .env)")

# 4. Initialisation du modèle
cerveau_gemini = LLM(
    model="gemini/gemini-3.5-flash-lite",
    api_key=os.environ["GEMINI_API_KEY"]
)

# ==========================================
# 5. OUTIL DE BASE DE DONNÉES INTERNE
# ==========================================
@tool("Recherche dans la base de donnees interne")
def recherche_doc(requete: str) -> str:
    """Cherche la bonne procédure d'entreprise en fonction de l'intention et du niveau d'urgence."""
    requete_lower = requete.lower()
    
    if "support" in requete_lower or "critique" in requete_lower or "crash" in requete_lower:
        return """PROCÉDURE D'URGENCE (CRASH SERVEUR) : 
        1. Créer un ticket de maintenance de niveau 1. 
        2. Assigner immédiatement l'équipe DevOps de garde. 
        3. Informer le client que l'équipe intervient sous 15 minutes."""
    elif "devis" in requete_lower or "tarif" in requete_lower:
        return "TARIFS : Le prix de base pour un audit est de 5000$. Envoyer la plaquette commerciale."
    
    return "PROCÉDURE GÉNÉRALE : Accuser réception de la demande et transmettre au service client sous 24h."

# ==========================================
# 6. LES AGENTS
# ==========================================
agent_analyste = Agent(
    role="Spécialiste en Qualification de Prospects B2B",
    goal="Analyser les messages entrants en anglais pour extraire les informations clés, identifier le besoin et évaluer l'urgence.",
    backstory="Tu es le premier point de contact d'une entreprise technologique. Tu catégorises précisément les demandes (Devis, Support, Information, Spam) et leur niveau d'urgence.",
    llm=cerveau_gemini,
    verbose=True,
    allow_delegation=False
)

agent_chercheur = Agent(
    role="Spécialiste en Documentation Interne",
    goal="Trouver la procédure exacte à appliquer selon le problème identifié chez le prospect.",
    backstory="Tu es le gardien du savoir de l'entreprise. Tu utilises ton outil de recherche pour fournir les étapes factuelles à suivre.",
    llm=cerveau_gemini,
    tools=[recherche_doc],
    verbose=True,
    allow_delegation=False
)

agent_redacteur = Agent(
    role="Responsable de la Communication Client B2B",
    goal="Rédiger des réponses emails professionnelles, empathiques et claires en anglais.",
    backstory="Tu sais parler à un client en crise. Tu traduis la procédure technique en un plan d'action rassurant sans mentionner le jargon interne.",
    llm=cerveau_gemini,
    verbose=True,
    allow_delegation=False
)

# ==========================================
# 7. CONFIGURATION D'ENTRÉE (SIMULATION ENTRÉE API CLOUD)
# ==========================================
MESSAGE_CLIENT_ENTRANT = "Hello, my name is Michael Smith. Our database just crashed and we urgently need someone to look at our servers. Please contact me at m.smith@techcorp.com."

# ==========================================
# 8. LES TÂCHES
# ==========================================
task_qualification = Task(
    description=f"""Analyse ce message entrant : '{MESSAGE_CLIENT_ENTRANT}'
    Extrais : Nom du client, Email, Intention principale (Devis, Support technique, Spam, Information) et Niveau d'urgence (Bas, Moyen, Critique).""",
    expected_output="Analyse structurée des données du client.",
    agent=agent_analyste
)

task_recherche = Task(
    description="Prends le résultat de la qualification du client et utilise ton outil de recherche pour trouver la procédure interne correspondante.",
    expected_output="Procédure interne exacte à appliquer.",
    agent=agent_chercheur
)

task_redaction = Task(
    description="Utilise la procédure trouvée pour rédiger un email de réponse complet (Objet, Corps, Signature) en anglais destiné au client. Sois professionnel et rassurant.",
    expected_output="Un email complet rédigé en anglais, prêt à l'envoi.",
    agent=agent_redacteur
)

# ==========================================
# 9. EXÉCUTION DU SYSTÈME
# ==========================================
equipe_support_b2b = Crew(
    agents=[agent_analyste, agent_chercheur, agent_redacteur],
    tasks=[task_qualification, task_recherche, task_redaction],
    verbose=True
)

print("\n🚀 Démarrage du traitement du message client...")
resultat_support = await equipe_support_b2b.kickoff_async()

print("\n\n========================================")
print("📩 EMAIL CLIENT PRÊT À L'ENVOI :")
print("========================================\n")
print(resultat_support)
