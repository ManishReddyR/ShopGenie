# Searche for the top-k most relevant products based on the query.
import numpy as np

def search_products(query, model, index, df, top_k=5):
    query_vec = model.encode([query])
    scores, indices = index.search(np.array(query_vec), top_k)

    return df.iloc[indices[0]]