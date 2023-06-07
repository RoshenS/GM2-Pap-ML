#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#changing vignetting effect

from PIL import Image, ImageDraw

vignette_strength = 1.0  #vignette strength (0.0 to 1.0)

def change_vignetting(input_path, output_path, vignette_strength):
    # import image
    image = Image.open(image_path)

    # Create a new image with the same size and mode as the original image
    vignette = Image.new('RGBA', image.size)

    # Create a radial gradient mask
    mask = Image.new('L', image.size, 0)
    draw = ImageDraw.Draw(mask)
    width, height = image.size
    radius = (width / 2, height / 2)
    max_distance = max(radius)
    for y in range(height):
        for x in range(width):
            distance = ((x - radius[0]) ** 2 + (y - radius[1]) ** 2) ** 0.5
            intensity = int(255 * (1 - distance / max_distance * vignette_strength))
            draw.point((x, y), fill=intensity)

    # Apply the vignette mask to the image
    image_with_vignette = Image.composite(image, vignette, mask)

    # Save image
    image_with_vignette.save(output_path, 'PNG')    

    

