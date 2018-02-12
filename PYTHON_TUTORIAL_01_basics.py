# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# # The Basics

# <markdowncell>

# ## Python Files
# * **Extension:** files end in `.py`
#     - Not strictly required
#     - e.g. `script.py`
# * **Execution:**
#     - CANOPY: play button
#     - IPython: `run script.py`
#     - Python terminal: `python script.py`

# <markdowncell>

# ## The `import` Statement
# - Python is made up of several modules. 
# - Before you can use a module, you must `import` it.

# <codecell>

import math

# <markdowncell>

# Gives access to all functions and objects in the `math` module.

# <codecell>

print math.pi

# <codecell>

print math.cos(10)

# <markdowncell>

# The prefix is helpful in avoiding name collision.

# <markdowncell>

# ## Alternative `import`s
# Import all symbols so we no longer need the `math` prefix

# <codecell>

from math import *

print pi

# <markdowncell>

# Import select symbols

# <codecell>

ani
from math import pi, cos

myvar = 1.4
print cos(myvar)

# <markdowncell>

# ## What is available?

# <codecell>

print dir(math)

# <codecell>

help(math.pow)

# <markdowncell>

# Common imports:

# <codecell>

import os, sys, math, shutil, re, subprocess

# <markdowncell>

# ## Comments

# <markdowncell>

# Every line of text in your file is considered python code uless it is preceeded by a `#` sign

# <codecell>

# This is a comment
# It's ignored by the python interpreter

print(cos(pi)) # this is also ignored

# <markdowncell>

# ## Variables

# <markdowncell>

# - Variable names in Python can contain:
#     - alphanumerical characters a-z, A-Z, 0-9
#     - Undescore _
# - Cannot be a `keyword`
#     
#         and, as, assert, break, class, continue, def, del, elif, else, except, 
#         exec, finally, for, from, global, if, import, in, is, lambda, not, or,
#         pass, print, raise, return, try, while, with, yield
#         
# - Convension: names start with
#     - lowercase for variables
#     - Uppercase for objects
#     
# - The `=` character is assignment

# <codecell>

x87_ = 10
print x87_

# <markdowncell>

# ## Data types

# <markdowncell>

# In a **dynamically typed** language, the type is determined at assigment.

# <codecell>

a = 2
b = 1e9
c = False
d = "A string"

# <codecell>

print type(a)
print type(b)
print type(c)
print type(d)

# <markdowncell>

# ##Type casting

# <codecell>

print a,b,c,d

# <codecell>

print float(a)
print int(2.6)
print str(c)

# <codecell>

print d, float(d)

# <codecell>

print float("24")

# <markdowncell>

# ##`None`
# 
# This is the null value type in Python.

# <codecell>

value = None
print value

# <markdowncell>

# ## Example: Scientific Hello World

# <codecell>

import math
r = float("4.2")
s = math.sin(r)
print "hello world! The sin(" +  str(r) + ") =", s

# <markdowncell>

# - cast "4.2" to a `float`
# - String concatentation `+`

