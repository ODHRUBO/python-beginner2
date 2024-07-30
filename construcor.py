class Student:
    def __init__(self,name,marks):#parametarize constructor
        self.name=name
        self.marks=marks
        print("Adding new student in database.")

s1=Student("seiam",90)
print(s1.name,s1.marks)

s2=Student("Emon",97)#attributes
print(s2.name,s2.marks)