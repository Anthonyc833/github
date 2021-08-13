import string
import random
from random import *
characters = string.ascii_letters + string.punctuation  + string.digits
plenght = (int("how long is the password"))
if plenght == 0:
  print("you cant print that")
else if plenght < 50:
  print("thats to big")
else:
  password =  "".join(choice(characters) for x in range(plenght))



print (password)
