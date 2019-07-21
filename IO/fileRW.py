# this is for file read and write

# method 1
#myFile = open('willie.txt')
#content = myFile.read()
#print(content)
# must close this, like java
#myFile.close()

# method 2
# if we use this, we don't have to close the file stream
#with open('willie.txt') as f:
#    print(f.read())

'''
myfile = open('willie.txt')
content = myfile.readlines()

for i in content:
    print(i)
    print("------")

myfile.close()
'''



# write
# argument could be 'w' - write,'a' - append
with open('willie.txt','a') as f:
    f.write('This is the write test\n')




