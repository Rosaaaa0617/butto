import os,sys

current_dir_path = os.path.dirname(__file__)
sys.path.append(current_dir_path)

from mid import morph, mesh, group, fixedAb, save, include
from post import repeat
from mid.pre import segments

from ansa import base, constants,session


def findpoint():
    min_y=float('inf')
    max_y=float('-inf')
    min_x=float('inf')
    max_x=float('-inf')
    for ent in base.CollectEntitiesI(constants.LSDYNA, None, 'HOT POINT'):
        y = ent.position[1]
        x = ent.position[0]
        
        if y < min_y:
            min_y=y
        elif y > max_y:
            max_y=y
        
        if x < min_x:
            min_x = x
        elif x > max_x:
            max_x = x

    return min_x, max_x, min_y, max_y



if __name__ == "__main__":
    directory = r"E:\#code\butto\data\input"
    line_sets,node_x,node_y = segments.get_line_sets(directory)
    session.New("discard")
    
    # create section
    mode="2d"
    distance = 2000
    if mode == "2d":
        morph.CreCurveSetFaces(False,directory)
    else:
        morph.CreCurveSetFaces(True,directory)
       
       
    # Extrude(distance)
    base.SetCurrentDeck(constants.LSDYNA)
    dir_entities = []
    point1 = [0, 0, 0.]
    point2 = [0, 0, 500]
    base.SurfaceExtrudeExtrude(select_entities=base.CollectEntities(constants.LSDYNA, None,"FACE"), dir_entities=dir_entities, direction_method=0, internal_face=False, respect_user_selection=False, point1=point1, point2=point2)

    min_x, max_x, min_y, max_y=findpoint()
    print(min_x, max_x, min_y, max_y)
    
    