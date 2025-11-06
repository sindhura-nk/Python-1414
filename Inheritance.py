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

# Multilevel Inheritance
print("=========Multilevel Inheritance============")
class Employee:
    def __init__(self,name,location,mobile):
        self.name = name
        self.location = location
        self.mobile = mobile
    def emp_info(self):
        print(f"Employee Details are :{self.name}, He/She joined at {self.location}.You can reach him/her on {self.mobile}")

class Lead(Employee):
    def __init__(self, name, location, mobile,project):
        super().__init__(name, location, mobile)
        self.project = project
    def get_project_info(self):
        super().emp_info()
        print(f'Employee {self.name} is working as a Lead for {self.project}project')

class Manager(Lead):
    def __init__(self, name, location, mobile, project,client):
        super().__init__(name, location, mobile, project)
        self.client = client
    def get_manager_info(self):
        super().emp_info()
        super().get_project_info()
        print(f'Employee {self.name} works as a Lead for {self.project}. He is currently assigned as a manager for {self.client}Client')

m1 = Manager('Raman','Kharadi',345657345,'BT-IPCS','BT-Global')
m1.get_manager_info()
print(f'Data of employee : {m1.name},{m1.mobile},{m1.location},{m1.client},{m1.project}')

## Hierarchal Inheritance : Single Parent and 2 child
# Showroom and Car models scenario
print("=============Hierarchal Inheritance================")
class Showroom:
    def __init__(self):
        self.name = "Garve Hyundai"
        self.location = "Pune-Wakad Area"
    def greeting(self):
        print(f'Welcome to the {self.name} Showroom. We provide car deliveries around {self.location} area. Feel free to explore through our best models.')

class hyundai_i10(Showroom):
    def __init__(self,min_price,max_price):
        super().__init__()
        self.min_price = min_price
        self.max_price = max_price
    def get_i10_info(self):
        super().greeting()
        if self.min_price>10 and self.max_price<20:
            print(f'Grand i10 is the best choice. It provides good space for a family of four. ')
        else:
            print(f'Grand i10 falls under a different margin, We have more better choices. would you like to explore other models.')

class hyundai_i20(Showroom):
    def __init__(self,min_price,max_price):
        super().__init__()
        self.min_price = min_price
        self.max_price = max_price
    def get_i20_info(self):
        super().greeting()
        if self.min_price>20 and self.max_price<40:
            print(f'Grand i20 is the best choice. It provides good space for a family of four. ')
        else:
            print(f'Grand i20 falls under a different margin, We have more better choices. would you like to explore other models.')

enq1 = hyundai_i10(13,17)
enq1.get_i10_info()
enq2 = hyundai_i20(25,35)
enq2.get_i20_info()
