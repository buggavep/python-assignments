# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# # The Procedural Python
# 
# - Imperative programming
# - Organization steps
# - Avoid cut-paste!
# 
# Outline:
# 
# - Definition
# - Arguments
# - Return types

# <markdowncell>

# ## Definition

# <codecell>

def my_function():
    names = ['joe','nate']
    for k in names:
        print k

# <codecell>

my_function()

# <markdowncell>

# - The `pass` keyword is the Python "do nothing" command.
# - Very common for defining, but not implementing, functions.

# <markdowncell>

# ## Arguments
# 
# These are **positional** arguments

# <codecell>

def my_function(a,b,c):
    print a,b,c

my_function(2,7,6)

# <markdowncell>

# In this example, the variables are **named arguments**.

# <codecell>

def my_function(a,b,c=100):
    print a,b,c
    
my_function(c=2,b=4,a=50)

# <codecell>

my_function(a=2,b=4)

# <markdowncell>

# ### Why not pass a dictionary as inputs? `**kwargs`
# 
# - source: [stackoverflow](http://stackoverflow.com/questions/1769403/understanding-kwargs-in-python)
# - `kwargs` is a dict of the keyword args passed to the function

# <codecell>

def print_keyword_args(**kwargs):
    for key, value in kwargs.iteritems():
        print key, value

# <codecell>

print_keyword_args(a=20,b=30)

# <codecell>

print_keyword_args(a=20,b=30,c=100)

# <markdowncell>

# ### `*args`
# 
# Passing an arbitrary number of arguments to your function

# <codecell>

def print_args(*args):
    for index, value in enumerate(args):
        print index, value

# <codecell>

print_args(10,20,40)

# <codecell>

print_args(10,20)

# <markdowncell>

# ### Combination

# <codecell>

def print_all(pos, *args, **kwargs):
    print "pos", pos
    
    for index, value in enumerate(args):
        print 'args', index, value
        
    for key, value in kwargs.iteritems():
        print 'kwargs', key, value

# <codecell>

print_all("positional",10,20,30,a=40,b=50)

# <markdowncell>

# ## Returning values

# <codecell>

def my_function(a,b,c=100):
    if c  == 100:
        return a+b+c
    else:
        return a+b

# <codecell>

value = my_function(10,10)
print value

# <codecell>

value = my_function(1,1,10)
print value

# <markdowncell>

# ### Using a `tuple`

# <codecell>

def my_function():
    a = 10
    b = 20.0
    c = "string"
    return a, b, c

# <markdowncell>

# Results as a `tuple`.

# <codecell>

print my_function()

# <markdowncell>

# Results as individual variables

# <codecell>

x,y,z = my_function()
print x,y,z

# <markdowncell>

# ### Multiple values with a dictionary

# <codecell>

def my_function():
    a = 10
    b = 20.0
    c = "string"
    return {'a': a, 'b': b, 'c': c}

# <codecell>

values = my_function()
print values['a']

