# File Handling
# Read the contents of the file => view the contents
# Write the contents to the file => Adding data to file
# Append the contents to the file => Update new data to the file
print("===========read method==========")
# read the file - read(): read all the contents of the file
with open('dummy.txt','r') as file:
    print(file.read())
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