import json



def get_config(config_file_path="/config/streamer_config.json"):
    with open(config_file_path, 'r') as file:
        return json.load(file)


if __name__ == "__main__":
    config_file = "/config/config.json"
    config = get_config()