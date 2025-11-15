
import json
import os
import re

pjoin = os.path.join
abspath = os.path.abspath

def load_json(filename):
    """
    Load a json configuration
    """
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
        src_path = data["InFilePath"]
        out_path = data["OutFilePath"]
        file_names = data["FileList"]
    return src_path, out_path, file_names

def text_oneliner(src_path, out_path, file_names):
    """
    Load text files and convert them as a single lined text file
    """
    for file_name in file_names:
        file_path = pjoin(src_path, file_name)
        with open(file_path, 'r', encoding='utf-8') as text_file:
            lines = text_file.read()
        cleaned_line = re.sub(r'\n+', ' ', lines) # switch '\n' to a space
        cleaned_line = re.sub(r'\s+', ' ', cleaned_line) # switch multiple spaces to a space
        print("Loaded from", abspath(file_path), len(cleaned_line), "characters")
        if not os.path.exists(out_path):
            os.makedirs(out_path)
        with open(pjoin(out_path, file_name), 'w', encoding='utf-8') as text_file:
            text_file.write(cleaned_line)
            print("Saved as a ", abspath(pjoin(out_path, file_name)))

if __name__ == "__main__":
    src_path, out_path, file_names = load_json("./data.json")
    text_oneliner(src_path, out_path, file_names)
