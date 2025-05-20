# To send a prompt to the Groq LLM API and returns the generated response
import requests

def ask_llm(prompt, api_key="your_groq_api_key", model="you_groq_model"):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a helpful shopping assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3
    }

    response = requests.post("https://api.groq.com/openai/v1/chat/completions",
                             headers=headers, json=data)
    response_json = response.json()

    if "choices" in response_json:
        return response_json["choices"][0]["message"]["content"]
    else:
        raise ValueError(f"Unexpected response structure: {response_json}")
