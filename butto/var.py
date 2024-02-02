import random, os, ansa,sys
from ansa import base, constants,session

current_dir_path = os.path.dirname(__file__)
sys.path.append(current_dir_path)

from mid.pre import segments
from mid import group

def CreCurveSetFaces(directory,name,z,path):
    line_sets,node_x,node_y=segments.get_line_sets(directory)
    # print(line_sets)
    for line_set in line_sets:
        curves = []
        for i in range(len(line_set)):     
            p1 = [node_x[int(line_set[i][0])], node_x[int(line_set[i][1])]]
            p2 = [node_y[int(line_set[i][0])], node_y[int(line_set[i][1])]]
            p3 = [z, z]
            
            if not path:
                curve_id = base.CreateCurve(2, p1, p2, p3)
            else:
                curve_id = base.CreateCurve(2, p3, p2, p1)
        curves.append(curve_id)
    # print(curves)
    # if not path:
    #     base.FacesNewPlanar(faces_array=curves, respect_user_selection=False)

    #     print(curves)
    #     # setty = base.CreateEntity(constants.LSDYNA, "SET", {'Name': name})
    #     # base.AddToSet(setty, curves)   
    #     return curves    


def Extrude(distance):
    dir_entities = []
    point1 = [0, 0, 0.]
    point2 = [0, 0, distance]
    base.SurfaceExtrudeExtrude(select_entities=base.CollectEntities(constants.LSDYNA, None,"CURVE"), dir_entities=dir_entities, direction_method=0, internal_face=False, respect_user_selection=False, point1=point1, point2=point2)
    
    props = base.CollectEntities(constants.LSDYNA, None, "SECTION_SHELL", False)
    base.AutoCalculateOrientation(props, True)


if __name__ == "__main__":
    deck=constants.LSDYNA
    session.New("discard")
    base.SetCurrentDeck(deck)
    
    dir1=r"E:\#code\butto\data\input\star"
    dir2=r"E:\#code\butto\data\input\sec2"
    dirpath=r"E:\#code\butto\data\input\path"
    sec1=CreCurveSetFaces(dir1,'sec1',0,False)
    sec2=CreCurveSetFaces(dir2,'sec2',500,False)
    path=CreCurveSetFaces(dirpath,'path',0,True)
    # surf = base.SurfaceExtrudeExtrude(select_entities=sel_ent, dir_entities=dir_ent, direction_method=1,internal_face=False, respect_user_selection=False)
    # print(surf)
    
