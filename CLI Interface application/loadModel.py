import PIL
import math
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub

def load_Model(model_path):
    print("int model")
    model = tf.keras.models.load_model(model_path, custom_objects={'KerasLayer':hub.KerasLayer})
    #print(model.summary())
    return model