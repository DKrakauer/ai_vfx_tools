from color import generate_color_palette
from unity_gen import generate_base_unity_file_name, duplicate_unity_files, tweak_files

def generate_vfx(prompt):
    print("Recieved prompt:" + prompt)
    # Generate the color palette
    print("Generating color palette for prompt:" + prompt)
    color_palette = generate_color_palette(prompt)

    # Generate the base Unity file name
    print("Generating VFX starting point file name...")
    base_file_name = generate_base_unity_file_name(prompt)

    if base_file_name is None:
        print("Failed to generate base Unity file name.")
        return

    print("Ending early for testing purposes.")
    return

    # Duplicate the Unity files
    duplicated_file_name = duplicate_unity_files(base_file_name)

    # Tweak the duplicated files
    tweak_files(color_palette, duplicated_file_name)

    print("VFX generation completed.")

generate_vfx("green fire")