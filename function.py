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
    for x in food:
        print(x)

fruits = ['peper', 'onion', 'sardine']
ingre = ['mango','apple']
print(for_loop(fruits))
print(for_loop(ingre))

def for_loop():
    a = 4
    b = 4
    if a > b:
        print("Yes a is greater than b")
    else:
        print("No a is not graeter than b")

for_loop()

def ret(x):
    return 5 * x

print(ret(4))




