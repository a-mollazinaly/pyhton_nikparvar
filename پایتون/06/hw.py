print("In The Name Of God!")
print("Hello World!")
print("# He - Will - Come!")
# --------------------------------------------#
first_name = input("please enter your first_name: ")
last_name = input("please enter your last_name: ")
age = input("please enter your age: ")
math_score = int(input("please enter your math_score: "))
physics_score = int(input("please enter your physics_score: "))
python_score = int(input("please enter your python_score: "))
e = 0
#---------------------------------------------#
class Student:
    def __init__(self, first_name, last_name, age, math_score, physics_score, python_score):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.math_score = math_score
        self.physics_score = physics_score
        self.python_score = python_score
        
    def check_status (self):
        if (float((self.math_score + self.physics_score + self.python_score)/3)) >= 17:
            print("accepted")
        else :
            print("failed")

#---------------------------------------------#
student = Student(first_name, last_name, age, math_score, physics_score, python_score)