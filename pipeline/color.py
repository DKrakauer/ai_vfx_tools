import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def get_dominant_colors(image, n_colors):
    # make sure image was loaded properly
    if image is None:
        print("Failed to load image.")
    else:
        print("Image loaded successfully.")

    # Reshape the image to be a list of pixels
    pixels = image.reshape(-1, 3)

    # Perform K-means clustering to find the most dominant colors
    kmeans = KMeans(n_clusters=n_colors)
    kmeans.fit(pixels)

    # Get the RGB values of the cluster centers
    colors = kmeans.cluster_centers_

    # Convert each color to integer values
    colors = colors.round(0).astype(int)

def plot_colors(colors):
    # Create a new image with each color
    color_palette = np.zeros((50, 50 * len(colors), 3), dtype=np.uint8)

    # For each color in the color palette
    for i, color in enumerate(colors):
        # Fill the corresponding section with the color
        color_palette[:, i*50:(i+1)*50, :] = color

    # Display the color palette
    plt.figure(figsize=(len(colors), 1))
    plt.imshow(color_palette)
    plt.axis('off')
    plt.show()

# Read the image
import os
print(os.getcwd())
image = cv2.imread('c:\\Users\shado\Desktop\Projects\\aivfx\pipeline\\test1.jpg')

# Convert BGR image to RGB
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Get the dominant colors
colors = get_dominant_colors(image, 5)  # Adjust the second parameter as needed

# Plot the dominant colors
plot_colors(colors)

# def synthesize_color_palette(color_palettes):
#     for each 