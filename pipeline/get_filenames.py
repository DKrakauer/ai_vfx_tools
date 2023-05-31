import os

def print_file_names(folder_path):
    for root, dirs, files in os.walk(folder_path):
        folder_name = os.path.basename(root)
        print(f"Folder: {folder_name}")
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if file_path.endswith(".mat") or file_name.endswith('.prefab'):
                file_name_with_subfolder = os.path.join(folder_name, file_name)
                print(file_path + file_name_with_subfolder)

# Usage example
folder_path = "UnityTechnologies\ParticlePack"
print_file_names(folder_path)
