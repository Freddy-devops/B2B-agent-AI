# Autonomous B2B Support & Regional Compliance AI Suite (Code Caméléon)

An enterprise-grade multi-agent B2B solution built with CrewAI for technical support automation, lead qualification, and dynamic international legal compliance (EU AI Act, GDPR, CCPA).

## 🚀 Key Features

* **🛡️ Prompt Injection Firewall**: Input stream isolation using strict boundary tagging (`<message_client>`) to neutralize prompt injection attacks.
* **🌍 "Code Caméléon" Architecture**: Automatic geographic origin detection (ISO Country Code) and dynamic injection of mandatory legal disclaimers based on jurisdiction (EU AI Act for Europe, CAN-SPAM opt-out for the US).
* **🔑 Multi-Tenant Isolation & GDPR Kill Switch**: Isolated client data management paired with a targeted purge tool (Right to be Forgotten), enabling instant deletion of a specific client's data without affecting other entities.
* **⚡ Production-Ready & Async**: Optimized asynchronous execution pipeline (`kickoff_async`) built for serverless Cloud deployment (AWS Lambda, Render, GCP).

## 🛠️ Tech Stack

* **Multi-Agent Framework**: [CrewAI](https://github.com/joaomdmoura/crewai)
* **LLM Engine**: Gemini 3.5 Flash-lite (via `litellm`)
* **Language**: Python 3.10+
* **Environment Management**: `python-dotenv`, `nest_asyncio`

## 📂 Repository Structure

```text
b2b-support-agent/
├── .gitignore          # Files excluded from Git tracking (.env, caches)
├── requirements.txt    # Project dependencies
├── README.md           # Main project documentation
├── SECURITY.md         # Security policy and compliance standards
└── main.py             # Source code for agents and workflows