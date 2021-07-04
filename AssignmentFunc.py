'''
Convert  the following into function, invoke or call the function  and comment what the code does
1)
a = 33
b = 200
if b > a:
    print("b is greater than a")

2)
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

3)
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and be are equal")
else:
    print("a is greater than b")

4)
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

5)
for x in range(6):
    print (x)

6)username = raw_input("Enter username:")
print("Username is: " + username)

'''

#Answers

#1
def func():
    a = 33
    b = 200
    if b > a:
        print("b is greater than a")
func()

#This code will only print out a statement if b is graeter than a

print()

#2)
def func1():
    a = 33
    b = 33
    if b > a:
        print("b is greater than a")
    elif a == b:
        print("a and b are equal")

func1()

#This code will print out a statement if a and b are equal

print()

#3)
def func2():
    a = 200
    b = 33
    if b > a:
        print("b is greater than a")
    elif a == b:
        print("a and be are equal")
    else:
        print("a is greater than b")
func2()

#This code will print out a statement if a is greater than b

print()

#4)
def for_loop(food):
    for x in food:
        print(x)
        if x == ("banana"):
            break
fruits = ["apple", "banana", "cherry"]

for_loop(fruits)

#This code will list the fruits and break at banana
print()

#5)
def for_loop(range):
    for x in range(6):
        print (x)


for_loop(range)

print()

#6)
def inp():
    username = input("Enter username")
    print("Username is: " + username)

inp()

#This code will first print out an input option for the user to enter his/her username and finally print a statement telling the user the username.
        

