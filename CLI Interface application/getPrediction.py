import PIL
import math
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import imageProcessor
from loadModel import load_Model
from imageProcessor import image_Processor

def get_Prediction(image_path, model_path, top_k, class_names):
    print("predict")
    top_k = int(top_k)
    model = load_Model(model_path)
    processed_image = image_Processor(image_path)
    #print(model.summary())
    
    probs = model.predict(np.expand_dims(processed_image, axis=0))
    probs_list = probs[0].tolist()
    #print(probs_list)
    
    topkindex = sorted(range(len(probs_list)), key=lambda i: probs_list[i])[-top_k:]
    
    print("Probability of the flower is : ")
    
    for index in topkindex:
        print(class_names[str(index)], end=" : ")
        print(probs_list[index])
    
    return True