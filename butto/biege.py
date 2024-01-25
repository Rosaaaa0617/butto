import os,sys,ansa
from ansa import session,base, constants

current_dir_path = os.path.dirname(__file__)
sys.path.append(current_dir_path)

from mid import morph, mesh, group, fixedAb, save, include


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


def bar_3pb(distance,input_dir,output_dir,asset_file_dir):
    # bar: model key file
    # asset_file_dir: ansa_qual/ansa_mpar
    session.New("discard")
    morph.CreCurveSetFaces(True,input_dir,distance)
    morph.Extrude(distance)
    mesh.FixGeoBatchMesh(output_dir,asset_file_dir,mpar="2dmesh",qual="2dmesh")
    group.set_bar()
    model_file = os.path.join(output_dir,"bar.key")
    save(model_file)
    print("-----save bar-----",model_file)

    session.New("discard")
    base.InputLSDyna(filename=os.path.join(asset_file_dir,"mat.key"), header="merge",create_parameters="on")
    base.InputLSDyna(filename=os.path.join(output_dir,"bar.key"), header="merge",create_parameters="on")

    include.SetIsoValue()

    # output
    



def fixed_3pb(output_dir,min_y,max_y,distance):
    # 3pb: model key file
    session.New("discard")
    fixedAb.clip(min_y,max_y,distance)
    mesh.FixGeoBatchMesh(output_dir,asset_file_dir,mpar="2dmesh",qual="2dmesh")
    group.threepb(min_y,max_y)
    include.SetFixValue()
    
    base.InputLSDyna(filename=os.path.join(output_dir,"bar.key"),header="merge",create_parameters="on")
    
    # output complete 3pb model key file
    model_file = os.path.join(output_dir,"model.key")
    save(model_file)
    print("-----save 3pb model-----",model_file)
    







if __name__ == "__main__":
    distance = 2000
    input_dir,output_dir,asset_file_dir = dbg_mode(True)
    
    bar_3pb(distance,input_dir,output_dir,asset_file_dir)
    min_y,max_y=fixedAb.findpoint()
    print('miny', min_y,max_y)
    
    # fixed_3pb(output_dir,min_y,max_y,distance)
    
    # include control and material
    
    # include.Merge_fix(asset_file_dir,output_dir,"3pb","model.key","total.key")
    base.SetCurrentDeck(constants.LSDYNA)
