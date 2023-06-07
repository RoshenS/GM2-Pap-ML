#!/usr/bin/env python
# coding: utf-8

# In[1]:


#function to change contrast of the image
#playing around with setting contrast_factor with 1.0 being orignial contrast level

#import PIL python library
from PIL import Image, ImageEnhance

def change_contrast(image_path, output_path, contrast_factor):
    # import image and open it, get it ready for filtering
    image = Image.open(image_path)
    # change the image contrast
    enhancer = ImageEnhance.Contrast(image)
    enhanced_image = enhancer.enhance(contrast_factor)
    # Save the modified image
    enhanced_image.save(output_path)

