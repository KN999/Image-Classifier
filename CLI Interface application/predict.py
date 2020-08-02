import argparse
import json
from getClassNames import get_class_names
from getPrediction import get_Prediction

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description = "predict the top flower names from an image along with their corresponding probabilities")
    parser.add_argument("path_to_image",
                        help = "Image's path relative to script")
    parser.add_argument("path_to_model",
                        help = "Model's path relative to script")
    parser.add_argument("--top_k", help="Number of top probabality that needs to be fetched",
                        required = False)
    parser.add_argument("--category_names",
                        help = "Json file to map class with flower name",
                        required = False)
    
    image_path = parser.parse_args().path_to_image
    model_path = parser.parse_args().path_to_model
    top_k = parser.parse_args().top_k
    category_names = parser.parse_args().category_names
    
    if category_names == None:
        category_names = "./label_map.json"
    if top_k == None:
        top_k = 3
        
    class_names = get_class_names(category_names)
    
    get_Prediction(image_path, model_path, top_k, class_names)
    