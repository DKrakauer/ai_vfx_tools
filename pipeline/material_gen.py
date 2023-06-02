from color_tools import get_rgba
from unity_gen import duplicate_unity_files
from get_filenames import get_meta_material_paths

def find_guids(file_path):
    guids = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for i in range(len(lines)):
            if lines[i].strip() == 'm_Materials:':
                next_line = lines[i + 1].strip()
                if next_line.startswith('- {') and 'guid' in next_line:
                    guid_start = next_line.index('guid:') + 6
                    guid_end = next_line.index(',', guid_start)
                    guid = next_line[guid_start:guid_end].strip()
                    guids.append(guid)
    return guids

def find_matching_file_paths(guids, meta_guids):

    printable_guids = ", ".join(guids)
    print(f"\nSearching for the following material guids: {printable_guids}")
    matching_file_paths = []
    
    for category in range(len(meta_guids)):
        for meta_guid_path in meta_guids[category]:
            with open(meta_guid_path, 'r') as file:
                lines = file.readlines()
                if len(lines) >= 2:
                    guid_from_file = lines[1].strip().split(':')[1].strip()
                    if guid_from_file in guids:
                        matching_file_paths.append(meta_guid_path)
    
    return matching_file_paths

def find_materials(file_path, categories):
    guids = find_guids(file_path)
    meta_guids = get_meta_material_paths(categories)
    material_paths = find_matching_file_paths(guids, meta_guids)
    return material_paths

def extract_file_name(path):
    # Split the path using the '\\' separator
    parts = path.split('\\')

    # Extract the last part of the split path
    file_name = parts[-1]

    # Remove the extension and return the file name
    return file_name.split('.')[0]

def remove_meta_suffix(strings):
    modified_strings = []
    for string in strings:
        if string.endswith(".meta"):
            modified_string = string[:-5]  # Remove the last 5 characters (.meta)
            modified_strings.append(modified_string)
        else:
            modified_strings.append(string)
    return modified_strings

def update_material_colors(primary_color, secondary_color, file_path):
    print(f"Updating material colors for file: {file_path}")
    with open(file_path, 'r+') as file:
        lines = file.readlines()

        for i in range(len(lines)):
            if lines[i].strip() == "m_Colors:":
                for j in range(i+1, min(i+10, len(lines))):
                    # print(lines[j].strip())
                    if lines[j].strip().startswith("- _Color:"):
                        # print("Found color line: " + lines[j])
                        updated_color_line = f"    - _Color: {{r: {primary_color[0]}, g: {primary_color[1]}, b: {primary_color[2]}, a: {primary_color[3]}}}\n"
                        lines[j] = updated_color_line
                    if lines[j].strip().startswith("- _EmissionColor:"):
                        # print("Found color line: " + lines[j])
                        if lines[j].strip().startswith("- _EmissionColor: {r: 0, g: 0, b:0"):
                            break
                        else:
                            updated_color_line = f"    - _EmissionColor: {{r: {secondary_color[0]}, g: {secondary_color[1]}, b: {secondary_color[2]}, a: {secondary_color[3]}}}\n"
                            lines[j] = updated_color_line
                            break

        file.seek(0)
        file.writelines(lines)
        file.truncate()

def generate_material_files(color_palette, file_path, categories):
    """
    Generate the material file for the VFX.

    Args:
        color_palette (ColorPalette): The color palette for VFX.
        file_path (str): The file path of the duplicated Unity file.
    """

    material_paths = find_materials(file_path, categories)
    print("Ending paths for materials found: " + str(material_paths))

    output_paths = []
    mat_paths = remove_meta_suffix(material_paths)
    for path in mat_paths:
        name = extract_file_name(path)
        output_paths.append(duplicate_unity_files(name, path))
    
    # print("Generated output files for materials: " + str(output_paths))
    print(" ")
    primary_color = get_rgba(color_palette[0], 0.8, 0.9)
    secondary_color = get_rgba(color_palette[1], 0.7, 0.8)

    for path in output_paths:
        update_material_colors(primary_color, secondary_color, path)
    
    return