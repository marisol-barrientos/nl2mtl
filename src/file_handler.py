import json


class FileHandler:
    @staticmethod
    def read_file(file_path):
        with open(file_path, 'r') as file:
            return file.read()

    @staticmethod
    def write_file(data, file_path):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
