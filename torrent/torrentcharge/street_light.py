from .foundation import Foundation

class Street_Light(Foundation):
    def __init__(self):
        super(Street_Light,self).__init__()
        self.charges=(self.unit*420)/100
        print("---------"*10)
        print("Your Charges: %0.2f"%self.charges)