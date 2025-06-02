def preprocess_message(message):
    # Function to preprocess the message text
    # This can include lowercasing, removing special characters, etc.
    return message.lower().strip()

def format_output(autism_level):
    # Function to format the autism level output
    return f"Autism Level: {autism_level:.2f}"

def load_model_config(config_path):
    # Function to load model configuration from a file
    import json
    with open(config_path, 'r') as config_file:
        return json.load(config_file)

def save_model_config(config, config_path):
    # Function to save model configuration to a file
    import json
    with open(config_path, 'w') as config_file:
        json.dump(config, config_file, indent=4)