# ETL Pipeline for Flipkart Product Data
import pandas as pd
import ast

# 1: Extract
def extract(file_path):
    return pd.read_csv(file_path)

# 2: Transform
def transform(data):
    data = data.dropna()
    data = data.drop(['product_rating', 'overall_rating',
                        'uniq_id', 'crawl_timestamp', 'pid',
                        'is_FK_Advantage_product'], axis=1)
    
    data['product_category_tree'] = data['product_category_tree'].apply(
        lambda x: ast.literal_eval(x)[0] if pd.notna(x) else ""
        )
    data["Text_Embedding"] = (
    data['product_url'] + " | " +
    data["product_name"] + " | " +
    data["product_category_tree"] + " | " +
    data['retail_price'].astype(str) + " | " +
    data['discounted_price'].astype(str) + " | " +
    data['image'] + " | " +
    data['description'] + " | " +
    data['brand'] + " | " +
    data["product_specifications"]
    )

    return data

# 3 : load
def load(data, file_path):
    data.to_csv(file_path, index=False)
    return file_path