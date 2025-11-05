## Properties and methods of parent class are accessed by child class

class student:
    def __init__(self,name,id,section):
        self.name = name
        self.id = id
        self.section = section
        self.school_name = 'Challenger Public School'
    
    def student_info(self):
        print(f'Welcome to {self.school_name}.\nStudent Details are {self.name,self.id,self.section}')

# class scores(student):
#     def __init__(self, mscore,sscore,hscore):
#         self.mscore = mscore
#         self.sscore = sscore
#         self.hscore = hscore
#     def show_scores(self):
#         print(f'Scores of {self.name} in Math subject are:{self.mscore}')

class scores(student):
    def __init__(self,name,id,section, mscore,sscore,hscore):
        super().__init__(name,id,section)
        self.mscore = mscore
        self.sscore = sscore
        self.hscore = hscore
    
    def show_scores(self):
        print(f'Scores of {self.name} in Math subject are:{self.mscore}')
    def greet(self):
        super().student_info()
        print(f'Student scores are provided . Data is saved.')
s1 = scores('Raman',11,'2K',56,67,78)
print('=====child class======')
s1.show_scores()
print('==========parent class access======')
s1.greet()

print('============Single Level Inheritance========')
# Single leve inheritance One parent has only one child
class Animal:
    def __init__(self,type):
        self.type = type
    def animal_info(self):
        print(f'Animals are part of Ecosystem. These have different types, we are discussing about {self.type}')
    
class Dog(Animal):
    def __init__(self, type,breed):
        super().__init__(type)
        self.breed = breed
    
    def make_sound(self):
        super().animal_info()
        print(f'The sound that dogs make is referred as barking.This {self.breed} of dogs are usually very calm in nature')

A1 = Animal('mammal')
A1.animal_info()

D1 = Dog('mammal','Labrador')
D1.animal_info()
D1.make_sound()
