import os
import subprocess
import shutil

REPO_URL = "https://github.com/fbaptiste/python-deepdive.git"
TEMP_DIR = "_temp_python_deepdive"

# Clean up if exists
if os.path.exists(TEMP_DIR):
    shutil.rmtree(TEMP_DIR)

print("Cloning repository...")
subprocess.run(["git", "clone", "--depth", "1", REPO_URL, TEMP_DIR], check=True)

print("Creating folder structure...")

for root, dirs, files in os.walk(TEMP_DIR):
    # skip .git
    if ".git" in root:
        continue

    relative_path = os.path.relpath(root, TEMP_DIR)
    if relative_path == ".":
        continue

    os.makedirs(relative_path, exist_ok=True)

    for file in files:
        file_path = os.path.join(relative_path, file)
        open(file_path, "a").close()

# Cleanup
shutil.rmtree(TEMP_DIR)

print("✅ Folder structure created successfully")
