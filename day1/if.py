# if statments = it only executes the statment when the condition is true 
# if, elif, else

age = int(input("Enter Your Age: "))
has_ticket = True
price = 10.00

if age >= 40:  # Senior Citizen should come first
    print("You're a Senior Citizen. Budday 🤬")
    print(f"The ticket price for a senior is ${price * 0.75}")        
elif age >= 18:
    print("You're an adult")
    print(f"The ticket price for an adult is ${price}")
else:
    print("You're a child")
    print(f"The ticket price for a child is ${price * 0.5}")

if has_ticket:
    print("You have a ticket, you may enter")
else:
    print("You need to buy a ticket")
      