print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
name = name1 + name2
f1 = name.count('t')
f2 = name.count('r')
f3 = name.count('u')
f4 = name.count('e')
s1 = name.count('l')
s2 = name.count('o')
s3 = name.count('v')
s4 = name.count('e')
perc1 = str(f1+f2+f3+f4)
perc2 = str(s1+s2+s3+s4)
perc = perc1 + perc2
perc_int = int(perc)
if(perc_int <= 10 or perc_int >= 90) :
    print(f"Your percent is {perc}, You go together like coke and mentos.")
elif(perc_int >= 40 and perc_int <= 50) :
    print(f"Your percent is {perc}, You go alright together.")
else :
    print(f"Your percent is {perc}.")
