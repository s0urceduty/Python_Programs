import json
import os

CONFIG_FILE = "metarobot_config.json"

def load_config():
    """Load system configuration."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            return json.load(file)
    else:
        return {}

def save_config(config):
    """Save system configuration."""
    with open(CONFIG_FILE, "w") as file:
        json.dump(config, file, indent=4)
