from color import generate_color_palette
from unity_gen import generate_base_unity_file_name, duplicate_unity_files, tweak_files
from get_filenames import generate_categories, get_prefab_paths

def generate_vfx(prompt):
    print("Recieved VFX command for prompt: " + prompt)
    print(" ")

    # Generate category names, and file names, save them to a txt file.
    # categories = generate_categories()
    # base_effect_names = get_prefab_paths(categories)
    # print("Categories recognized in local files: ")
    # print(categories)
    # print(" ")

    # # Generate the base Unity file name
    # print("Generating VFX starting point file name...")
    # base_file_name = generate_base_unity_file_name(prompt, categories, base_effect_names)

    # if base_file_name is None:
    #     print("Failed to generate base Unity file name.")
    #     return
    # else:
    #     print("File path generated: " + base_file_name + "\n")
    
    # TODO: remove this line
    base_file_name = "assets/Magic Effects/Prefabs/IceLance.prefab"
    

    # Duplicate the Unity files
    # TODO: implement copying files to ouput folder, keep bulk generation in mind
    duplicated_file_name = duplicate_unity_files(base_file_name)

    print("\nEnding early for testing purposes. ")
    return

    # Generate the color palette
    print("Generating color palette for prompt: " + prompt)
    color_palette = generate_color_palette(prompt)
    print("Color palette generated: ")

    # Tweak the duplicated files
    tweak_files(color_palette, duplicated_file_name)

    print("VFX generation completed.")

# generate_vfx("green fire")