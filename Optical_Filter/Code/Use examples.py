#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#How to call optical filter function
#You might have to pay particular attention to file path directory, chnage it to your suitability

#path where input image stored
image_path = "/Users/apple/Desktop/2.jpg" 
#path where output image stored
output_path = "/Users/apple/Desktop/2con10.jpg"  

#changing parameters according to images that you are interested in
contrast_factor = 1.0  #1.0 being the original contrast level
vignette_strength = 1.0  #vignette strength (0.0 to 1.0)
#set distortion factor to be less than 1.0 to give pincushion distortion, and more than 1 to give barrel distortion
distortion_factor =  1.2 
flare_center = (100,150)  # set coordinate of center of the flare or glare effect
flare_radius = 100  # set radius of the flare or glare effect
flare_intensity = 2  # set intensity of the flare or glare effect
red_shift = 0 # number of pixels to shift for red 
blue_shift = 10  # number of pixels to shift for blue 


#example of calling function e.g. changing contrast of the image
change_contrast(image_path, output_path, contrast_factor)
change_vignetting(image_path, output_path, vignette_strength)
apply_barrel_distortion(image_path, output_path, distortion_factor)
apply_lens_flare_glare(image_path, output_path, flare_center, flare_radius, flare_intensity)
apply_chromatic_aberration(image_path, output_path, red_shift, blue_shift)

