# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# #Control Flow
# - Indention
# - `if, elif`, and `else`
# - `for` loops
# - `while` loops
# - `exception` handling

# <markdowncell>

# ##Indention
# 
# There are no braces (`{,}`) around blocks of code in Python.  
# 
# - Instead, python uses whitespace
# - Example `if` statement in `C++`
# 
# <code><pre>
# if( value < 0){
#     std::cout << value << std::endl;
# }
# std::cout << "done" << std::endl;
# </pre></code>
# 
# - In python, a colon (`:`) denotes the start of a block.
# 
# <code><pre>
# if value < 0:
#     print value
# print done
# </pre></code>
# 

# <markdowncell>

# ##`if`, `elif`, and `else`

# <codecell>

cash = 1.1
car = 3.1
bus = 2.0
if car < cash:
    print 'Enjoy your car ride'
elif bus < cash:
    print 'Another one rides the bus'
elif cash < 1.00:
    print 'stay home'
else:
    print 'Walking..'

# <markdowncell>

# If nothing `else`, walking.

# <markdowncell>

# ###The `ternary` expression

# <codecell>

action = 'car' if car < cash else 'walking' #one-liner

print action

# <markdowncell>

# ## The `for` loop

# <codecell>

numbers = [1,2,3,4,5]
for i in numbers:
    print i

# <codecell>

for i in range(10,20):
    print i,

# <codecell>

names = ['pat','jonh']
for name in names:
    print name

# <markdowncell>

# ###`continue`
# 
# You can skip part of the remaining block.

# <codecell>

for i in xrange(10):
    print i,
    if i % 2 == 0:
        print 'even'
        continue
    print "---"

# <markdowncell>

# ### `break`
# 
# Stop executing the entire loop.

# <codecell>

for i in xrange(10):
    if i == 5:
        break
    print i

# <markdowncell>

# ## The `while` loop

# <codecell>

count = 0
while (count < 10):
   print count,
   count += 1

# <markdowncell>

# When would you prefer a `while` loop to a `for` loop?

# <markdowncell>

# ##Exceptions
# 
# Gracefully handling errors.

# <codecell>

num = '123.4d'
print float(num)

# <codecell>

try:
    print float(num)
except ValueError, e:
    print e
    print 'This is called Duck Typing'

# <markdowncell>

# ### Multiple exceptions

# <codecell>

def example(values):
    try:
        print float(values)
    except ValueError, e:
        print e
    except TypeError, e:
        print e
        
example(['3','4'])
example('A string?')

# <markdowncell>

# ###`enumerate`
# 
# Sometimes you want the index of a collection and the value.  For example:

# <codecell>

names = ['Deborah','Carla','Mary','Susan']

# <codecell>

index = 0
for name in names:
    print index, names[index], name
    index += 1

# <codecell>

for i, name in enumerate(names):
    print i, name

# <markdowncell>

# ### `sorted`
# 
# - Different than the list method `sort`.
# - A copy of a stored list.

# <codecell>

print sorted(names)

# <codecell>

for name in sorted(names):
    print name,

# <markdowncell>

# ###`reversed`
# - A reverse iterator (e.g. not a list)

# <codecell>

for i in reversed(names):
    print i,

# <codecell>

print list(reversed(names))

# <codecell>

print names

# <markdowncell>

# ###`zip`
# 

# <codecell>

last = ['Smith','Mason','Carter','Dee']
print last
print names

# <codecell>

together = zip(names, last)
print together

# <codecell>

for index, pair in  enumerate(zip(names,last)):
    print index, pair[0], pair[1]

# <markdowncell>

# ### Comprehension
# 
# The Python *consise* expression.

# <codecell>

names.append("Dan")
print names

# <markdowncell>

# Create a list of just names that start with `d`

# <codecell>

dnames = []
for name in names:
    if name.startswith('D'):
        dnames.append(name.lower())
print dnames

# <markdowncell>

# ### List Comprehension: the "Python way"

# <codecell>

dnames = None
dnames = [name.lower() for name in names if name.startswith('D')]

# <codecell>

print dnames

# <markdowncell>

# ### Dictonary `items()`

# <codecell>

d = {'a': 10, 'b': 20, 'c': 30}

# <codecell>

for i in d.keys():
    print i, d[i]

# <codecell>

for k, v in d.items():
    print k, v

# <codecell>

key = "a"
if key in d:
    print "key " + key + " is present in dictionary"

