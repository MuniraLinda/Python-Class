def first_function():
    print("my name is Muniratu")

def second_function():
    print("My age is 21")   

def agesum():
    a = 34 
    b = 56 
    c = a + b    
    print(c)

def inp():
    age = input("Enter your age")
    print("My age is " + age)

first_function()
second_function()
agesum()
inp()


def Add(a,b):
    c = a + b
    return c

a = Add(12,56)
print(a)

def Add(a,b,d):
    c = a + b - d
    return c

a = Add(12,56,45)
print(a)

def arbarg(*kids):
    print("The oldest child is " + kids[2])

arbarg('nana','kojo','keame')


def my_function(**kid):
    print("his last name is " + kid["lname"])

my_function(fname = "Tobias", lname = 'refsnes')

def cout(Country = "Ghana"):
    print("My country is " + Country)

cout()

def for_loop(food):

