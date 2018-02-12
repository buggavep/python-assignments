# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# # Data Structures
# 
# - String
# - Lists
# - Tuples
# - Dictionaries

# <markdowncell>

# ##Strings
# 
# - A string is a container of characters.
# - Python strings are **immutable**, meaning they cannot change once assigned.

# <codecell>

s = "Hello world, world"
print type(s)

# <markdowncell>

# Length

# <codecell>

print len(s)

# <codecell>

s[0] = 'h'

# <markdowncell>

# Find and replace (notice the immutability).

# <codecell>

s2 = s.replace("world", "python")
s3 = s2.replace("Hello","monty")
print s
print s2
print s3

# <markdowncell>

# Slicing, more on this later

# <codecell>

print s
print s[6:11]

# <codecell>

print s[6:]

# <codecell>

print s[-2:]

# <markdowncell>

# Concatenation

# <codecell>

print s
print s3

# <codecell>

s4 = s + ' ' + s3
print s4

# <markdowncell>

# Find

# <codecell>

print s4.find('world')

# <codecell>

print s4.find('monty')

# <markdowncell>

# Formatting

# <codecell>

print 'A string with value {0} and {1}'.format(10,20.3)

# <markdowncell>

# More string help...

# <codecell>

#help(str)

# <markdowncell>

# ## Lists
# 
# - A list is a container of objects.
# - They do not need to be the same
# - **Mutable**

# <codecell>

values = ['1',2,3.0,False]
print len(values)
print values

# <codecell>

print type(values)

# <markdowncell>

# ### Slicing

# <codecell>

print values
print values[1]

# <codecell>

print values[:3]

# <codecell>

print values[2:]

# <markdowncell>

# ### Append and remove
# 
# - Note: mutability

# <codecell>

l = []
l.append(8)
l.append(10)
l.append(10)
l.append(12)

# <codecell>

print l

# <codecell>

l.remove(10)
print l

# <codecell>

l.remove(l[0]) # Can also say del
print l

# <markdowncell>

# ### Generating lists
# 
# Create a list using the function `range(start,stop,step)`.

# <codecell>

l = range(0,10,2)
print l

# <codecell>

l = range(-5,5)
print l

# <codecell>

line = "This is a    \t list -      \t of strings"
print len(line.split('\t'))
print line.split('\t')

# <markdowncell>

# ### Sorting
# 
# Notice this is modifying the list.

# <codecell>

l = range(-5,5)
print l

l.sort(reverse=True)
print l

# <markdowncell>

# ## Tuples
# 
# - Sequence of objects, like `lists`.
# - But they are **immutable**

# <codecell>

t = (10,40.0,"A")

# <codecell>

print type(t), len(t)

# <codecell>

t[1] = 'B'

# <markdowncell>

# ##Unpacking
# 
# <blockquote>
# A Python favorite!
# </blockquote>

# <markdowncell>

# Unpack the tuple

# <codecell>

print t
x,y,z = t #Unpacking
print z

# <markdowncell>

# Unpack the list.

# <codecell>

print l
A, B = l[:2]
print B

# <markdowncell>

# ## Dictionaries
# 
# - A flexible collection of `{key: value}` pairs.
# - Also called *associative arrays* or *hash maps* in other languages.
# 
# <blockquote>
# Another Python favorite!
# </blockquote>

# <codecell>

data = {}

data['k1'] = True
data['x2'] = 2
data[100] = 3.0

# <codecell>

print data

# <codecell>

print len(data), type(data)

# <markdowncell>

# Add a new entry

# <codecell>

data['k4'] = 100

# <markdowncell>

# ### Example

# <codecell>

data = {'number': 10, 1:'string'}
data['c'] = [1,2,3,4]

# <codecell>

print data

# <codecell>

print data[1]

# <codecell>

print data['c'][3]

# <codecell>

print data['number']

# <markdowncell>

# ### Default values

# <codecell>

print data.get('number',0)

# <codecell>

print data.get('B',0) # The key `B` does not exist

# <codecell>

data['B'] = data.get('B',0) + 100
print data.get('B',0) 

