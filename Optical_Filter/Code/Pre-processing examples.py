#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#combine constrast and vignet:

import cv2
import numpy as np
from PIL import Image, ImageEnhance

def apply_image_effects2(image_path, output_path, contrast_factor, vignette_strength):
    # Read the image
    image = cv2.imread(image_path)

    # Adjust contrast
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB
    pil_image = Image.fromarray(image)  # Convert to PIL Image
    enhancer = ImageEnhance.Contrast(pil_image)
    enhanced_image = enhancer.enhance(contrast_factor)
    enhanced_image = np.array(enhanced_image)  # Convert back to numpy array
    enhanced_image = cv2.cvtColor(enhanced_image, cv2.COLOR_RGB2BGR)  # Convert to BGR

    #adjust vignetting
    height, width = enhanced_image.shape[:2]
    center_x = width // 2
    center_y = height // 2

    # Create a meshgrid of coordinates
    x, y = np.meshgrid(np.arange(width), np.arange(height))
    x_distance = x - center_x
    y_distance = y - center_y

    # Calculate the distance from the center for each pixel
    distance = np.sqrt(x_distance**2 + y_distance**2)

    # Calculate the vignette mask
    max_distance = np.sqrt(center_x**2 + center_y**2)
    vignette_mask = 1 - (distance / max_distance) ** vignette_strength
    vignette_mask = np.clip(vignette_mask, 0, 1)

    # Apply the vignette effect
    result = cv2.merge([enhanced_image[:,:,c] * vignette_mask for c in range(3)])

    # Save the modified image
    cv2.imwrite(output_path, result)

#set input and output image path   
image_path = "/Users/apple/Desktop/3.jpg"  
output_path = "/Users/apple/Desktop/3con0.5,vig1.5.jpg"  
contrast_factor = 0.5  # Adjust the contrast factor (1.0 means no change)
vignette_strength = 1.5  # Adjust the vignette strength (0.0 to 1.0)

#call function
apply_image_effects2(image_path, output_path, contrast_factor, vignette_strength)


# In[ ]:


#combine distortion+glare+chromatic effect in an optical filter

import cv2
import numpy as np


def apply_image_effects3(image_path, output_path, distortion_factor, glare_center, glare_radius, glare_intensity,
                        red_shift, blue_shift):
    # Read the image
    image = cv2.imread(image_path)

    if image is None:
        print(f"Failed to load the image at {image_path}")
        return

    # Apply lens distortion
    height, width = image.shape[:2]
    distorted_image = np.zeros_like(image)
    for y in range(height):
        for x in range(width):
            # Calculate the distance from the center
            distance = np.sqrt((x - glare_center[0]) ** 2 + (y - glare_center[1]) ** 2)

            # Calculate the distortion factor based on the distance
            distortion = 1 + distortion_factor * distance

            # Calculate the new coordinates
            new_x = int((x - glare_center[0]) * distortion + glare_center[0])
            new_y = int((y - glare_center[1]) * distortion + glare_center[1])

            if 0 <= new_x < width and 0 <= new_y < height:
                distorted_image[y, x] = image[new_y, new_x]

    # Apply glare effect
    mask = np.zeros((height, width), np.uint8)
    cv2.circle(mask, glare_center, glare_radius, (255), -1)
    glare = np.exp(-(1 - mask) * glare_intensity)
    glare_image = cv2.merge([glare, glare, glare]) * 255
    glare_image = glare_image.astype(np.uint8)

    # Apply chromatic aberration
    shifted_image = np.zeros_like(distorted_image)
    shifted_image[:, :blue_shift] = distorted_image[:, :blue_shift]
    shifted_image[:, -red_shift:] = distorted_image[:, -red_shift:]

    # Combine the distorted image with glare and chromatic aberration
    final_image = cv2.addWeighted(distorted_image, 1.0, glare_image, 0.5, 0)
    final_image = cv2.add(final_image, shifted_image)

    # Save the modified image
    cv2.imwrite(output_path, final_image)

#set input and output image path   
image_path = "/Users/apple/Desktop/3.jpg"  
output_path = "/Users/apple/Desktop/3dis0.005glare10050,radius10,intensity1.0,r1, b3.jpeg"  
distortion_factor = 0.005  # distortion factor for lens distortion
glare_center = (100, 50)  # center of the glare effect
glare_radius = 10  # radius of the glare effect
glare_intensity = 1.0  # intensity of the glare effect
red_shift = 1  # number of pixels to shift red 
blue_shift = 3  # number of pixels to shift blue 

apply_image_effects3(image_path, output_path, distortion_factor, glare_center, glare_radius, glare_intensity,
                    red_shift, blue_shift)

