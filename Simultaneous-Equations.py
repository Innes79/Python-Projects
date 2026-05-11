import time 
import os
import sys
again = True
while again == True:
  a = float(input ("what is the number before x on the top equation: "))
  b = float(input ("what is the number before x on the botom equation: "))
  c = float(input ("what is the answer for the top question:"))
  d = float(input ("what is the answer for the bottom question:"))
  h = float(input("enter the value of y for the top equation: "))
  i = float(input("enter the value of y for the bottom equation: "))
  
  if a*i - b*h == 0:
      print("Error: No single answer (the equations are weird)")
      time.sleep(3)
  
  g = (c*i - d*h) / (a*i - b*h)
  l = (a*d - b*c) / (a*i - b*h)
  
  print("X =", g)
  print("Y =", l)
  again = input("would you like to go again?").lower()
  if again[0] == "y":
    again = True
  else:
    print("ok")
    
