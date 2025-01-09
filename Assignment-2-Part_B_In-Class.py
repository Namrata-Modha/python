"""
Date: 03-10-2024
Author: Namrata Modha
Purpose: To demonstrate the use of lists and tuples
"""

#define and initialize a list
temps = [48.0,30.5,20.2,100.0,42.0]
#print(temps[2])

temps[2] = "test"

#print(temps)


# repitition operator (*)

scores = [0] * 5
#print(scores)

#Append a single value with function
score = [1,2,3]
#print(score)
score.append(4)
#print(score)


#append insert remove

stats = [48.0,30.5,20.2,100.0]

stats.append(99.5)
#print(stats)

stats.insert(2, 40.0)
#print(stats)

stats.pop()
print(stats)

stats.pop(2)
print(stats)

stats.append(20.2)
stats.insert(1,20.2)
#print(stats)

x = len(stats)
print(x)



inventory = ["staff", "hat", "bread", "potion"]
print(inventory)

for x in inventory:
    print(x)


item = "bread"
if item in inventory:
    print("yes its found and the length of the array is:", len(inventory))
    #inventory.remove(item)

#print(inventory)

a = "new"
print(type(a))

a = 5
print(type(a))


