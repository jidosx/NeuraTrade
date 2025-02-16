import os
import sys

def configure_plugin():
    # Get the model path and DeepSeek API key from the user
    model_path = input("Enter the path to the NeuraDSP model: ")
    deepseek_api_key = input("Enter your DeepSeek API key: ")

    # Create a configuration file
    with open("config.json", "w") as f:
        f.write(f'{{"model_path": "{model_path}", "deepseek_api_key": "{deepseek_api_key}"}}')

if __name__ == "__main__":
    configure_plugin()
