import os
import random
from color_tools import get_rgba

def duplicate_unity_files(prompt, base_file_name):
    """
    Duplicate the Unity files.

    Args:
        prompt (str): The prompt for VFX.
        base_file_name (str): The base file name for the Unity files.

    Returns:
        str: The duplicated file name.
    """
    # Preprocess the name
    name = prompt.replace(" ", "").replace(",", "")

    # Get the extension from file_path
    _, extension = os.path.splitext(base_file_name)

    # Generate the new file name
    new_file_name = ""
    if extension != ".mat.meta":
        new_file_name = f"{name}{extension}"
    else:
        new_file_name = f"{name}.mat"

    # Generate the new file path
    output_path = os.path.join("output", new_file_name)

    # Duplicate the file
    with open(base_file_name, "rb") as original_file:
        with open(output_path, "wb") as duplicate_file:
            duplicate_file.write(original_file.read())

    print("Created new output file: " + output_path)
    return output_path

def update_colors(file_path, main_color, second_color):
    count = 0
    total = 0
    with open(file_path, 'r+') as file:
        lines = file.readlines()
        total = len(lines)
        for i in range(total):
            if lines[i].strip() == 'startColor:':
                # Find the maxColor line
                for j in range(i+1, i+5):
                    if 'maxColor' in lines[j]:
                        # Generate random color choice
                        if random.random() < 0.7:
                            color_choice = main_color
                        else:
                            color_choice = second_color
                        
                        # Update the maxColor line
                        updated_line = f"      maxColor: {{r: {color_choice[0]}, g: {color_choice[1]}, b: {color_choice[2]}, a: {color_choice[3]}}}\n"
                        lines[j] = updated_line
                        count += 1
                        # print("Max color line:\n " + lines[j])
                        # print("Updated max color line:\n " + updated_line)
                        break
        
        file.seek(0)
        file.writelines(lines)
        file.truncate()
    return count, total

def tweak_files(color_palette, duplicated_file_name):
    """
    Tweak the duplicated files.

    Args:
        color_palette (ColorPalette): The color palette for VFX.
        duplicated_file_name (str): The duplicated file name.
    """
    print("Reworking new effect files... ")
    primary_color = get_rgba(color_palette[0], 0.8, 0.9)
    secondary_color = get_rgba(color_palette[1], 0.7, 0.8)
    count, total = update_colors(duplicated_file_name, primary_color, secondary_color)
    print("Changed " + str(count) + " out of " + str(total) + " colors.\n")
    return duplicated_file_name