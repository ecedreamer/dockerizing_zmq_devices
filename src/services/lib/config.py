import json



def get_config(config_file_path="/config/config.json"):
    with open(config_file_path, 'r') as file:
        config = json.load(file)
        return config


if __name__ == "__main__":
    config_file = "/config/config.json"
    config = get_config()