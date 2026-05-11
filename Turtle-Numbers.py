import turtle
import os 
import sys
import time

print("In this python turtle demo, you are able to type")
print("numbers and they are drawn up on the screen.")
print("")
time.sleep(7)
print("this project took inspiration from leo and his letter drawing code")
print("")
time.sleep(5)
input("press enter to start ")
os.system("clear")

t = turtle.Turtle()
t.penup()

def n0():
  t.pendown()
  t.right(90)
  for e in range(144):
    t.left(2.5)
    t.forward(2)
  t.penup()
  t.forward(120)
  t.left(90)

def n1():
  t.pendown()
  t.left(90)
  t.forward(25)
  t.right(180)
  t.forward(50)
  t.penup()
  t.left(180)
  t.forward(25)
  t.right(90)
  t.pendown()
  t.forward(100)
  t.left(150)
  t.forward(50)
  t.penup()
  t.left(30)
  t.forward(56)
  t.left(90)
  t.forward(100)
  t.left(90)

def n2():
  t.left(90)
  t.pendown()
  t.right(180)
  t.forward(50)
  t.right(180)
  t.forward(50)
  t.right(130)
  t.forward(60)
  for a in range(12):
    t.forward(10)
    t.left(20)
  t.penup()
  t.right(20)
  t.forward(63)
  t.left(90)
  t.forward(130)
  t.left(90)
  
def n3():
  t.pendown()
  t.right(90)
  for b in range(12):
    t.forward(6.5)
    t.left(15.8)
  t.right(180)
  for c in range(12):
    t.forward(6.5)
    t.left(15.8)
  t.penup()
  t.left(70)
  t.forward(95)
  t.left(90)
  t.forward(90)
  t.left(90)
  
def n4():
  t.penup()
  t.right(90)
  t.forward(20)
  t.pendown()
  t.left(90)
  t.forward(100)
  t.left(120)
  t.forward(85)
  t.left(60)
  t.left(90)
  t.forward(100)
  t.penup()
  t.right(90)
  t.forward(58)
  t.left(90)
  t.forward(60)
  t.left(90)

def n5():
  t.right(90)
  t.pendown()
  for d in range(20):
    t.forward(6.5)
    t.left(10)
  t.right(110)
  t.forward(25)
  t.right(90)
  t.forward(45)
  t.penup()
  t.right(90)
  t.forward(98)
  t.left(90)
  t.forward(78.5)
  t.left(90)
  
def n6():
  t.pendown()
  t.right(90)
  for f in range(37):
    t.left(10)
    t.forward(5)
  for g in range(23):
    t.left(10)
    t.forward(5)
  t.right(90)
  for g in range(20):
    t.right(8)
    t.forward(5)
  t.penup()
  t.right(80)
  t.forward(105)
  t.left(90)
  t.forward(82)
  t.left(90)
  
def n7():
  t.pendown()
  t.right(20)
  t.forward(100)
  t.right(340)
  t.left(90)
  t.forward(50)
  t.right(180)
  t.forward(50)
  t.right(90)
  t.penup()
  t.forward(100)
  t.left(90)
  t.forward(85)
  t.left(90)
  
def n8():
  t.forward(25)
  t.pendown()
  for h in range(56):
    t.right(8)
    t.forward(4)
  t.left(185)
  for i in range(56):
    t.right(8)
    t.forward(4)  
  t.right(187)
  t.penup()
  t.forward(83)
  t.left(89)
  t.forward(150)
  t.left(90)

def n9():
  t.pendown()
  t.forward(80)
  for j in range(36):
    t.forward(5)
    t.left(10)
  t.right(180)
  t.forward(80)
  t.left(90)
  t.penup()
  t.forward(75)
  t.left(90)
again = "y"
speed = "4"

wspeed = str(input("would you like to set the speed, this will be permanent, if you put n, it will be at default speed (y/n):")).lower()
if wspeed == "y": 
  speed = input("enter the speed you want the sequence to run:")  
else:
  print("ok")
    
while again[0] == "y":
  t.clear()
  t.goto(0, 0)   
  time.sleep(0.5)
  os.system("clear")
  
  number = input("enter the numbers that you would like to display:")
  time.sleep(0.5)
  os.system("clear")
  
  t.setheading(0)
  t.speed(speed)
  t.left(180)
  t.forward(125)
  t.left(90)
  t.forward(50)
  t.right(180)
  
  
  count = len(number)
  
  i = 0
  while count != i:
    if number[i] == "0":
      n0()
    elif number[i] == "1":
      n1()
    elif number[i] == "2":
      n2()
    elif number[i] == "3":
      n3()
    elif number[i] == "4":
      n4()
    elif number[i] == "5":
      n5()
    elif number[i] == "6":
      n6()
    elif number[i] == "7":
      n7()
    elif number[i] == "8":
      n8()
    elif number[i] == "9":
      n9()
    else:
      print("")
    i+=1
  again = input("would you like draw more numbers? (y/n)")
  
  
