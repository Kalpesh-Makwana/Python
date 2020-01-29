from .foundation import Foundation
from collections import OrderedDict

class Glp(Foundation):
    def __init__(self):
        super(Glp,self).__init__()
        sub_cat={'A': ['Single Phase',30],'B':['Three Phase',70]}
        
        print("---------"*10)
        for cat in sub_cat:
                print(cat+') '+sub_cat.get(cat)[0])
        print("---------"*10)
        p=input('Make Your Choise: ')
        print("---------"*10)
        
        if p in sub_cat.keys():
            data=OrderedDict({200:410})
            fix=sub_cat.get(p)[1]
            if self.unit>200:data[self.unit-200]=480
            self.calculation(data,fix)
        else:
            self.invalid_choise()
    
