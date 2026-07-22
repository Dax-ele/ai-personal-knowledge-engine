from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


class EmbeddingService:

    def __init__(self):
        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )


    def encode(self, texts):
        """
        Trasforma una lista di testi in embeddings
        """
        return self.model.encode(texts)


    def similarity(self, text1, text2):
        """
        Calcola la similarità tra due testi
        """

        embeddings = self.encode(
            [text1, text2]
        )

        score = cosine_similarity(
            [embeddings[0]],
            [embeddings[1]]
        )

        return float(score[0][0])