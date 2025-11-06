# polymorphism: Taking multiple forms
# Operator, method

# Operator Overridding
sal1 = 45000
sal2 = 90000
print("+ performs addition when providing with numericals")
print(sal1+sal2)

first_name = "Raman"
Last_name = "Gaikwad"
print("+ performs concatenation-combining multiple texts")
print(first_name," ",Last_name)

student_scores = [90,89,67]
student_grades = ['A','A','C']
print("+ performs mergining of lists")
print(student_grades+student_scores)

# Method overriding
print("length function prints number of elements present in the list")
print(len(student_scores))

print("length function prints number of characters present in the string")
print(len(first_name))
print(len(Last_name))

print("============================")
# Userdefined Polymorphism scenario
class India:
    def capital(self):
        print(f'Capital of India is Delhi')

class UnitedStates:
    def capital(self):
        print(f'Capital of US is Washington')

class UK:
    def capital(self):
        print(f'Capital of United Kingdom is London')

c1 = India()
c2=UnitedStates()
c3 = UK()

c1.capital()
c2.capital()
c3.capital()

print("===============================")
def capital_display(country_object):
    country_object.capital()

capital_display(c1)
capital_display(c2)
capital_display(c3)