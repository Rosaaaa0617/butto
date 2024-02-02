import ansa
from ansa import base, session, constants


    
class LsDyna:     
    d = constants.LSDYNA 
    
    @classmethod
    def save(self, output_ansa_file):
        print("Saving file",output_ansa_file)
        base.OutputLSDyna(filename=output_ansa_file, mode = "all")   
    
    @classmethod
    def new(self):
        session.New("discard")
        base.SetCurrentDeck(self.d)
    
    @classmethod
    # type: 'NODE','CURVE','SECTION_SHELL'...
    def prop(self, type):
        return base.CollectEntitiesI(self.d, None, type)
    
    @classmethod
    def new_set(self, name):
        return base.CreateEntity(self.d, "SET", {'Name':name})
    
    # @classmethod
    # def set_entity_values(self,value):
        
