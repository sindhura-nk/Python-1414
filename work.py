print('continuing my logic code')

import Power
s1 = Power.square(9)
print(f'Square of the number is {s1}')

# instead of using power.method, you can import the required method using from-import
from Power import squareroot
s2 = squareroot(45)
print(f'Square root of the number is {s2:.2f}')

# you can import all the methods
from Power import *

# you can import specific methods alone
from Power import cube,quarduple
c1 = cube(45)
print(f'cube of the number is {c1}')
q1 = quarduple(9)
print(f'Quadraple of the number is {q1}')

print('======================================')
# import even-odd
import evenodd
print(evenodd.even_odd(56))
print('======================================')
# use from import and use even_odd method, print the output whether 67 is even or odd
from evenodd import even_odd
print(even_odd(67))

print('======================================')
print("==========PACKAGES====================")

from calculations import factorial
f1 = factorial.fact(97)
print(f1)

from calculations.factorial import fact
f2 = fact(4)
print(f2)

# will import all the modules present in calculations
from calculations import * 

# will import specific modules from calculation
from calculations import fibonacci
f3 = fibonacci.fibo(15)
print(list(f3))


print("=====================================")
