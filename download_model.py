from huggingface_hub import hf_hub_download
import os

# Define the model details
repo_id = "Qwen/Qwen3-VL-2B-Instruct-GGUF"

# List of filenames to download
filenames = ["Qwen3VL-2B-Instruct-Q4_K_M.gguf", "mmproj-Qwen3VL-2B-Instruct-Q8_0.gguf"]

# Define the local directory to save the models
# You can change this to your preferred path
local_dir = "./models"

# Create the directory if it doesn't exist
os.makedirs(local_dir, exist_ok=True)

print(f"Attempting to download files from {repo_id}...")

for filename in filenames:
    try:
        # Download the model
        model_path = hf_hub_download(
            repo_id=repo_id,
            filename=filename,
            local_dir=local_dir,
        )
        print(f"File '{filename}' downloaded successfully to: {model_path}")
    except Exception as e:
        print(f"An error occurred during download of '{filename}': {e}")

print("Download process completed.")