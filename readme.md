<h1 align="center">ShopGenie: AI-Powered Shopping Assistant</h1>


ShopGenie is an AI-powered shopping assistant built with Streamlit, leveraging **Retrieval-Augmented Generation (RAG)** and **Groq's LLaMA model**. It allows users to find personalized product recommendations from a Flipkart dataset using semantic search and LLM-powered responses.

---

## Overview

ShopGenie helps users discover the most relevant products based on natural language queries such as:

> “Find me black sports shoes under ₹2000 with good reviews.”

The assistant performs intelligent product retrieval using embeddings and FAISS, and generates contextual suggestions using a language model.

---

## Features

- **Streamlit UI**: A user-friendly interface for querying and receiving recommendations.
  
- **ETL Pipeline**: Cleans and preprocesses Flipkart product data.
  
- **Semantic Search with FAISS**: Uses `SentenceTransformers` to encode data and retrieve top-k results.
  
- **Groq LLaMA Integration**: Generates LLM-based answers for retrieved results.
  
- **RAG Implementation**: Combines retrieved context with LLM output for insightful suggestions.

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/ManishReddyR/ShopGenie.git
cd ShopGenie
```

### 2. Install Dependencies

```bash
# (Optional) Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

# Install Python packages
pip install -r requirements.txt
```

### 3. Setup Environment Variables

Create a .env file in the root directory:

```bash
GROQ_API_KEY=your_actual_api_key_here
GROQ_Model=Selecy_your_Model
```

### 4. Run Application

```bash
streamlit run ShopAsssistant.py
```

---

## Usage

- **Enter Your Query**:Describe what you're looking for in natural language.
  
- **Review Suggestions**: View the top recommendations and product details.

- **Understand Context**: Responses are generated based on real product metadata.

---

## Dependencies

- [Python 3.11+](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [SentenceTransformers](https://www.sbert.net/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Pandas](https://pandas.pydata.org/)
- [NumPy](https://numpy.org/)

---

## Contributing

Contributions are welcome! <br>
If you have suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request.
