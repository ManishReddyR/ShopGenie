# Computes sentence embeddings from input CSV data and builds a FAISS index.
import numpy as np
import pandas as pd
import faiss
import os
from sentence_transformers import SentenceTransformer


def compute_embeddings_and_index(data_path):
    """
    Generates embeddings and builds a FAISS index.

    Parameters:
        data_path (str): Path to the data.

    Returns:
        index (faiss.IndexFlatL2): FAISS index built from embeddings.
        model (SentenceTransformer): The embedding model used.
        df (pd.DataFrame): The original dataframe loaded from the CSV.
    """
    df = pd.read_csv(data_path)
    texts = df['Text_Embedding'].tolist()
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(texts, show_progress_bar=True)

    embd_matrix = np.array(embeddings).astype('float32')
    index = faiss.IndexFlatL2(embd_matrix.shape[1])
    index.add(embd_matrix)
    
    os.makedirs("embeddings", exist_ok=True)
    faiss.write_index(index, "embeddings/faiss_index.faiss")

    return index, model, df
