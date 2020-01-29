from .foundation import Foundation

class Ltp(Foundation):
    def __init__(self):
        super(Ltp,self).__init__()
        self.charges=((self.unit*330)/100)+13.4
        print("---------"*10)
        print("Your Charges: %0.2f"%self.charges)