import requests


class APIHandler:
    def __init__(self, api_key, model_name):
        self.api_key = api_key
        self.model_name = model_name
        self.base_url = "https://api.openai.com/v1/chat/completions"

    def call_gpt4_chat_api(self, prompt):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": self.model_name,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 4000
        }
        response = requests.post(self.base_url, headers=headers, json=data)
        return response.json()
