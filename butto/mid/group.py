import random
from ansa import base, constants

# 2dcrush random 
def RandomSet(line_sets):
    length=len(line_sets)
    my_list=list(range(1,1+length))
    lower = base.CreateEntity(constants.LSDYNA, "SET", {'Name': 'UP'}) #go up
    upper = base.CreateEntity(constants.LSDYNA, "SET", {'Name': 'DOWN'}) #go down
   
    random.shuffle(my_list)
    
    for index, val in enumerate(my_list):
        group_name = lower if index % 2 == 0 else upper
        base.AddToSet(group_name, base.GetEntity(constants.LSDYNA,'SECTION_SHELL', val))
        
        
    


    
# 3pb pick nodes fixed
def threepb(min_y,max_y):
    set_end = []
    set_mid = []
    ENDS = base.CreateEntity(constants.LSDYNA, "SET", {'Name': 'ENDS','OUTPUT TYPE':'SET_PART'})
    MID = base.CreateEntity(constants.LSDYNA, "SET", {'Name': 'MID','OUTPUT TYPE':'SET_PART'})
    
    base.AddToSet(ENDS,base.GetEntity(constants.LSDYNA,'SECTION_SHELL',1))
    base.AddToSet(ENDS,base.GetEntity(constants.LSDYNA,'SECTION_SHELL',2))
    base.AddToSet(MID,base.GetEntity(constants.LSDYNA,'SECTION_SHELL',3))         
        
    # for ent in base.CollectEntitiesI(constants.LSDYNA, None, 'NODE'):
    #     y = ent.position[1]
    #     if y <= min_y:
    #         set_end.append(ent)
    #         base.AddToSet(ENDS, set_end)
            
    #     elif max_y <= y:
    #         set_mid.append(ent)
    #         base.AddToSet(MID, set_mid)
            
    
    


# 3pb pick nodes bar
def set_bar():
    ents=base.CollectEntitiesI(constants.LSDYNA,None,'SECTION_SHELL')
    bar = base.CreateEntity(constants.LSDYNA,"SET",{'Name':'BAR','OUTPUT TYPE':'SET_PART'})
    base.AddToSet(bar,ents)
    



# tensile pick nodes
def tensile(distance):
    set_head = []
    set_tail = []
    HEAD = base.CreateEntity(constants.LSDYNA, "SET", {'Name': 'HEAD'})
    TAIL = base.CreateEntity(constants.LSDYNA, "SET", {'Name': 'TAIL'})
      
    for ent in base.CollectEntitiesI(constants.LSDYNA, None, 'NODE'):
        z = ent.position[2]
        if 0 <= z <= 1:
            set_head.append(ent)
            base.AddToSet(HEAD, set_head)
            
        elif distance-distance/10 <= z <= distance+1:
            set_tail.append(ent)
            base.AddToSet(TAIL, set_tail)

