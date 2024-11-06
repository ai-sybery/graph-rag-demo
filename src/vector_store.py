class VectorStore:
    def __init__(self):
        self.embeddings = self._setup_embeddings()
        self.pipeline = Pipeline(self.embeddings)
    
    def _setup_embeddings(self):
        config = {
            "path": EMBEDDING_MODEL,
            "dimension": 1024,
            "multilingual": True,
            "language": "ru"  # Добавили русский язык
        }
        return Embeddings(config)