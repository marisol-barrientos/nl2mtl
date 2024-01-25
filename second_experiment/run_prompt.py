import json
import requests

def read_prompt(file_path):
    with open(file_path, 'r') as file:
        prompt = file.read()
    return prompt

def call_gpt4_chat_api(prompt, api_key, model_name):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model_name,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 4000
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()


def save_to_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    api_key = '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'  # Replace with your actual API key
    input_file = '/home/marisolbarrientosmoreno/Desktop/1st_semester_phd/nl2mtl/second_experiment/input/article_80.txt'  # Replace with your input file path
    output_file = '/home/marisolbarrientosmoreno/Desktop/1st_semester_phd/nl2mtl/second_experiment/output/article_80_output.json'  # Replace with your desired output file path
    model_name = 'gpt-4'

    try:
        prompt = read_prompt(input_file)
        api_response = call_gpt4_chat_api(prompt, api_key, model_name)
        save_to_json(api_response, output_file)
        print("Output saved to", output_file)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
