import json
import streamlit as st
import google.generativeai as genai
from src.config import GEMINI_API_KEY

class GraphStore:
    def __init__(self):
        # Инициализация Gemini
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel("gemini-1.5-flash-002")
        
        # Инициализация графа в session_state
        if 'graph' not in st.session_state:
            st.session_state.graph = {
                'entities': {},
                'relations': [],
                'next_id': 0
            }
    
    def save_graph(self):
        """Сохранение в session_state"""
        # Граф уже в session_state
        pass
    
    def extract_graph_data(self, text: str):
        """Извлечение графа через Gemini"""
        response = self.model.generate_content([
            "Извлеки из текста сущности и связи в формате JSON.",
            text
        ])
        return json.loads(response.text)