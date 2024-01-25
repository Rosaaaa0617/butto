from ansa import base
from .pre import segments

def save(output_ansa_file):
    print("Saving file:", output_ansa_file)
    base.OutputLSDyna(filename=output_ansa_file, mode = "all")   
    
