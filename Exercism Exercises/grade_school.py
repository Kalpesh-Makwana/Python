class School:
    def __init__(self):
        self.dicti={}

    def add_student(self, name, grade):
        self.dicti[name]=grade

    def roster(self):
        return [i[0] for i in sorted(self.dicti.items(),key=lambda item:(item[1],item[0]))]
        
    def grade(self, grade_number):
        return [stud for stud in sorted(self.dicti.keys()) if self.dicti[stud]==grade_number]
        
