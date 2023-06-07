#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#varry image chromatic abberation

import cv2
import numpy as np

red_shift = 0 # number of pixels to shift for red
blue_shift = 10  # number of pixels to shift for blue


def apply_chromatic_aberration(image_path, output_path, red_shift, blue_shift):
    # Read the image
    image = cv2.imread(image_path)

    # Split the image into color channels
    blue, green, red = cv2.split(image)

    # Create a canvas for the shifted channels
    shifted_blue = np.zeros_like(blue)
    shifted_red = np.zeros_like(red)

    # Shift the blue
    shifted_blue[:, :blue_shift] = blue[:, :blue_shift]

    # Shift the red
    shifted_red[:, -red_shift:] = red[:, -red_shift:]

    # Merge and combine the shifted back into the image
    shifted_image = cv2.merge((shifted_blue, green, shifted_red))

    # Save the modified image
    cv2.imwrite(output_path, shifted_image)

