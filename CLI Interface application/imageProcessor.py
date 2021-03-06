import PIL
import math
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub

IMG_SIZE = 224

def image_Processor(image_path):
    print("image")
    img = np.asarray(PIL.Image.open(image_path))
    processed_img = img / 255
    #img = tf.cast(img, tf.float32)
    img = tf.image.resize(img, (IMG_SIZE, IMG_SIZE)).numpy()
    
    return img