import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Пути для хранения данных в Streamlit
STORAGE_DIR = Path('.streamlit')
STORAGE_DIR.mkdir(exist_ok=True)

# API ключи
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Модель для embeddings
EMBEDDING_MODEL = "intfloat/multilingual-e5-large"