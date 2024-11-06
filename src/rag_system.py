from src.graph_store import GraphStore
from src.vector_store import VectorStore
import streamlit as st

class RAGSystem:
    def __init__(self):
        # Инициализация хранилищ в session_state
        if 'graph_store' not in st.session_state:
            st.session_state.graph_store = GraphStore()
        if 'vector_store' not in st.session_state:
            st.session_state.vector_store = VectorStore()
    
    def process_document(self, text: str, metadata: dict = None):
        """Обработка документа"""
        # Векторное индексирование
        st.session_state.vector_store.pipeline.index([(text, metadata)])
        
        # Извлечение и сохранение графа
        graph_data = st.session_state.graph_store.extract_graph_data(text)
        st.session_state.graph_store.save_graph()
        
        return "Документ обработан"

    def search(self, query: str, top_k: int = 5):
        """Гибридный поиск"""
        # Векторный поиск
        vector_results = st.session_state.vector_store.pipeline.search(query, top_k)
        
        # Поиск по графу
        graph = st.session_state.graph_store.graph
        graph_results = [entity for entity in graph['entities'].values() 
                        if query.lower() in entity['name'].lower()][:top_k]
        
        return {
            "vector": vector_results,
            "graph": graph_results
        }