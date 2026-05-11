import time 
import os 
import sys

repeat = True
seconds = int(input("enter what the current second is:"))
minutes = int(input("enter what the current minute is:"))
hours = int(input("enter what the current hour is:"))

realhours = hours

while repeat == True:
  seconds+=1 
  if seconds<10:
    print(hours ,minutes ,"0" + str(seconds))
  elif seconds > 9:
    print(hours ,minutes ,seconds)
  time.sleep(1)
  os.system("clear")
  if seconds > 59:
    seconds = 0 
    minutes = minutes + 1
  if minutes > 59:
    minutes = 0
    hours = hours + 1
    realhours = hours
  if hours > 12:
    hours = hours - 12
 
 
