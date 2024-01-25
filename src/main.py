import os

from json_to_html import JsonToHtmlConverter
from config_loader import ConfigLoader
from file_handler import FileHandler
from api_handler import APIHandler

import json


def main():
    config_loader = ConfigLoader("./config.json")
    config_data = config_loader.config_data
    script_dir = os.path.dirname(__file__)
    parent_dir = os.path.dirname(script_dir)

    file_handler = FileHandler()
    api_handler = APIHandler(config_data['api_key'], config_data['model_name'])


    try:
        input_text = file_handler.read_file(parent_dir + config_data['input_file'])
        prompt = file_handler.read_file(parent_dir + config_data['prompt_file']).replace(
            "NATURAL_LANGUAGE_TEXT_HERE", input_text
        )

        api_response = api_handler.call_gpt4_chat_api(prompt)
        file_handler.write_file(api_response, parent_dir + config_data['in_between_output_file'])

        processed_data = json.loads(api_response['choices'][0]['message']['content'])
        file_handler.write_file(processed_data, parent_dir + config_data['output_file'])

        print("Output saved to", parent_dir + config_data['output_file'])

        converter = JsonToHtmlConverter(parent_dir + config_data['output_file'], parent_dir + config_data['html_output_file'])
        converter.convert()

    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    main()
