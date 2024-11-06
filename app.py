import streamlit as st
import google.generativeai as genai
from src.rag_system import RAGSystem
from src.config import GEMINI_API_KEY

# Настройка страницы
st.set_page_config(page_title="Graph RAG Demo", layout="wide")

# Инициализация Gemini и RAG
genai.configure(api_key=GEMINI_API_KEY)
rag = RAGSystem()

def main():
    st.title("Graph RAG System")
    
    # Загрузка документов
    uploaded_files = st.file_uploader(
        "Загрузите документы",
        accept_multiple_files=True,
        type=['txt', 'pdf']
    )
    
    if uploaded_files:
        for file in uploaded_files:
            # Чтение текста
            text = file.getvalue().decode('utf-8')
            
            # Обработка документа
            with st.spinner(f'Обработка {file.name}...'):
                result = rag.process_document(
                    text,
                    metadata={"filename": file.name}
                )
                st.success(result)
    
    # Поисковый интерфейс
    query = st.text_input("Ваш вопрос:")
    if query:
        with st.spinner('Поиск...'):
            # Получение контекста
            results = rag.search(query)
            
            # Генерация ответа через Gemini
            model = genai.GenerativeModel("gemini-1.5-flash-002")
            response = model.generate_content([
                "На основе следующего контекста ответь на вопрос на русском языке.",
                f"Векторный поиск: {results['vector']}",
                f"Графовый поиск: {results['graph']}",
                f"Вопрос: {query}"
            ])
            
            # Вывод результатов
            st.write("Ответ:", response.text)
            
            # Показать источники
            with st.expander("Источники"):
                st.write("Векторный поиск:", results['vector'])
                st.write("Графовый поиск:", results['graph'])

if __name__ == "__main__":
    main()