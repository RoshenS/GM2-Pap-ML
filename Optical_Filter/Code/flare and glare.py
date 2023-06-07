#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# changing lens flare and glare

import cv2
import numpy as np

flare_center = (100,150)  # Set coordinate of center of the flare or glare effect
flare_radius = 100  # set radius of the flare or glare effect
flare_intensity = 2  # set intensity of the flare or glare effect

def apply_lens_flare_glare(image_path, output_path, flare_center, flare_radius, flare_intensity):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to float32 for calculations
    image = image.astype(np.float32) / 255.0

    # Create an empty canvas with the same size as the image
    canvas = np.zeros_like(image)

    # Generate random noise
    noise = np.random.randn(*image.shape) * 0.1

    # Add lens flare and glare
    flare_mask = np.zeros_like(image)
    cv2.circle(flare_mask, flare_center, flare_radius, (1, 1, 1), -1)
    flare = np.exp(-(1 - flare_mask) * flare_intensity)
    canvas = image + noise + flare

    # Normalize the values to the range [0, 1]
    canvas = np.clip(canvas, 0, 1)

    # Convert the image back to uint8 format
    canvas = (canvas * 255).astype(np.uint8)

    # Save image
    cv2.imwrite(output_path, canvas)

