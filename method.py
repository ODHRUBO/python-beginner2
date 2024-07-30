class Student:
    university="cu"

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def welcome(self):
        print("welcome students",self.name)

    def get_marks(self):
        return self.marks
    
s1=Student("seiam",96)
s1.welcome()
print(s1.get_marks)
