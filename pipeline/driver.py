from color import generate_color_palette
from unity_gen import generate_base_unity_file_name, duplicate_unity_files, tweak_files
from get_filenames import generate_categories, get_prefab_paths

def generate_vfx(prompt):
    print("Recieved prompt:" + prompt)
    # Generate the color palette
    print("Generating color palette for prompt:" + prompt)
    color_palette = generate_color_palette(prompt)

    # Generate category names, and file names, save them to a txt file.
    categories = generate_categories()
    base_effect_names = get_prefab_paths(categories)
    print("Categories and file names generated:")
    print(categories[0])
    print(base_effect_names[0])

    print("Ending early for testing purposes.")
    return

    # Generate the base Unity file name
    print("Generating VFX starting point file name...")
    base_file_name = generate_base_unity_file_name(prompt)

    if base_file_name is None:
        print("Failed to generate base Unity file name.")
        return

    # Duplicate the Unity files
    duplicated_file_name = duplicate_unity_files(base_file_name)

    # Tweak the duplicated files
    tweak_files(color_palette, duplicated_file_name)

    print("VFX generation completed.")

generate_vfx("green fire")