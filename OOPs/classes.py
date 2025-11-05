'''
syntax:
class class_name:
    # Initialize all the varibles 
    def __init__(self,parameters1,parameters2):
        self.parameters1 = parameters1
        self.paramters2 = parameters2
    
    def method1(self):
        pass

    def method2(self):
        pass
'''  
print("==============================")
class vehicle:
    # defining instance attributes
    def __init__(self,wheels,steering):
        self.wheels = wheels
        self.steering = steering
        self.x = 1
    
    def car(self):
        print(f"car has {self.wheels}")

    def truck(self):
        print(f"truck wheels are {self.wheels}")

# create an object of the class vehicle
v1 = vehicle(4,1)
# printing attributes
print("Attributes of vehicle v1")
print(v1.wheels)
print(v1.steering)

# print method outputs
v1.car()
v1.truck()

print("==============================")
'''
you can create methods with specific parameters as well. 
When the object calls the method, we need to pass that paramter data also
'''
class school:
    def __init__(self,student_name,student_id):
        self.student_name = student_name
        self.student_id = student_id
    
    def display_data(self,class_data):
        self.class_data = class_data
        print(f'Student with id {self.student_id} and name {self.student_name} belongs to class {self.class_data}')

s1 = school('Raman',101)
print(s1.student_id)
print(s1.student_name)
s1.display_data('2A')

'''
you can create a class where init doesnt take any parameters.
you can define methods which take respective parameters
'''
print("==============================")
class vehicle2:
    def __init__(self):
        pass
    def car(self,wheels):
        self.wheels=wheels
        print(f"number of wheels for car vehicle are : {self.wheels}")
    def truck(self,wheels):
        self.wheels = wheels
        print(f'number of wheels for truck are {self.wheels}')

v2 = vehicle2()
# use car method
v2.car(4)
# use truck method
v2.truck(6)

'''
# you can also create methods that dont use instance attributes(i.e without using self).
#  use @staticmethod decorator
'''
print("============11th nov==========")
class Person:
    # instance attributes
    def __init__(self,name):
        self.name = name
    
    @staticmethod
    def greeting():
        print(f'welcome to the session')

    def info(self):
        print(f'Person details are: {self.name}')

p1 = Person('Raman')
p1.greeting()
p1.info()

p2 = Person('Suman')
print(p1.name,p2.name)


# class attributes
'''
class class_name:
    # class attributes
    parameter1 = "abc"
    parameter2 = "xyz

    # to use the class attributes in methods, u can use @classmethod decorator
    @classmethod
    def method1(cls): # pass cls as the input parameter
        pass # to access class attributes, use cls.parameter1 or cls.parameter2
'''

class Python_classes:
    # class attributes
    company = '3RI'
    url = 'https://www.3ritechnologies.com/'

    # instance attributes
    def __init__(self,name,trainer):
        self.name = name
        self.trainer = trainer
    
    # methods
    def greeting(self):
        print(f"Greetings from {self.trainer}: Welcome from to the session {self.name}")
    
    # to use class attributes in a method
    @classmethod
    def login_info(cls):
        print(f'Welcome to {cls.company}. You can login using {cls.url}')

pc1 = Python_classes('Raman','Sindhura')
print(f"Class Attributes for pc1: {pc1.company} and {pc1.url}")
print(f"Instance Attributes for pc1: {pc1.name} and {pc1.trainer}")

pc2 = Python_classes('Suman','Sindhura')
print(f"Class Attributes for pc2: {pc2.company} and {pc2.url}")
print(f"Instance Attributes for pc2: {pc2.name} and {pc2.trainer}")

'''
Scenario1: 
Create a class blank account with attributes as account holder name,balance,account number.
Define below methods: 
withdrawal
deposit
transfer
'''
