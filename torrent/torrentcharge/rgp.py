from .foundation import Foundation
from collections import OrderedDict

class Rgp(Foundation):#For RGP category
    def __init__(self):
        super(Rgp,self).__init__()  #calling foundation class constructor
        sub_cat={
                'A':['RGP : Residential General Purpose',self.rgp_func],
                'B':['BPL : Below Poverty Line',self.bpl_func]
            }
        print("---------"*10)
        for cat in sub_cat:
            print(cat+') '+sub_cat.get(cat)[0])
        print("---------"*10)

        opt=input("Selecet Your Option: ")
        
        if opt not in sub_cat.keys():
            print("Please Select Proper Choise")  
        else:
            val=sub_cat.get(opt)

            if val is not None:
                method=val[1]
            else:
                print("Please Select Proper Choise")
            method() #calling choise based method



    def rgp_func(self):
        sub_cat={'A': ['Single Phase',25],'B':['Three Phase',65]}
        
        print("---------"*10)
        for cat in sub_cat:
                print(cat+') '+sub_cat.get(cat)[0])
        print("---------"*10)
        choise=input('Please Select Your Choise: ')
        print("---------"*10)
        
        if choise in sub_cat.keys():
            data=OrderedDict({50:320,150:390})
            fix=sub_cat.get(choise)[1]
            if self.unit>200:data[self.unit-150]=490
            self.calculation(data,fix)
        else:
            print("Please Select Proper Choise")



    def bpl_func(self):
        data=OrderedDict({30:150,20:320,150:390})
        if self.unit>200:data[self.unit-150]=490
        self.calculation(data,5)
        

    
