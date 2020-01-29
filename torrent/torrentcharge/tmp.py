from .foundation import Foundation

class Tmp(Foundation):
    def __init__(self):
        super(Tmp,self).__init__()
        self.charges=((self.unit*500)/100)+25
        print("---------"*10)
        print("Your Charges: %0.2f"%self.charges)
