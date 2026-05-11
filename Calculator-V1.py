import time
import os
import sys

repeat = True
answer = 0
inr = "0"

print("****Welcome to the calculator****")
time.sleep(2)
same = False
while repeat == True:
    if same == False:
        a = int(input("Enter the first value: "))
        b = int(input("Enter the second value: "))
    elif same == True:
        print("by the way the answer was", answer,)
        a = answer
        b = int(input("Enter the value you want to affect the previous answer: "))
    operation = input("What operation would you like to use (+ - * / // % ^): ")
    if operation == "+":
        answer = a + b
        print(a, "+", b, "=", answer)
        time.sleep(0.5)
        yn = str(input("Do you wanna repeat? ")).lower()
        if yn[0] == "y":
            repeat = True
            os.system("clear")
        elif yn[0] == "n":
            repeat = False
            os.system("clear")
    elif operation == "-":
        answer = a - b
        print(a, "-", b, "=", answer)
        time.sleep(0.5)
        yn = str(input("Do you wanna repeat? ")).lower()
        if yn[0] == "y":
            repeat = True
            os.system("clear")
        elif yn[0] == "n":
            repeat = False
            os.system("clear")
    elif operation == "*":
        answer = a * b
        print(a, "*", b, "=", answer)
        time.sleep(0.5)
        yn = str(input("Do you wanna repeat? ")).lower()
        if yn[0] == "y":
            repeat = True
            os.system("clear")
        elif yn[0] == "n":
            os.system("clear")
            repeat = False
    elif operation == "/":
        answer = a / b
        print(a, "/", b, "=", answer)
        time.sleep(0.5)
        yn = str(input("Do you wanna repeat? ")).lower()
        if yn[0] == "y":
            repeat = True
            os.system("clear")
        elif yn[0] == "n":
            os.system("clear")
            repeat = False
            os.system("clear")
    elif operation == "//":
        answer = a // b
        print(a, "//", b, "=", answer)
        time.sleep(0.5)
        yn = str(input("Do you wanna repeat? ")).lower()
        if yn[0] == "y":
            repeat = True
            os.system("clear")
        elif yn[0] == "n":
            os.system("clear")
            repeat = False
    elif operation == "%":
        answer = a % b
        print(a, "%", b, "=", answer)
        time.sleep(0.5)
        yn = str(input("Do you wanna repeat? ")).lower()
        if yn[0] == "y":
            repeat = True
            os.system("clear")
        elif yn[0] == "n":
            os.system("clear")
            repeat = False
    else:
        repeat = True
        time.sleep(0.5)
        os.system("clear")
        print("I did not recognise the input you typed, try again")
        inr = "1"
        input()
        os.system("clear")
    if inr != "1" and repeat == True:
        same = input("press y to use the answer from the last calculation and n to start a new calculcation: ")
        if same == "y":
            same = True 
            time.sleep(0.3)
            os.system("clear")
        elif same == "n":
            same = False 
            time.sleep(0.3)
            os.system("clear")
    inr = "0"
