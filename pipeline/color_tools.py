import math
import PIL
import extcolors
import numpy as np
import urllib.request
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
from matplotlib import gridspec
from tqdm import tqdm
from art_api import go_make_art_with_this
import random
import threading

def fetch_image(image_path):
  img = PIL.Image.open(image_path)
  return img

def extract_colors(img):
  tolerance = 32
  limit = 6
  colors, pixel_count = extcolors.extract_from_image(img, tolerance, limit)
  return colors

def render_color_palette(colors):
  size = 100
  columns = 6
  rows = math.ceil(len(colors) / columns)
  width = columns * size
  height = rows * size
  result = Image.new("RGBA", (width, height), (0, 0, 0, 0))
  canvas = ImageDraw.Draw(result)
  for idx, color in enumerate(colors):
      x = int((idx % columns) * size)
      y = int((idx // columns) * size)
      canvas.rectangle([(x, y), (x + size - 1, y + size - 1)], fill=color[0])
  return result

def overlay_palette(img, color_palette):
  fig, ax = plt.subplots(2, 1, figsize=(8, 10))

  # Render the first image
  ax[0].imshow(img)
  ax[0].axis('off')

  # Add the color palette below the first image
  ax[1].imshow(color_palette)
  ax[1].axis('off')

  # Adjust spacing between subplots
  plt.tight_layout()

  # Show the figure
  plt.show()

def study_image(image_path):
  img = fetch_image(image_path)
  colors = extract_colors(img)
  color_palette = render_color_palette(colors)
  overlay_palette(img, color_palette)
  return colors

def simplify_color_palette(color_lists):
  num_colors = len(color_lists[0])
  simplified_palette = []

  for i in range(num_colors):
      target_color = color_lists[0][i]  # First color in the first list
      min_distance = float('inf')
      closest_color = None

      for color_list in color_lists:
          current_color = color_list[i]  # Current color in the list

          # Calculate the Euclidean distance between target_color and current_color
          distance = sum((c1 - c2) ** 2 for c1, c2 in zip(target_color[0], current_color[0]))

          if distance < min_distance:
              min_distance = distance
              closest_color = current_color

      simplified_palette.append(closest_color)

  return simplified_palette

def get_brightest_colors(color_list):
    brightest_colors = []
    
    # Sort the colors based on brightness/vibrancy
    sorted_colors = sorted(color_list, key=lambda color: sum(color[0]))
    
    # Append the two brightest/most vibrant colors to the result list
    brightest_colors.append(sorted_colors[-1])
    brightest_colors.append(sorted_colors[-2])
    
    return brightest_colors

def get_images_from_stability(prompt):
    print("Requesting Images from stabiliy api...")
    #TODO: get images from stability api using prompt
    #save them in /images/$prompt1-4.png
    full_prompt = f"({prompt}), video game texture, vibrant color, solid color"
    #DPM 2M Karras, 30 steps, tiling, 512x512, batch size 4

    #return list of image paths
    print("Recieved, saving images...")
    return ["test2.png", "test3.png", "test4.png", "test5.png"]

def get_images_from_stability(prompt, current_iteration):
    text = f"({prompt}), video game texture, vibrant colors, solid color"
    
    # Create and start the threads
    t1 = go_make_art_with_this(text, f"images/midpoint{current_iteration}_1.png")
    t2 = go_make_art_with_this(text, f"images/midpoint{current_iteration}_2.png")
    t3 = go_make_art_with_this(text, f"images/midpoint{current_iteration}_3.png")
    t4 = go_make_art_with_this(text, f"images/midpoint{current_iteration}_4.png")
    images = [t1, t2, t3, t4]
    print("Done!")
    return images

def generate_color_palette(prompt, current_iteration):
    print("Getting Images...")
    image_list = get_images_from_stability(prompt, current_iteration)
    print("Analyzing Images...")

    image_list = [fetch_image(image) for image in image_list]
    colors_list = []
    for image in tqdm(image_list):
        colors = extract_colors(image)
        colors_list.append(colors)

    equalized_colors = simplify_color_palette(colors_list)
    # final_colors = get_brightest_colors(equalized_colors)
    final_colors = equalized_colors
    print("Final Colors: " + str(final_colors[0]) + " and " + str(final_colors[1]) + ".")
    return final_colors

def calculate_alpha(count, low, high):
    result = count / 262144 + random.uniform(low, high)
    return min(result, 1.0)

def get_rgba(color, low, high):
    rgb, alpha = color
    r, g, b = rgb
    r=r/255
    g=g/255
    b=b/255
    alpha = calculate_alpha(alpha, low, high)
    return (r, g, b, alpha)
