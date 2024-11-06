from txtai.embeddings import Embeddings
from txtai.pipeline import Pipeline

class VectorStore:
    def __init__(self):
        self.embeddings = self._setup_embeddings()
        self.pipeline = Pipeline(self.embeddings)
    
    def _setup_embeddings(self):
        """Настройка модели для embeddings"""
        config = {
            "path": "intfloat/multilingual-e5-large",  # Напрямую указываем модель
            "dimension": 1024,
            "multilingual": True,
            "language": "ru"
        }
        return Embeddings(config)