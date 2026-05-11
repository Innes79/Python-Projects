import os 
import sys
import time 
import random

same = True
again = True

a = 10 
b = 10
c = 10
d = 10
e = 10
f = 10
h = 10
i = 10

print("welcome to the password generator")
time.sleep(1.5)
print("this password generator is coded so that there are no duplicate\nand lets you pick 4 digits 6 digits or 8 digits")
time.sleep(3)
input("press enter to start")
os.system("clear")
while again == True:
    g = input("would you like to generate 4 digits or 6 digits (4/6/8)")

    while same == True:
        if a == b or a == c or a == d or a == e or a == f or a == h or a == i or b == c or b == d or b == e or b == f or b == h or b == i or c == d or c == e or c == f or c == h or c == i or d == e or d == f or d == h or d == i or e == f or e == h or e == i or h == i:
            a = random.randint(1,9)
            b = random.randint(1,9)
            c = random.randint(1,9)
            d = random.randint(1,9)
            e = random.randint(1,9)  
            f = random.randint(1,9)
            h = random.randint(1,9)
            i = random.randint(1,9)
        else:
            same == False
            if g == "4": 
                print(f"{a}{b}{c}{d}")
                yn = input("would you like to go again (y/n)").lower()
                if yn[0] == "y":
                    again = True
                    a = b
                else:
                    again = False 
                    break
            elif g == "6":
                print(f"{a}{b}{c}{d}{e}{f}")
                yn = input("would you like to go again (y/n)").lower()
                if yn[0] == "y":
                    again = True
                    a = b
                else:
                    again = False
                    break
            elif g == "8":
                print(f"{a}{b}{c}{d}{e}{f}{h}{i}")
                yn = input("would you like to go again (y/n)").lower()
                if yn[0] == "y":
                    again = True
                    a = b
                else:
                    again = False
                    break

    
