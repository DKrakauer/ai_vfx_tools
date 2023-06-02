import os

def print_file_names(folder_path):
    for root, dirs, files in os.walk(folder_path):
        folder_name = os.path.basename(root)
        print(f"Folder: {folder_name}")
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if file_path.endswith(".mat") or file_name.endswith('.prefab'):
                file_name_with_subfolder = os.path.join(folder_name, file_name)
                # print(file_path + file_name_with_subfolder)

def generate_categories():
    """
    Generate the categories for the VFX.

    Returns:
        list: The categories.
    """
    subfolder_names = []
    folder_path = "assets"
    if os.path.isdir(folder_path):
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            if os.path.isdir(item_path):
                subfolder_names.append(item)
    
    return subfolder_names

def get_prefab_paths(categories):
    """
    Get the prefab paths for the categories.

    Args:
        categories (list): The categories.

    Returns:
        list: The prefab paths.
    """
    prefab_paths = []
    
    for category in categories:
        category_path = os.path.join("assets", category, "Prefabs")
        prefab_list = []
        
        if os.path.exists(category_path):
            for file_name in os.listdir(category_path):
                if file_name.endswith(".prefab"):
                    prefab_path = os.path.join("Prefabs", file_name)
                    prefab_list.append(prefab_path)
        
        prefab_paths.append(prefab_list)
    
    return prefab_paths




