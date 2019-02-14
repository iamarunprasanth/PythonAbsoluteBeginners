# class
""""
class is like a blue print contains menthods, attributes, constructors.
"""
# defining a class
class Class1():
# THIS IS A class declaration
# Class name should start with a Upper case letter.
# DEFINING A MEthod
    def method(self):
        # methods inside a class will have a self keyword as the first argument.
        """
        This is a doc string inside method
        """
        print('this is a method inside class1')
# CONSTRUCTORS
"""
Constructors are special methods gets invoked when object of the class is created.
"""
# DEFINING A CONSTRUCTOR
def __init__(self):
    """
    THis is a doc string of a constructor
    """
# CREATING MULTIPLE OBJECTS
obj1 = Class1()
obj2 = Class1()

# SAMPLE CRITTER PROGRAM FROM BOOK
class Critter():
    # creating private attribute
    """PRivate attribute will start with __followed by attr name"""
    def __init__(self,name, age=1, reg_no=0):
        # Initializing attribute.
        self.name = name
        self.age = age
        self.__reg_no =reg_no
    def __str__(self):
        return "I am "+ self.name + ", my age is: "+ str(self.age)
    def talk(self):
        """Here we are accessing the name attribute"""
        print('I am '+self.name+ ' my reg no is: '+str(self.__reg_no))
        # accessing private method from public
        self.__private_method()
    # Creating a static method
    @staticmethod
    def status():
        """Static method doesn't need self attribute as an argument
        and it will contain a @staticmethod annotation
        static method can be called by the class name and using obj ref"""
        print('I am a static method ')
    # creating private methods
    def __private_method(self):
        """This is a private method"""
        print('from private method ')

    # creating properties
    @property
    def reg_no(self):
        return self.__reg_no
    @reg_no.setter
    def reg_no(self,reg_no):
        if type(reg_no) == int and reg_no > 1:
            self.__reg_no = reg_no
        else:
            print('failed to set registration number')


crit1 = Critter('arun',2,'dfsdfsdfsdf')
# accessing attribute
crit1.talk()
# Printing an object.
print(crit1)
crit1.status()
Critter.status()
# Special way of accessing private attribute
print(crit1._Critter__reg_no)
print(crit1._Critter__private_method())
print(crit1.reg_no)

