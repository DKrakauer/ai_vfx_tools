from get_filenames import generate_categories, get_prefab_paths
from effect_search import generate_base_unity_file_name
from color_tools import generate_color_palette
from unity_gen import duplicate_unity_files, tweak_files
from material_gen import generate_material_files

def generate_vfx(prompt, current_iteration):
    print("Recieved VFX command for prompt: " + prompt)
    print(" ")

    # Generate category names, and file names, save them to a txt file.
    categories = generate_categories()
    base_effect_names = get_prefab_paths(categories)
    print("Categories recognized in local files: ")
    print(categories)
    print(" ")

    # Generate the base Unity file name
    print("Generating VFX starting point file name...")
    base_file_name = generate_base_unity_file_name(prompt, categories, base_effect_names)

    if base_file_name is None:
        print("Failed to generate base Unity file name.")
        return
    else:
        print("File path generated: " + base_file_name + "\n")

    # Duplicate the Unity files
    duplicated_file_path = duplicate_unity_files(prompt, base_file_name)

    # Generate the color palette
    print("Generating color palette for prompt: " + prompt)
    color_palette = generate_color_palette(prompt, current_iteration)

    # Tweak the duplicated files
    duplicated_file_path = tweak_files(color_palette, duplicated_file_path)

    generate_material_files(color_palette, duplicated_file_path, categories)
    print("VFX generation completed.")

# generate_vfx("green fire")