import ansa, os
from ansa import *

def main(file_path):
    base.InputLSDyna(filename=file_path, header="merge", create_parameters="on")
    deck = constants.LSDYNA    
    for ent in base.CollectEntitiesI(constants.LSDYNA, None, 'SECTION_SHELL'):
        ent.set_entity_values(deck,{'MID':1})
        ent.set_entity_values(deck,{'T1':3})
        ent.set_entity_values(deck,{'NIP':3})
        ent.set_entity_values(deck,{'HGID':1})


def _SaveANSAFile():
    directory = os.getcwd()
    file_name = "total.key"
    output_ansa_file = os.path.join(directory, file_name)
    print("Saving file:", output_ansa_file)
    base.OutputLSDyna(filename=output_ansa_file, mode = "all", disregard_includes="on")




file_path = r"Z:\butto\asset\cantileverControl.key"
main(file_path)
_SaveANSAFile()

