import json


class ConfigLoader:
    def __init__(self, config_path):
        self.config_path = config_path
        self.config_data = self.load_config()

    def load_config(self):
        with open(self.config_path, 'r') as config_file:
            return json.load(config_file)

