
#list
myList = ["Willie", "IBM", 32, "DALLAS"]

#tuple
myTuple = (1,2,3,"one","two","three")

#dic
myDictionary = {"one" : 1, "Name" : "Willie", "Company" : "IBM"}


#for i in myDictionary.keys():
#    print myDictionary.get(i)

a = 1
b = 2

# function
def myAddOn(num1, num2):
   return num1 + num2

#print myAddOn(a,b)




# class
class Animal:
   name="patt"
   _unit="IBM"
   __owner="Willie"

   def bark(self):
      print ('Animal barks!')

   def _pFunc(self):
      print("This is a protective function")

   def __pWillie(self):
      print("This is a private thing!")


class Cat:
   name = "Edie"
   age = 5

# constructor
   def __init__(self,name,age):
      self.name = name
      self.age = age

   def play(self):
#      print(self.name, " can play, and she is ", self.age, " years old")
      print("{0} can play, and she is {1} years old!".format(self.name, self.age))

#cat1 = Cat(name="ID",age=3)
#cat1.play()



# inheritance
class Dog(Animal):
   pass








