from sentence_transformers import SentenceTransformer
import numpy as np


model_name = "intfloat/multilingual-e5-large"
model = SentenceTransformer(model_name)
PREFIX_QUERY = "query: "


CHUNK_SIZE = 500


def get_embeddings(text: str, query=False) -> np.ndarray:
    if query:
        text = PREFIX_QUERY + text
    texts = [text[i : i + CHUNK_SIZE] for i in range(0, len(text), CHUNK_SIZE)]
    embeddings = model.encode(texts)
    # print(embeddings.shape)
    # print(type(embeddings))
    return embeddings
