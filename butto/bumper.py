import os,sys,ansa
from ansa import session,base,constants

current_dir_path = os.path.dirname(__file__)
sys.path.append(current_dir_path)

from mid import morph, mesh, include, save
   
   

def dbg_mode(dbg_path):
    # \butto\data
    asset_file_dir = os.path.join(os.path.dirname(current_dir_path),"data")
    print(current_dir_path)

    if dbg_path:
        # test file path
        input_dir = os.path.join(os.path.dirname(current_dir_path),"data\\input")
        output_dir = os.path.join(os.path.dirname(current_dir_path),"data\\output")
        
    else:
        # butto file path
        input_dir = os.getcwd()
        output_dir = os.getcwd()
        
    return input_dir,output_dir,asset_file_dir


if __name__ == "__main__":
    
    input_dir,output_dir,asset_file_dir = dbg_mode(True)

    # create curve and faces
    # asset_file_dir: ansa_qual/ansa_mpar
    session.New("discard")
    morph.CreCurveSetFaces(False,input_dir,0)
    mesh.FixGeoBatchMesh(output_dir,asset_file_dir,mpar="2dmesh",qual="2dmesh")

    # output model key file 
    model_file = os.path.join(output_dir,"model.key")
    save(model_file)

    # # merge material and load
    # session.New("discard")
    # include.Merge_2dcrush(asset_file_dir, output_dir,"2dcrush","model.key","total.key")
    # calcu_file = os.path.join(output_dir,"total.key")
    # save(calcu_file)
    base.SetCurrentDeck(constants.LSDYNA)


