import yaml
import os

def load_config():
    path = os.path.join(os.path.dirname(__file__), '../../config/config.yml')
    with open(path, 'r') as file:
        config = yaml.safe_load(file)
    return config