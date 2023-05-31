import os
import openai
from dotenv import load_dotenv

def get_vfx_category(prompt):
    print("Getting VFX category for prompt:" + prompt)
    load_dotenv()

    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="I am trying to create some visual effects for " + prompt + ". I have access to a bunch of starter/basic effects which I want to use to save me some time. The categories of effects include: Fire, Explosion, Goop, Magic, Smoke, Steam, Water, Weapon, and Variety. Which category fits what I am looking for best? Please only respond with the exact category name provided.",
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    text_response = response['choices'][0]['text'].strip()
    words = text_response.split()

    if len(words) == 1:
        return words[0]
    else:
        print(f"Critical Error! GPT Response contains multiple words: {response}")
        return None
    
def get_vfx_file_name(category, prompt):
    print("Finding file name for category, prompt: " + category)
    return category

def generate_base_unity_file_name(prompt):
    """
    Generate the base file name for Unity files.

    Returns:
        str: The base file name.
    """
    
    category = get_vfx_category(prompt)

    return get_vfx_file_name(category, prompt)

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