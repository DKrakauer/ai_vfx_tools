import os
import openai
from dotenv import load_dotenv

def get_vfx_category(prompt, categories):
    print("Getting VFX category for prompt: " + prompt)

    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")

    prompt_string = "I am trying to create some visual effects for " + prompt + ". I have access to a bunch of starter/basic effects which I want to use to save me some time. I plan on changing the color, so all that matters is the shape of the effect. The categories of effects include: " + str(categories) + ". Which category fits what I am looking for best? Please only respond with the exact category name provided."

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt_string,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    text_response = response['choices'][0]['text'].strip()

    if text_response in categories:
        return text_response
    else:
        print(f"Critical Error! GPT Response gave an invalid category:  \n{prompt_string}\n{response}\n")
        return None

def prune_strings(string_list):
    pruned_list = []
    for string in string_list:
        pruned_string = string.replace("Prefabs/", "").replace(".prefab", "")
        pruned_list.append(pruned_string)
    return pruned_list

def choose_vfx_effect(effect_names, prompt, category):
    print("Choosing VFX effect for prompt: " + prompt)

    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")

    actual_effect_names = prune_strings(effect_names)
    prompt_string = "I am trying to create some visual effects for " + prompt + ". I have access to a bunch of " + category + " effects which I want to use to save me some time. I plan on changing the color, so all that matters is the shape of the effect. The only effects I have access to are: " + str(actual_effect_names) + ". Which effect fits what I am looking for best? Please only respond with the exact name of the effect."
    
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt_string,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    text_response = response['choices'][0]['text'].strip()

    if text_response in actual_effect_names:
        index = actual_effect_names.index(text_response)
        return effect_names[index]
    else:
        print(f"Critical Error! GPT Response gave an invalid effect!: \n{prompt_string}\n{response}\n")
        return None

def get_vfx_file_name(category_index, category, prompt, base_effect_names):
    print("Figuring out base file name for category: " + category)
    base_path = "assets"
    category_path = f"{base_path}/{category}"
    
    effect_name = choose_vfx_effect(base_effect_names[category_index], prompt, category)
    
    if effect_name == None:
        return None
    
    file_path = f"{category_path}/{effect_name}"
    return file_path

def find_index(string_list, target_string):
    try:
        index = string_list.index(target_string)
        return index
    except ValueError:
        return -1  # Return -1 if the target string is not found in the list



def generate_base_unity_file_name(prompt, categories, base_effect_names):
    """
    Generate the base file name for Unity files.

    Returns:
        str: The base file name.
    """
    category = get_vfx_category(prompt, categories)

    category_index = find_index(categories, category)

    file_path = get_vfx_file_name(category_index, category, prompt, base_effect_names)

    return file_path

def duplicate_unity_files(base_file_name):
    """
    Duplicate the Unity files.

    Args:
        base_file_name (str): The base file name for the Unity files.

    Returns:
        str: The duplicated file name.
    """
    # TODO: Implement Unity file duplication logic
    duplicated_file_name = base_file_name + '_duplicate'  # Example duplicated file name
    return duplicated_file_name

def tweak_files(color_palette, duplicated_file_name):
    """
    Tweak the duplicated files.

    Args:
        color_palette (ColorPalette): The color palette for VFX.
        duplicated_file_name (str): The duplicated file name.
    """
    # TODO: Implement file tweaking logic
    print("Tweaking files with color palette:", color_palette.colors)
    print("Using duplicated file:", duplicated_file_name)