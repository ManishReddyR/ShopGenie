import streamlit as st
import os
from rag.embed_and_index import compute_embeddings_and_index
from rag.retriever import search_products
from rag.llm_groq import ask_llm
from etl.etl_pipeline import extract, transform, load
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
groq_model = os.getenv("GROQ_MODEL")

# Custom Styling
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        padding: 8px 20px;
        border-radius: 8px;
    }
    .stTextInput > div > div > input {
        padding: 10px;
        border-radius: 8px;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_data():
    """
    Load and preprocess the data.
    """
    data_path = "data/flipkart_com-ecommerce_sample.csv"
    df = extract(data_path)
    df = transform(df)
    load(df, "data/processed_flipkart_data.csv")
    return df

@st.cache_resource
def load_index():
    return compute_embeddings_and_index("data/processed_flipkart_data.csv")

def format_context(rows):
    context = ""
    for _, row in rows.iterrows():
        context += f"Product Name: {row['product_name']}\n"
        context += f"Description: {row['description']}\n"
        context += f"Price: ₹{row['discounted_price']}\n\n"
    return context

# UI Header
st.title("🛍️ Personal Shopping Assistant")
st.markdown("Let me help you find the best products based on your needs using RAG + LLM!")

# Input Section
st.markdown("### 🔍 Search for Products")
query = st.text_input("Enter your query (e.g., 'Formal black shoes under ₹2000')")

if st.button("Search") and query:
    with st.spinner("Searching and generating recommendations..."):
        data = load_data()
        index, model, df = load_index()
        results = search_products(query, model, index, df)
        context = format_context(results)

        prompt = f"""Based on the following product listings, help the user:\n\n{context}\n\nUser Query: {query}"""
        response = ask_llm(prompt, api_key=api_key, model=groq_model)
        
        st.write("### Assistant’s Recommendation")
        st.write(response)