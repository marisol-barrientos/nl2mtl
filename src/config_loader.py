import json
import os

class ConfigLoader:
    def __init__(self, config_path):
        # Get the absolute path of the directory where the script is located
        self.script_dir = os.path.dirname(__file__)
        self.parent_dir = os.path.dirname(self.script_dir)
        # Construct the absolute path of the config file
        self.config_path = os.path.join(self.parent_dir, config_path)
        self.config_data = self.load_config()

    def load_config(self):
        with open(self.config_path, 'r') as config_file:
            return json.load(config_file)
