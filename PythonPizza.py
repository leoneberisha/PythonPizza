print("Welcome to PythonPizza! ")
pizza_size = input("What Size do you want your pizza L,M or S? ").lower()
bill=0
if pizza_size == "s":
    bill +=10
elif pizza_size =="m":
    bill+=12
elif pizza_size =="l":
    bill+=15

pepperoni = input("Would you like extra pepperoni? if Yes type 'Y', if No type 'N' ").lower()
if pepperoni == "y":
    if pizza_size == "s":
        bill+=2
    elif pizza_size == "m":
        bill +=3
    elif pizza_size == "l":
        bill +=4

cheese = input("Would you like extra cheese? Y/N? ").lower()
if cheese == "y":
    if pizza_size == "s":
        bill += 1
    elif pizza_size == "m":
        bill += 2
    elif pizza_size == "l":
        bill += 2.5

other_topics = input("Would you like other toppings (Mushroom/Olives)? ").lower()
if other_topics =="mushrooms" or other_topics=="olives":
    if pizza_size=="s":
        bill += 1.5
    elif pizza_size =="m":
        bill += 2
    elif pizza_size =="l":
        bill += 2.5

print(f'Your total bill is ${bill}')



