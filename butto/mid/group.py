import random
from ansa import base, constants

from mid.utils import LsDyna

deck_=constants.LSDYNA

# 2dcrush random 
def RandomSet(line_sets):
    _ = len(line_sets)
    my_list = list(range(1,1+_))
    random.shuffle(my_list)
    
    lower = LsDyna.new_set('UP') #go up
    upper = LsDyna.new_set('DOWN') #go down
   
    
    for index, val in enumerate(my_list):
        group_name = lower if index % 2 == 0 else upper
        base.AddToSet(group_name, base.GetEntity(deck_,'SECTION_SHELL', val))
        
        
    
# 3pb pick nodes fixed
def threepb(min_y,max_y):
    set_end = []
    set_mid = []
    ENDS = base.CreateEntity(deck_, "SET", {'Name': 'ENDS','OUTPUT TYPE':'SET_PART'})
    MID = base.CreateEntity(deck_, "SET", {'Name': 'MID','OUTPUT TYPE':'SET_PART'})
    
    base.AddToSet(ENDS,base.GetEntity(deck_,'SECTION_SHELL',1))
    base.AddToSet(ENDS,base.GetEntity(deck_,'SECTION_SHELL',2))
    base.AddToSet(MID,base.GetEntity(deck_,'SECTION_SHELL',3))         
        
            
    
    
# 3pb pick nodes bar
def set_bar():
    ents = LsDyna.prop('SECTION_SHELL')
    bar = base.CreateEntity(deck_,"SET",{'Name':'BAR','OUTPUT TYPE':'SET_PART'})
    base.AddToSet(bar,ents)
    


# tensile pick nodes
def tensile(distance):
    set_head = []
    set_tail = []
    HEAD = base.CreateEntity(deck_, "SET", {'Name': 'HEAD'})
    TAIL = base.CreateEntity(deck_, "SET", {'Name': 'TAIL'})
      
    for ent in base.CollectEntitiesI(deck_, None, 'NODE'):
        z = ent.position[2]
        if 0 <= z <= 1:
            set_head.append(ent)
            base.AddToSet(HEAD, set_head)
            
        elif distance-distance/10 <= z <= distance+1:
            set_tail.append(ent)
            base.AddToSet(TAIL, set_tail)

