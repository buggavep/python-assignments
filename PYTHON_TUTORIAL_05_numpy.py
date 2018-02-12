# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# ## `numpy`
# 
# Provides `C`-compiled array-oriented computing in `Python`.
# 
# - **Efficient**
# - **Foundational**
# - Typed,in-memory
# - Contigous and homeogenous
# 
# Usage
# 
# - Scientific data (weather data, satellite data)
# - Image processing
# - Time series
# - Linear algebra

# <codecell>

from IPython.display import display
from IPython.display import Image
from IPython.display import HTML

# <codecell>

import random

N = 100000
A = [0 for i in xrange(N)]
B = [1000.* random.random() for i in xrange(N)]
C = [1000.* random.random() for i in xrange(N)]
d = 0.1

# <codecell>

%%timeit
for i in xrange(N):
    A[i] = B[i] + d * C[i]

# <markdowncell>

# ## The `numpy` solution

# <codecell>

import numpy as np

a = np.array(A)
b = np.array(B)
c = np.array(C)

# <markdowncell>

# Using `numpy` matrix syntax.

# <codecell>

%%timeit
a = b + d*c

# <markdowncell>

# It's about **100x** times faster (~30 milisecond vs ~ 30 microsecond)

# <markdowncell>

# ## Why is `numpy` faster?
# 
# `numpy` 
# 
# - provides a **typed** data structure (`ndarray`)
# - a set of **compiled functions** (`ufuncs`)
# 
# `python`
# 
# - Lists: heterogeneous, **dynamically** typed
# - `for` loops are **interpreted**

# <codecell>

display(Image(filename='/home/CV/Tutorial/img/matrix_multiply_compare.png'))

# <codecell>

##Foundational stack
display(Image(filename='/home/CV/Tutorial/img/foundation.png'))

# <markdowncell>

# ## Outline
# 
# Understand the **`ndarray`** data structure
# 
# Discuss **ufuncs**
# 
# - Array-oriented computing
# - Avoid for loops
# - Use fast algorithms
#    
# Quick note on **slicing** and `numpy` views.
# 
# **Broadcasting**

# <markdowncell>

# ## The `ndarray` object
# 
# Arrays can be created from
# 
# * lists or tuples
# * using functions 
# * reading data from files

# <codecell>

vector = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9 ])
print vector
print type(vector)

# <codecell>

M = np.array([ [1, 2, 3],[4, 5, 6], [7,8,9]], dtype=np.int32)
print M
print type(M)

# <codecell>

### Properties

display(Image(filename='/home/CV/Tutorial/img/array1d.png'))

# <codecell>

print vector.shape
print vector.size
print vector.dtype

# <codecell>

print vector.strides
print vector.ctypes.data

# <codecell>

### Properties

display(Image(filename='/home/CV/Tutorial/img/array2d.png'))

# <codecell>

print M.shape, M.size, M.dtype

# <codecell>

print M.strides, M.ctypes.data

# <markdowncell>

# ### Understanding layout and strides

# <codecell>

A = M.T
print M.shape, M.size, M.dtype
print A.shape, A.size, A.dtype

# <codecell>

print M.strides, M.flags.c_contiguous, M.flags.f_contiguous
print A.strides, A.flags.c_contiguous, A.flags.f_contiguous

# <codecell>

display(Image(filename='/home/CV/Tutorial/img/trans.png'))

# <markdowncell>

# ### Views

# <codecell>

print M.ctypes.data, M.flags.owndata
print A.ctypes.data, A.flags.owndata

# <codecell>

B = A.reshape((A.size,))
print B.flags.owndata
print B

# <codecell>

print B.shape, B.strides

# <markdowncell>

# ### Using array-generating functions
#  
# For larger arrays it is inpractical to initialize the data manually

# <codecell>

print np.arange(1, 6, 0.55)

# <codecell>

print np.linspace(0, 10, 5)

# <codecell>

print np.zeros(4)
print np.ones((4,3))

# <codecell>

print np.diag([1, 2, 3])

# <codecell>

%matplotlib inline
import matplotlib.pyplot as plt

plt.show(plt.hist(np.random.rand(1000)))

# <codecell>

plt.show(plt.hist(np.random.normal(0,1,1000)))

# <markdowncell>

# ## Using `ufuncs`
# 
# - Operate on the elements of one or more `ndarray`
# - Call optimized c loops based on the `dtype`

# <markdowncell>

