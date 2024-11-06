import json
from pathlib import Path
import streamlit as st
import google.generativeai as genai
from src.config import GEMINI_API_KEY

class GraphStore:
    def __init__(self):
        self.graph_path = Path('.streamlit/graph.json')
        self.graph_path.parent.mkdir(exist_ok=True)
        
        # Инициализация Gemini
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel("gemini-1.5-flash-002")
        
        self.load_or_create_graph()
    
    def extract_graph_data(self, text: str):
        """Извлечение графа через Gemini"""
        response = self.model.generate_content([
            "Извлеки из текста сущности и связи в формате JSON.",
            text
        ])
        return json.loads(response.text)