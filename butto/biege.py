import os,sys,ansa
from ansa import session, base, constants

current_dir_path = os.path.dirname(__file__)
sys.path.append(current_dir_path)

from mid import morph, mesh, group, fixedAb, include
from mid.utils import LsDyna
from post import repeat


def dbg_mode(dbg_path):
    # \butto\data
    asset_file_dir = os.path.join(os.path.dirname(current_dir_path), "data")

    if dbg_path:
        # test file path
        input_dir = r"data\input\star"
        output_dir = r"data\output"
        
    else:
        # butto file path
        input_dir = os.getcwd()
        output_dir = os.getcwd()
        
    return input_dir,output_dir,asset_file_dir


def bar_3pb(distance,input_dir,output_dir,asset_file_dir):
    # bar: model key file
    # asset_file_dir: ansa_qual/ansa_mpar
    LsDyna.new()
    morph.CreCurveSetFaces(True,input_dir)
    morph.Extrude(distance)
    mesh.FixGeoBatchMesh(output_dir,asset_file_dir,mpar="2dmesh",qual="2dmesh")
    group.set_bar()
    include.SetIsoValue()
    
    # output bar model 
    model_file = os.path.join(output_dir,"bar.key")
    LsDyna.save(model_file)
    print("-----save bar-----",model_file)



def fixed_3pb(output_dir,min_x,max_x,min_y,max_y,distance,asset_file_dir):
    # 3pb: model key file
    LsDyna.new()
    fixedAb.main(min_x,max_x,min_y,max_y,distance)
    mesh.FixGeoBatchMesh(output_dir,asset_file_dir,mpar="2dmesh",qual="2dmesh")
    group.threepb(min_y,max_y)
    include.SetFixValue()
    
    # merge with bar model
    base.InputLSDyna(filename=os.path.join(output_dir,"bar.key"),header="merge",create_parameters="on")
    
    # output complete 3pb model key file
    model_file = os.path.join(output_dir,"model.key")
    LsDyna.save(model_file)
    print("-----save 3pb model-----",model_file)
    

def main(distance,mode):
    input_dir,output_dir,asset_file_dir = dbg_mode(mode)
    
    # draw bar
    bar_3pb(distance,input_dir,output_dir,asset_file_dir)
    min_x,max_x,min_y,max_y=fixedAb.findpoint()
        
    # draw 3pb model
    fixed_3pb(output_dir,min_x,max_x,min_y,max_y,distance,asset_file_dir)
    
    # include control and material  
    include.Merge_fix(asset_file_dir,output_dir,"3pb","model.key","total.key")
    
    # create meta session file
    repeat.main(asset_file_dir,output_dir)
    






if __name__ == "__main__":
    main(2000,True)

    
