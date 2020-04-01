import random as r
class Robot:
    def __init__(self):
        fc=chr(r.randint(65,89))
        sc=chr(r.randint(65,89))
        number=r.randint(100,998)
        self.name=fc+sc+str(number)
    

    def reset(self):
        fc=chr(r.randint(65,90))
        sc=chr(r.randint(65,90))
        number=r.randint(100,999)
        self.name=fc+sc+str(number)

    def seed(self,word):
        self.name=word