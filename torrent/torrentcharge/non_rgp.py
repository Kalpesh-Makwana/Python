from .foundation import Foundation

class Non_Rgp(Foundation):
    def __init__(self):
        super(Non_Rgp,self).__init__()
        self.charges=(self.unit*450)/100
        if self.unit<=5:
            self.charges+=70
        elif self.unit>5 and self.unit<=15:
            self.charges+=90
        print("---------"*10)
        print("Your Charges: %0.2f"%self.charges)