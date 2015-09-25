
# coding: utf-8

# # Introduction to arrays in numpy 
# The "numpy" is the efficient numerical computation library of python. We start with defining arrays and their basic manipulation. Arrays are like lists except their type is fixed for each element. The common types are `int` and `float`.
# We start with a one dimensional array of size 3.
# 
# 
# 

# In[1]:

import numpy as np

a = np.array([1, 2, 3])  
print type(a)            
print a.shape            
print a                  


# Now we define a two-dimensional array of size 2$\times$3

# In[2]:

b = np.array([[1,2,3],[4,5,6]])   
print b.shape                     
print b[1, :]


# Any time you need help you can write "numpy.array?", you may initialize a matrix using "numpy.full"

# In[3]:

print np.full((2,3),7)


# This initializes a 2$\times$3 with value float 7.0. try other functions like `numpy.zeros`, `numpy.ones`, and `numpy.eye`

# ## Boolean array indexing 
# Using the boolean array indexing you pick up the elements of an array. This type of indexing helps you to select the elements of an array that satisfy a condition. You must be aware that arrays in numpy is different from lists in python. However, we can convert a numeric list to a numpy array using `np.array`

# In[4]:

import numpy as np
a = np.array([[1,2], [3, 4], [5, 6]])
print (a > 2)
print a[a>2]


# ## Exercise
# Produce an identity matrix of size 10 and replace the diagonal elements with 1 to 10. 
# 

# In[5]:

myarray=np.eye(10)
myarray[myarray==1]=range(1,len(myarray)+1)
print myarray


# Replace the non-zero elements of the last matrix with increasing powers of 2.

# In[6]:

np.set_printoptions(suppress=True)
print (2**myarray)-1



# ## Matrix operations
# ###Elementwise operation
# Element-wise matrix operations are as follows
# Take 
# 
# $x=\left(\begin{array}{c c} 1&2\\3&4 \end{array}\right) ~~~~$ 
# $y=\left(\begin{array}{c c} 5&6\\7&8 \end{array}\right)$

# In[7]:

x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)
print x + y
print np.add(x, y)


# In[8]:

print x - y
print np.subtract(x, y)


# In[9]:

print x * y
print np.multiply(x, y)


# In[10]:

print x / y
print np.divide(x, y)


# ### Dot product
# Matrix product is the "dot operator. It can be used with only one, or two arguments

# In[11]:

print x.dot(y)
print np.dot(x,y)


# ###Matrix sum
# The sum of a matrix can be implemented on rows, on columns, or on the total matrix. 

# In[12]:

print np.sum(x, axis=1) # on rows 
print np.sum(x, axis=0) # on columns
print np.sum(x)  # on both



# ### Matrix transpose
# The function for transposing a matrix is .T

# In[13]:

print x.T
print np.sum(x.T,axis=0) # gives sum over rows (and not columns even with axis=0)


# ### Repeating a matrix
# repeating a matrix several times on rows and columns. This is a special case of the kronecker product

# In[14]:

print np.tile(x,(2,3))


# ### Reshaping a matrix

# In[15]:

print np.reshape(range(10),(2,5) )


# In[16]:

print np.reshape(range(10),(5,2) )


# Now we lets use some image libraries and plot some pictures.
# 

# In[17]:

import matplotlib.pylab as plt
get_ipython().magic(u'matplotlib inline')
#url=http://cs231n.github.io/assets/cat.jpg
img = plt.imread('../data/cat.jpg')
img_tinted = img * [0, 1, 0]
plt.imshow(img_tinted)
plt.axis("off")


# In[18]:

img_tinted = img * [.27, .72, 0.07]
plt.imshow(np.sum(img_tinted, axis=2), "gray")
plt.axis("off")

