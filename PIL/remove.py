# remove the most prevalent, common colour of the image with a range of tolerence.

from PIL import Image
from collections import defaultdict
import math

def get_most_common_color(img):
    """Return the most prevalent color in the image."""
    data = img.getdata()
    color_freq = defaultdict(int)
    
    for color in data:
        color_freq[color] += 1
        
    most_common_color = max(color_freq, key=color_freq.get)
    return most_common_color

def color_distance(color1, color2):
    """Return the Euclidean distance between two RGB colors."""
    r_diff = color1[0] - color2[0]
    g_diff = color1[1] - color2[1]
    b_diff = color1[2] - color2[2]
    
    return math.sqrt(r_diff**2 + g_diff**2 + b_diff**2)

def is_similar(color1, color2, tolerance=50):
    """Return True if two RGB colors are similar within a tolerance."""
    return color_distance(color1, color2) < tolerance

def remove_background(img_path, output_path, tolerance=50):
    """Remove the most prevalent color and its similar colors from the image."""
    
    # Open the image and convert it to RGBA to ensure it has an alpha channel
    img = Image.open(img_path).convert("RGBA")
    
    # Identify the most common color
    most_common_color = get_most_common_color(img)

    # Generate a new image with the prevalent color removed
    data = img.getdata()
    new_data = []

    for item in data:
        # Check if the item is similar to the most common color
        if is_similar(item[0:3], most_common_color[0:3], tolerance):
            # If matched, make it transparent
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)
            
    img.putdata(new_data)
    img.save(output_path, "PNG")

if __name__ == "__main__":
    remove_background("input.png", "output_image.png", tolerance=50)
