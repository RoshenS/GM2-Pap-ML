#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#imports

import numpy as np
import pandas as pd
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import time
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from matplotlib import colors
from matplotlib import cm, colors as mcolors
import seaborn as sns
sns.set_style('darkgrid')
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import tensorflow as tf
from tensorflow import keras
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Dense, Dropout,BatchNormalization
from keras.optimizers import Adamax
from keras import regularizers
from keras.models import Model
from PIL import Image


# In[ ]:

#you can change the model that you want to test by changing name of the model and respiratory.
#There are many options for you to choose your model from the main model file or image-compression file
#testing

#relative test paths
path = r'Data\\test\\pp.jpg'

#read the image
img = tf.io.read_file(path)
dec_img = tf.image.decode_jpeg(img, channels=3)

#changing the image type to tensorflow
tensor = tf.convert_to_tensor(dec_img)
test = tf.expand_dims(tensor, axis=0)

#model list
#name the model according to the model that you download and want to use
model_loc = 'Models\\Q=100_99.27'
model = keras.models.load_model(model_loc)

#the output is the confident level, assign the right class to the class with highest confident level
class_list = ["Normal","Papilledema","Psuedopap"]

#prediction
pred=model(test)

#display the class with highest confident level
print(class_list[np.argmax(pred)])

