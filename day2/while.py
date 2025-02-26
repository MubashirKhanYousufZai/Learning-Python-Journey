# WHILE LOOPS = remains the code working untill the condition is true

# while 17 == 17 :
#     print("Hello!")
name = input("Enter Your Name: ")
while name == "" :
    name = input("Enter Your Name: ")

age = int(input("Enter Your Age: "))
while age < 0 :
    print("Age can't be less then 0")
    age = int(input("Enter Your Age: "))


print(f"Hello {name}!")
print(f"You're {age} years old!")