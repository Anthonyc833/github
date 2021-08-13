import string
import random
from random import *
characters = string.ascii_letters + string.punctuation  + string.digits
plenght = input("how long is the password")
Upperletters = input("do you want upper case")
Lowerletters=input("do you want lower case letters")
digits=input("any numbers in that")
characters2=input("special characters")
if Upperletters == "Y":
  UL="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
else:
  UL=""
if Lowerletters == "Y":
  LL= "abcdefghijklmnopqrstuvwxyz"
else:
  LL=""



if int(plenght) < 0:
  print("you cant print that")
elif int(plenght) > 50:
  print("thats to big")
else:
  password =  "".join(choice(characters) for x in range(int(plenght)))
  print (password)
