#Assignments : Conditionals, Whileloop, Forloop
#Write a program that prints your name if a is greater than b
print()

a = 10
b = 5
if a > b:
    print("Muniratu Fianyeku")

print()    
#2. Write a program that prints the name of the instructor if a is not equal to b
a = 10
b = 5
if a != b:
    print("Nana Kwame Nketsiah")

print()    

#3.Write a program that prints yes if a is equal to b otherwise print b
a = 10
b = 10
if a == b:
    print("Yes")
else:
     print("b")

print()     

#4.Write a program that prints your gender if a is equal to b and c is equal to d
a = 5
b = 5
c = 10
d = 10
if a == b and c == d:
    print("female")

print()

#5.Write a program that print i as long as i is less than 6
i = 1

while i < 6:
    print(i)
    i += 1

print()

#6.Write a program that stop the loop if i is 3
i = 1

while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

print()

#7.Write a program when i is 3, it jumps directly to the next iteration
i = 1

while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
    i += 1

print()

#8.Write a program that loops through the items in the fruit list fruits = ['apple', 'banana', 'cherry']'''
fruits = ['apple', 'banana', 'cherry']
for F in fruits:
    print(F)

print()

#9. Write a program when the item value is banana , jumps directly to the next item
fruits = ['apple', 'banana', 'cherry']
for F in fruits:
    print(F)
    if F == "banana":
        continue

print()

#10.Write a program that uses the range function to loop through a code 6 times.
for m in range(6):
    print(m)