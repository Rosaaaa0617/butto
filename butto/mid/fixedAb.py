import os,sys,ansa
from ansa import session,base,constants

from mid.utils import LsDyna
 

# get coordinate from 3d model
def findpoint():
    positions = list(ent.position for ent in LsDyna.prop('NODE'))

    return (
        min(x for x, _, _ in positions),
        max(x for x, _, _ in positions),
        min(y for _, y, _ in positions),
        max(y for _, y, _ in positions)
    )


def main(min_x,max_x,min_y,max_y,distance):
    LsDyna.new()
    drawfixed(min_x,min_y,max_y,distance)
    cylinder(min_x,max_x)


            
def drawfixed(min_x,min_y,max_y,distance):
    # define radius of circle
    r = (max_y-min_y)/4
    # define2 points
    A = (min_x, 0.0, 0.0)
    B = (min_x, 0.0, 10.0)
    # define center of circle
    C1 = (min_x, min_y-r, distance/10)
    C2 = (min_x, min_y-r, distance-distance/10)
    C3 = (min_x, max_y+r, distance/2)
    # draw circle
    centers = [C1,C2,C3]
    for center in centers:
        base.CreateCircleCenter2PointsRadius(center, A, B, r)
        base.CurvesConnectMulti(curves="all")


def cylinder(min_x,max_x):
    distance=max_x-min_x
    base.CurvesConnectMulti(curves="all")
    
    ent = LsDyna.prop('CURVE')
    dir_entities = []
    point1 = [min_x, 0, 0.]
    point2 = [max_x, 0, 0.]
    base.SurfaceExtrudeExtrude(select_entities=list(ent), dir_entities=dir_entities, direction_method=0, internal_face=False, respect_user_selection=False, point1=point1, point2=point2, distance=distance)


