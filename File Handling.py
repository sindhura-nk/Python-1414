# File Handling
# Read the contents of the file => view the contents
# Write the contents to the file => Adding data to file
# Append the contents to the file => Update new data to the file
print("===========read method==========")
# read the file - read(): read all the contents of the file
with open('dummy.txt','r') as file:
    print(file.read())
# if the file doesn't exist, FileNotFound error

print("=============readline method=========")
# read the file- readline(): reads line data
with open('dummy.txt','r') as file:
    print(file.readline())
print("=============readlines method=========")   
# read the file- readlines(): multiple lines
with open('dummy.txt','r') as file:
    l1 = file.readlines()
    print(l1)
    print(len(l1))
    for line in l1:
        print(line)

# write contents to the file => write()
with open('dummy.txt','w') as file:
    file.write('updating line four') 
# if contents in the file already exist, then write() will replace all the contents

# try reading a file that doesnt exist
#with open('test.txt','r') as file:
#    print(file.read())
print("=================write=======================")
# try write to a file that doesn't exist
with open('test.txt','w') as file:
    file.write('This is a new file created by write method')
with open('test.txt','r') as file:
    print('viewing the file created using write method')
    print(file.read())
print("=================writelines=======================")
# you can add multiple lines using writelines method=> always include \n at the end of each line
with open('test.txt','w') as file:
    l1 = ['This is a new file created by write method \n','this is the second line \n,'
    'this is the third line \n']
    file.writelines(l1)
with open('test.txt','r') as file:
    print('viewing the file created using write method')
    print(file.read())

print("=================Append data==========")
with open('dummy.txt','a') as file:
    file.write('\nUpdating line five')

with open('dummy.txt','r') as file:
    print(file.read())

print("==========seek and tell =============")
with open('dummy.txt','r') as file:
    file.seek(10) # change the cursor position
    print(file.tell()) # current position information

print("==============read and write- r+ ==========")
#with open('test2.txt','r+') as file:
#    print(file.read())

with open('dummy.txt','r+') as file:
    print(file.read()) # if read is used first, cursor position moves to the end of the file
    file.write('This is new data being added with r+ method ') # write will add the content at the end of the file
    print(file.read())

with open('test.txt','r+') as file:
    file.write('Hello World') # this will add the data(by default position is at the beginning of the file)
    file.seek(0)
    print(file.read())

# print("============== append and read a+ ============")
# with open('dummy.txt','a+') as file:
#     file.write(' with some information')
#     # gives the current cursor position in file
#     print(f'reading file at last position {file.tell()}: ')
#     print(file.read())
#     file.seek(0) # shift the cursor to 0th position
#     print(f'After shifting position, {file.tell()}:')
#     print(file.read())

print("===========read and write - w+ ==========")
with open('test2.txt','w+') as file:
    file.write("This is a new file created")
    file.seek(0)
    print(file.read())
print("===================reopening and write data to existing file=========")
with open('test2.txt','w+') as file:
    file.write('this data is updated with w+')
    file.seek(0)
    print(file.read())

# Can also open image files 
print("=============Image file reading============")
with open('imagecheck.png','rb') as file:
    print(file.read())

# if the file is present in another directory, you can use os functions
import os
os.chdir(r'E:\Sindhura\3RI')

with open('pending.txt','r') as file:
    print(file.read())