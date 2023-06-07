#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#barrel distortion function:

import cv2
import numpy as np

#set distortion factor to be less than 1.0 to give pincushion distortion, and more than 1 to give barrel distortion
distortion_factor =  1.2 


def apply_barrel_distortion(image_path, output_path, distortion_factor):
    # Read the image
    image = cv2.imread(image_path)

    # Get the dimensions of the image
    height, width = image.shape[:2]

    # Set the center of the image
    center_x = width / 2
    center_y = height / 2

    # Create a new image with the same size and type as the original image
    distorted_image = np.zeros_like(image)

    # Apply distortion
    for y in range(height):
        for x in range(width):
            # Calculate the normalized coordinates
            nx = (x - center_x) / center_x
            ny = (y - center_y) / center_y

            # Calculate the radial distance
            r = np.sqrt(nx**2 + ny**2)

            # Apply distortion
            distorted_r = r * distortion_factor

            # Calculate the new coordinates
            new_x = int(center_x + nx * distorted_r * center_x)
            new_y = int(center_y + ny * distorted_r * center_y)

            # Copy the pixel to the new location
            if 0 <= new_x < width and 0 <= new_y < height:
                distorted_image[new_y, new_x] = image[y, x]

    # Save image
    cv2.imwrite(output_path, distorted_image)

