class Foundation:
    charges=0
    unit=0
    def __init__(self):
        flag=1
        while flag:
            self.unit=int(input("Enter unit:"))
            flag=1 if self.unit<=0 else 0

    def calculation(self,data,fixcharge):
        for key in data:
            if key<=self.unit: self.charges+=key*data[key]
            elif self.unit>=0: self.charges+=self.unit*data[key]
            else:break
            self.unit-=key
        self.charges=(self.charges/100)+fixcharge
        print("Your Charges: %0.2f"%self.charges)
    

    def invalid_choise():
        print("Invalid Choise")