# ###Unary functions
# 
# Several built-in functions that takes one argument:
# 
#         abs, fabs, sqrt, exp, square, log, ceil, floor
# For example

# <codecell>

x = np.arange(-5.,5.)
print np.square(x)

# <codecell>

print np.abs(x)

# <markdowncell>

# ### Binary functions
#     
#         add, subtract, multiply, divide, power, maximum, minimum, greater, less

# <markdowncell>

# For example

# <codecell>

y = np.square(x)
z = np.add(x,y)
print z
print x + y

# <markdowncell>

# ### Aggregates
# 
#         sum, mean, std, var, min, max, argmin, argmax, cumsum, cumprod

# <markdowncell>

# Examples

# <codecell>

print z.sum(), np.sum(z)

# <codecell>

x = np.random.rand(8).reshape((2,4))
print x.shape

# <codecell>

x.sum(axis=0) # sum the columns

# <codecell>

x.sum(1) # sum the rows

# <markdowncell>

# ### Caution using standard python types

# <codecell>

x = np.random.random(10000)

%timeit np.sum(x)
%timeit sum(x)

# <markdowncell>

# Again, about **100x** slower.

# <markdowncell>

# ### The `accumulate` methods

# <codecell>

np.add.accumulate(x)

# <codecell>

np.cumsum(x)

# <codecell>

np.*.accumulate?

# <markdowncell>

# ### Linear algebra
#     
#         dot, inv, diag, trace, eig, det, qr, svd, solve
#         
# Example matrix multiply

# <codecell>

x = np.random.rand(8).reshape((2,4))
b = np.dot(x,x.T)
print b

# <markdowncell>

# ##Indexing and slicing
# 
# - Index slicing is the technical name for the syntax 
# 
#         container[lower:upper:step]
#     
#     to extract part of an array.
# 
# - We can omit any of the three parameters
# 
#         lower:upper:step

# <markdowncell>

# ###Examples

# <codecell>

x = np.arange(1, 20, 1)
print x

# <codecell>

print x[0:10:1]

# <codecell>

print x[:10]

# <codecell>

print x[:10:2]

# <markdowncell>

# ## 2D slicing

# <codecell>

M = np.array([ [1, 2, 3],[4, 5, 6], [7,8,9]])

# <codecell>

display(Image(filename='/home/CV/Tutorial/img/slice2d.png'))

# <codecell>

print M[0:2]

# <codecell>

print M[:,0:2]

# <codecell>

M = np.array(np.arange(1,17)).reshape((4,4))
print M

# <codecell>

print M[::2, ::2]

# <codecell>

display(Image(filename='/home/CV/Tutorial/img/slice2deven.png'))

# <markdowncell>

# ### Filtering

# <codecell>

print x > 10

# <codecell>

y = x[x>10]
print y

# <codecell>

mask = (5 < x) * (x < 10)
print mask

# <codecell>

print x[mask]

# <markdowncell>

# ##Broadcasting
# 
# Arithmetic between `array`s of different, but compatible, shapes.

# <codecell>

print np.arange(5) + 1

# <codecell>

display(Image(filename='/home/CV/Tutorial/img/broad_simple.png'))

# <codecell>

A = np.arange(8).reshape(4,2)
B = np.arange(2)

print A.shape, B.shape

# <codecell>

A + B

# <codecell>

display(Image(filename='/home/CV/Tutorial/img/broad2d.png'))

# <markdowncell>

# ### Example
# 
# Find the distance from the mean of the set to every point?

# <codecell>

a = np.random.randn(400,2)
m = a.mean(0)
plt.plot(a[:,0], a[:,1], 'o', markersize=6, alpha=0.5)
plt.plot(m[0], m[1], 'ro', markersize=10)
plt.show()

# <markdowncell>

# Euclidean distance
# 
# $$d = \sqrt{ \sum (x_i - y_i)^2 }$$

# <codecell>

sq = np.square(a - m)
print sq.shape, a.shape, m.shape

# <markdowncell>

# The mean `a.mean(0)` was broadcast to every row in our matrix `a`.  Now we compute the column sum of `sq`.

# <codecell>

ssq = sq.sum(axis=1)
print ssq.shape

# <markdowncell>

# Now take the `sqrt`.

# <codecell>

dist = np.sqrt(ssq)
print dist.shape

# <codecell>

plt.show(plt.hist(dist))

# <codecell>

print a.mean()

# <codecell>

a.shape

# <codecell>

a.mean(0).shape

# <codecell>

a.mean(1).shape

