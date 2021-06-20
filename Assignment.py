#Develop an application for the preparation of rice and stew. The application must include:

#A List of the ingredient using the list data type

ingredients = ['rice', 'water', 'oil','tomatoes', 'onion', 'pepper', 'fish', 'pepper', 'spices', 'vegetables']

print(ingredients)

#Staff details in a dictionary which include their names ,rank, department, id number and their telephone number in 12 digit.

Staff1 = {
    'Name':'Eric Adjei', 
    'Rank':'Chef', 
    'Department':'Operations', 
    'Id_number':'P201',
'Telephone_number':233545034567
 }
Staff2 = {
    'Name':'Adiza Malik', 
    'Rank':'Kitchen Assistant', 
    'Department':'Operations', 
    'Id_number':'P2045',
'Telephone_number':233575039778
 }
Staff3 = {
    'Name':'Yaw Sarpong', 
    'Rank':'Customer Service', 
    'Department':'Administrative', 
    'Id_number':'P2030',
'Telephone_number':233245034587
 }

Staff4 = {
    'Name':'Majeed A. Rahman', 
    'Rank':'Marketing Officer', 
    'Department':'Marketing', 
    'Id_number':'P2040',
'Telephone_number':233305034587
 }

print(Staff1)
print(Staff2)
print(Staff3)
print(Staff4)

#Using set , create a list of the number of tables(10) in the restaurant, which has been numbered according "table 1", "table 2", etc.
#And using for loop, loop through the set of items

Tablelist = {'table 1', 'table 2', 'table 3', 'table 4', 'table 5', 'table 6', 'table 7', 'table 8', 'table 9', 'table 10'}

for x in Tablelist:
    print(x)

#Assign the food prpearation to a multiline string, detailing how rice and stew is prepared. 


The_Process = ("""The Cooking Process
1. Put a saucepan with two cups of water and a tablespoon of salt and few drops of oil on fire and bring to boil.
2.Wash rice and add to boiling water. Allow it to boil for 5 minutes and bring fire to low heat.
3.For the stew, prep your ingredients by cutting onions, washing fish, washing tomamtoes and pepper and blending all together with some onions.
4. Put a clean pan on fire and add some oil,
5. Add chopped onions and fry for some minutes.
6. Pour in your blended tomatoes and add some tomatoe puree as well.
7. Allow it to cook for some time until the mixture is no more watery.
8. Add your fish, spices and seasoning(bay leave, curry, msg).
9. Avoid rigorous stirring so as to not break the fish.
10. Add chopped vegetables, stir, simmer for 2 minutes and take off from fire.
11. Check on your rice which should be cooked by now.
12. Serve hot and garnish as tradition demands.


""")
print(The_Process)