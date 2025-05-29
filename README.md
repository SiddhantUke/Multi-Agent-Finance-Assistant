# Multi-Agent-Finance-Assistant
AI-powered multi-agent finance assistant built with open-source LLMs, real-time market data, semantic search, and voice interaction—deployed on Streamlit.


🧠 Multi-Agent Finance Assistant
The Multi-Agent Finance Assistant is an AI-powered Streamlit app that provides real-time market analysis, financial news summarization, risk insights, and voice interaction. Built with a modular agent-based architecture, it integrates open-source LLMs, web scraping, speech processing, and vector retrieval—all orchestrated for dynamic finance query handling.

🚀 Key Features
Agent-Based Design: Modular agents for API fetching, web scraping, risk analysis, retrieval, generation, and voice.

Open-Source LLMs: Uses Hugging Face models like Mistral and TinyLlama via ctransformers.

Real-Time Data: Pulls market data (e.g., TSMC, Samsung) and earnings news from reliable sources like Yahoo Finance and Reuters.

Semantic Search: Context-aware response generation using FAISS + sentence transformers.

Speech Interface: Converts queries to text with Whisper and responses back to speech using gTTS.

Streamlit Frontend: Intuitive web UI for interaction and report generation.

🧱 Tech Stack
LLMs: Mistral / TinyLlama (ctransformers)

Vector Store: FAISS

NLP Models: Sentence-Transformers

Voice Processing: Whisper, gTTS

Frameworks: Streamlit, FastAPI (optional), LangGraph or CrewAI (extensible)

Data Sources: Yahoo Finance, Reuters

📦 Folder Structure

finance-assistant/
├── agents/               # All individual agent modules
├── data_ingestion/       # Market data loader
├── orchestrator/         # Main pipeline logic
├── streamlit_app/        # UI entry point
├── docs/                 # Documentation
├── requirements.txt
├── Dockerfile
└── README.md


✅ Deployment
Easily deployable via Streamlit Cloud by linking your GitHub repo and pointing to streamlit_app/app.py.




