import streamlit as st
from orchestrator.main_orchestrator import run_pipeline
from gtts import gTTS
from agents.voice_agent import text_to_speech

st.title("Morning Market Brief Assistant")

query = st.text_input("Ask your query:")
if st.button("Run Agent"):
    result = run_pipeline(query)
    st.write(result)
    text_to_speech(result)
