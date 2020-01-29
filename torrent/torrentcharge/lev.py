from .foundation import Foundation

class Lev_Lt(Foundation):
    def __init__(self):
        super(Lev_Lt,self).__init__()
        self.charges=((self.unit*410)/100)+25
        print("---------"*10)
        print("Your Charges: %0.2f"%self.charges)