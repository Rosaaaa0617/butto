import ansa, os, random,sys
from ansa import base, constants, session

current_dir_path = os.path.dirname(__file__)
sys.path.append(os.path.dirname(current_dir_path))

from mid import save

# 2d crush: merge control key file
def Merge_2dcrush(asset_file_dir, output_dir, mode, input_name, output_name):
    session.New("discard")
    base.InputLSDyna(filename=os.path.join(asset_file_dir,f"{mode}Control.key"), version="R11",header="merge",create_parameters="on")
    base.InputLSDyna(filename=os.path.join(asset_file_dir,"mat.key"), version="R11",header="merge",create_parameters="on")
    base.InputLSDyna(filename=os.path.join(output_dir,input_name), sets_id="keep-old", version="R11",header="merge",create_parameters="on")
    SetValue()
    base.InputLSDyna(filename=os.path.join(asset_file_dir,"beam8r.k"), version="R11",header="merge",create_parameters="on")
    model_file = os.path.join(output_dir,output_name)
    save(model_file)
    return model_file
    
    

# 3pb: merge control key file
def Merge_fix(asset_file_dir, output_dir, mode, input_name, output_name):
    session.New("discard")
    base.InputLSDyna(filename=os.path.join(output_dir,input_name), sets_id="keep-new",header="merge",create_parameters="on")
    base.InputLSDyna(filename=os.path.join(asset_file_dir,f"{mode}Control.key"),header="merge",create_parameters="on")


    model_file = os.path.join(output_dir,output_name)
    save(model_file)



# 2d crush values
def SetValue():
    deck = constants.LSDYNA    
    # Random Material
    my_list = {1,2}
    for ent in base.CollectEntitiesI(constants.LSDYNA, None, 'SECTION_SHELL'):
        random_element = random.choice(list(my_list))
        ent.set_entity_values(deck,{'MID':random_element})
        ent.set_entity_values(deck,{'T1':50})
        ent.set_entity_values(deck,{'NIP':4})
        ent.set_entity_values(deck,{'ELFORM':15})

# bar values
def SetIsoValue():
    deck = constants.LSDYNA    
    # Random Material
    for ent in base.CollectEntitiesI(constants.LSDYNA, None, 'SECTION_SHELL'):
        ent.set_entity_values(deck,{'MID':2})
        ent.set_entity_values(deck,{'T1':3})
        ent.set_entity_values(deck,{'NIP':3})
        # ent.set_entity_values(deck,{'HGID':1})

# fixed values
def SetFixValue():
    deck = constants.LSDYNA    
    for ent in base.CollectEntitiesI(constants.LSDYNA, None, 'SECTION_SHELL'):
        ent.set_entity_values(deck,{'T1':1})
        ent.set_entity_values(deck,{'NIP':2})
        if ent._id <=2:
            ent.set_entity_values(deck,{'MID':82})
        else:
            ent.set_entity_values(deck,{'MID':55})
 
        
            
if __name__ == "__main__":
    asset_file_dir=r"E:\#code\butto\data"    
    output_dir=r"E:\#code\butto\data\output"
    # Merge_fix(asset_file_dir, output_dir, "3pb", "model.key", "3pb.key")
    Merge_2dcrush(asset_file_dir, output_dir, "2dcrush", "model.key", "total.key")