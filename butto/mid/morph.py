import random, os, ansa, sys
from ansa import base, constants,session

current_dir_path = os.path.dirname(__file__)
sys.path.append(os.path.dirname(current_dir_path))

from mid.pre import segments
from mid.utils import LsDyna
from mid import group


# create 2d model
# True: extrude
def CreCurveSetFaces(ext,directory):
    line_sets,node_x,node_y=segments.get_line_sets(directory)
    # print(line_sets)
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
    if not ext:
        group.RandomSet(line_sets)



def Extrude(distance):
    ent = LsDyna.prop('CURVE')
    dir = []
    point1 = [0, 0, 0.]
    point2 = [0, 0, distance]
    base.SurfaceExtrudeExtrude(select_entities=list(ent), dir_entities=dir, direction_method=0, internal_face=False, respect_user_selection=False, point1=point1, point2=point2)
    
    shell = LsDyna.prop('SECTION_SHELL')
    base.AutoCalculateOrientation(list(shell), True)

        
if __name__ == "__main__":
    dir = r"data\input\multi"
    
    distance = 2000
    mode = "2d"
    LsDyna.new()
        
    if mode == "2d":
        print("mode:",mode)
        CreCurveSetFaces(False,dir)
    else:
        print("mode:",mode)
        CreCurveSetFaces(True,dir)
        Extrude(distance)
        
    


