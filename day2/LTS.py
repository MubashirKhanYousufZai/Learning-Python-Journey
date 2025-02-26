# List[] = mutable, most flexable
# Tupple ()= immutable, faster
# Set {} = mutable(add/remove), unordered, no duplicates, best for membership testing


# LIST[]:
# fruits = ["apple", "banana", "mango", "watermelon"]
# print(fruits)
# print(fruits[0]) # we can check whats in the list by inserting their Index no. in the list like that
# fruits[3] = "kela" # we can change the element by inserting its index no. like that
# fruits.append("kela") # we can add an element by using append method
# fruits.remove("apple") # we can remone an element by using remove method like that
# fruits.pop(0) # this methods remove the element of list by their index no.
# fruits.clear # this method will remove all the elements of the list
# for fruit in fruits:
#     print(fruit, end=" ")

# TUPPLE():
# fruits = ("apple", "banana", "mango", "watermelon") # we can not adit our tupple like list but its way faster to access

# SET{}:
fruits = {"apple", "banana", "mango", "watermelon", "watermelon", "watermelon", "watermelon", "watermelon"}

# fruits.add("pineapple") # we can add an element by using add methon in sets
# fruits.remove("apple") # we can remove an element by using remove methon in sets
# fruits.clear() # we can also sets
# for fruit in fruits:
#     print(fruits, end=" ")

fruit = input("Enter a fruit to search for: ")

if fruit in fruits:
    print(f"{fruit} was found")
else:
    print(f"{fruit} Not found")