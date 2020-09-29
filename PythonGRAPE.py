"""
=======
P P P P      G G G G G G
P       P  G
P       P  G
P P P P    G       G G
P          G           G 
P          G           G 
P          G           G
P            G G G G G G
 \
   \
    |
  o o o o 
o         o
o         o
o         o
o         o
  o o o o
=======
Version 1.0.1
-Python Grape-
A simple python module.

==Example==
from PythonGRAPE import *
var = ["banana", "apple"]
print(read(var, 1))
==Credits==
By Daniel4-Scratch

"""

import warnings, random


# Functions
def square_turtle(radius):
  pendown()
  for i in range(4):
    forward(radius)
    left(90)
  penup()
  
def read(var, number):
  return var[number]
