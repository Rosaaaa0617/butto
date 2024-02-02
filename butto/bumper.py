import os,sys,ansa
from ansa import session,base,constants

# butto\butto
current_dir_path = os.path.dirname(__file__)
sys.path.append(current_dir_path)

from mid import morph, mesh, include
from mid.utils import LsDyna
from post import repeat
   

def dbg_mode(dbg_path):
    # \butto\data
    asset_file_dir = os.path.join(os.path.dirname(current_dir_path), "data")

    if dbg_path:
        # test file path
        input_dir = r"data\input\multi"
        output_dir = r"data\output"
        
    else:
        # butto file path
        input_dir = os.getcwd()
        output_dir = os.getcwd()
        
    return input_dir,output_dir,asset_file_dir


def main(mode):
    # choose file path
    input_dir,output_dir,asset_file_dir = dbg_mode(mode)
    
    # create curve and faces
    LsDyna.new()
    morph.CreCurveSetFaces(False,input_dir)
    mesh.FixGeoBatchMesh(output_dir,asset_file_dir,mpar="2dmesh",qual="2dmesh")

    # output model key file 
    model_file = os.path.join(output_dir,"model.key")
    LsDyna.save(model_file)
    
    # merge control file and mat file
    include.Merge_2dcrush(asset_file_dir, output_dir, "2dcrush", "model.key", "total.key")
    
    # create relative meta session
    repeat.main(asset_file_dir,output_dir)



if __name__ == "__main__":
    # butto: false
    # local test: true
    main(True)


