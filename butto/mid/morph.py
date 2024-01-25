import random, os, ansa,sys
from ansa import base, constants,session

current_dir_path = os.path.dirname(__file__)
sys.path.append(current_dir_path)

from pre import segments
import group

# create 2d model
def CreCurveSetFaces(ext,directory,distance):
    line_sets,node_x,node_y=segments.get_line_sets(directory)
    for line_set in line_sets:
        curves = []
        for i in range(len(line_set)):     
            p1 = [node_x[int(line_set[i][0])], node_x[int(line_set[i][1])]]
            p2 = [node_y[int(line_set[i][0])], node_y[int(line_set[i][1])]]
            p3 = [0, 0]
            curve_id = base.CreateCurve(2, p1, p2, p3)
            curves.append(curve_id)
        # if not extrude, create faces and random set of section
        if not ext:                
            base.FacesNewPlanar(faces_array=curves, respect_user_selection=False)
        else:
            Extrude(distance)
            
    if not ext:
        group.RandomSet(line_sets)



def Extrude(distance):
    sel_entities = base.CollectEntities(constants.LSDYNA, None,"CURVE")
    dir_entities = []
    point1 = [0, 0, 0.]
    point2 = [0, 0, 2000.]
    base.SurfaceExtrudeExtrude(select_entities=sel_entities, dir_entities=dir_entities, direction_method=0, internal_face=False, respect_user_selection=False, point1=point1, point2=point2, distance=distance)
    
    props = base.CollectEntities(constants.LSDYNA, None, "SECTION_SHELL", False)
    base.AutoCalculateOrientation(props, True)

        
        



if __name__ == "__main__":
    directory = r"E:\#code\butto\data\input"
    line_sets,node_x,node_y = segments.get_line_sets(directory)
    session.New("discard")
    CreCurveSetFaces(False,directory,0)
    # SaveANSAFile(r"E:\#code\butto\data\output\curve.key")
    base.SetCurrentDeck(constants.LSDYNA)