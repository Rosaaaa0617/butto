import os,sys,ansa
from ansa import session,base,constants

current_dir_path = os.path.dirname(__file__)
sys.path.append(current_dir_path)

import morph, mesh

# get coordinate from 3d model
def findpoint():
    min_y=float('inf')
    max_y=float('-inf')
    for ent in base.CollectEntitiesI(constants.LSDYNA, None, 'NODE'):
        y = ent.position[1]
        if y < min_y:
            min_y=y
        elif y > max_y:
            max_y=y
    return min_y,max_y
            

def clip(min_y,max_y,distance):
    session.New("discard")
    drawfixed(min_y,max_y,distance)
    cylinder(distance)


            
def drawfixed(min_y,max_y,distance):
    # define radius of circle
    r = (max_y-min_y)/4
    # define2 points
    A = (0.0, 0.0, 0.0)
    B = (0.0, 0.0, 10.0)
    # define center of circle
    C1 = (0.0, min_y-r, distance/10)
    C2 = (0.0, min_y-r, distance-distance/10)
    C3 = (0.0, max_y+r, distance/2)
    # draw circle
    Ab1 = base.CreateCircleCenter2PointsRadius(C1, A, B, r)
    Ab2 = base.CreateCircleCenter2PointsRadius(C2, A, B, r)
    Ab3 = base.CreateCircleCenter2PointsRadius(C3, A, B, r)
    
    return 
    
def cylinder(distance):
    base.CurvesConnectMulti(curves="all")
    sel=base.CollectEntities(constants.LSDYNA,None,'CURVE')
    dir_entities = []
    point1 = [-distance/3, 0, 0.]
    point2 = [distance/3, 0, 0.]
    base.SurfaceExtrudeExtrude(select_entities=sel, dir_entities=dir_entities, direction_method=0, internal_face=False, respect_user_selection=False, point1=point1, point2=point2, distance=distance/3)



    



if __name__ == "__main__":

    distance=2000
    asset_file_dir=r"E:\#code\butto\data"    
    output_dir=r"E:\#code\butto\data\output"
    input_dir=r"E:\#code\butto\data\input"



    # create curve and faces
    # asset_file_dir: ansa_qual/ansa_mpar
    session.New("discard")
    morph.CreCurveSetFaces(True,input_dir,distance)
    mesh.FixGeoBatchMesh(output_dir,asset_file_dir,mpar="2dmesh",qual="2dmesh")
    min_y,max_y=findpoint()
    clip(min_y,max_y,distance)