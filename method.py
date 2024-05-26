class Employee:
   empCount = 0
   def __init__(self, name, age):
      self.__name = name
      self.__age = age
      Employee.empCount += 1
   def showcount(self):
         print (self.empCount)
   counter=classmethod(showcount)

e1 = Employee("Bhavana", 24)
e2 = Employee("Rajesh", 26)
e3 = Employee("John", 27)

e1.showcount()
Employee.counter()


@staticmethod
def showcount():
            print (Employee.empCount)
e1.showcount()
Employee.showcount()

lst = [25, 12, 10, -21, 10, 100]
for num in lst:
   print (num, end = ' ')