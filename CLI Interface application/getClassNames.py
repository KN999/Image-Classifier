import json

def get_class_names(json_file):
    print("classname")
    with open(json_file, 'r') as f:
        file = json.load(f)
        
    class_names = dict()
    
    for index in file:
        class_names[str(int(index)-1)] = file[index]
    return class_names