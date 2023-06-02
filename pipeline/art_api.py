import json
import base64
import requests
import io
from PIL import Image, PngImagePlugin

# Easy function to throw a prompt into to make the bot code easier to read
def go_make_art_with_this(prompt: str, output_path: str):
    url = "http://127.0.0.1:7860"
    payload = {
        "prompt": prompt,
        "steps": 30,
        "width": 512,
        "height": 512,
        "tiling": True,
        "sampler_name": "DPM++ 2M Karras",

    }

    response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)

    r = response.json()

    # print(r)

    for i in r['images']:
        if len(r['images']) > 1:
            print("More than one image returned, using the first one.")
        
        image = Image.open(io.BytesIO(base64.b64decode(i.split(",",1)[0])))

        png_payload = {
            "image": "data:image/png;base64," + i
        }
        response2 = requests.post(url=f'{url}/sdapi/v1/png-info', json=png_payload)

        pnginfo = PngImagePlugin.PngInfo()
        pnginfo.add_text("parameters", response2.json().get("info"))
        image.save(output_path, pnginfo=pnginfo)
        print("Image saved to " + output_path)
        return output_path
    
    print("No images returned, something went wrong. Returning white image.")
    img = Image.new('RGB', (60, 30), color = (73, 109, 137))
    return img

# go_make_art_with_this("Dark ranger hunter with long flowing blonde hair, purple black armor, no helmet, large bow, wolf pet companion, and a quiver of arrows on her back.", "test.png")