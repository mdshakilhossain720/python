
def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return;

# Now you can call printme function
printme("I'm first call to user defined function!")
printme("Again second call to the same function")


def greetings(name):
    "This is docstring of greetings function"
    print("Hello {}".format(name))
    return


greetings("Samay")
greetings("Pratima")
greetings("Steven")


def printinfo( name, age = 35 ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return

# Now you can call printinfo function
printinfo( age=50, name="miki" )
printinfo( name="miki" )

def printinfo( name, age ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return

# Now you can call printinfo function
# by positional arguments
printinfo ("Naveen", 29)

# by keyword arguments
printinfo(name="miki", age = 30)

#global variables
name = 'TutorialsPoint'
marks = 50
def myfunction():
   # accessing inside the function
   print("name:", name)
   print("marks:", marks)
# function call
myfunction()