print("WELCOME TO PIZZA SHOPPP\n\n")
print("SMALL PIZZA : $10\n")
print("MEDIUM PIZZA : $15\n")
print("LARGE PIZZA : $20\n\n")
size = input("Size : ")
pepper = input("Pepperoni : ")
cheese = input("Cheese : ")
if (size == "S") :
    Bill = 10
    if (pepper == "Y") :
        Bill += 2
    if (cheese == "Y") :
        Bill += 1
elif (size == "M") :
    Bill = 15
    if (pepper == "Y") :
        Bill += 3
    if (cheese == "Y") :
        Bill += 1
elif (size == "L") :
    Bill = 20
    if (pepper == "Y") :
        Bill += 3
    if (cheese == "Y") :
        Bill += 1
else :
    print("Wrong Input\n")
print(f"\nTotal Bill : ${Bill}")
