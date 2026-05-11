import os
import sys
import time

print("****Welcome to the calcualtor V2****")
time.sleep(0.5)
input("Press enter to calculate")
time.sleep(0.5)
os.system("clear")
again = "yes"
while again[0] == "y":
    expression = input("Enter a mathematical equasion:")
    result = eval(expression)
    time.sleep(0.3)
    print(result)
    time.sleep(0.3)
    again = input("would you like to calculate another?").lower()
    if again[0] == "y":
        time.sleep(0.3)
        print("ok")
        time.sleep(0.7)
        os.system("clear")
    elif again[0] == "n":
        time.sleep(0.3)
        print("come back soon")
        time.sleep(0.7)
        os.system("clear")
