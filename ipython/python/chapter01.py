
# coding: utf-8

# #How To Install Python 2.7 Anaconda
# 
# We suggest installing Anaconda. Installation of Python using Anaconda is local and does not require administrator rights. The graphical installer for Windows, Mac, or Linux is [here](http://continuum.io/downloads) the Anaconda quickstart  pdf file is available [here](https://store.continuum.io/static/img/Anaconda-Quickstart.pdf).
# 
# 

# 
# # Python IDE
# We suggest installing [sublime](http://www.sublimetext.com) text editor which includes Python highlighting. You must configure the sublime editor first. 
# 1- Run sublime
# 2- Tools/Build System/New Build System 
# 3- 
# Go to 
# 
# ```
# {
#      "cmd": ["python2.7", "$file"],
#      "path": "User/username/anaconda/bin:$PATH",
#      "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
#      "selector": "source.python"  
#  }
# ```
# 
# Save "untitled.sublime-build" as "conda.sublime-build" and always use this build to run your python codes. Sublime configuration may vary a bit in "path" if you use Linux, Mac, or Windows system. For Windows system sublime configuration might become tricky. The 
# 
# ```
# {
# 	"cmd": ["python", "-u", "$file"],
# 	"file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
# 	"path": "c:\\myconda", "selector": "source.python"
# }
# ```
# 
# In the case that you cannot configure your sublime text editor, try using browser-based Python by typing "ipython notebook" in the command line.
# 

# 
# 
# #Introduction to Python
# Start testing your python by printing basic operations on numbers
# 
# 
# 

# In[116]:

print "Hello World!"


# In[117]:

print 2+2


# We start with some examples from [LearnPython](http://www.learnpython.org)

# **Variable Types**
# 
# You are automatically defining a variable type while initializing the variable such as

# In[118]:

myint = 7
myfloat1 = 7.0; myfloat2 = float(7)


# You may separate commands using ";"

# In[119]:

print myint/2; print myfloat1/2; print myfloat2*2; print myfloat2**2


# In[120]:

print myfloat1


# In[121]:

mystring1 = 'Hello'
mystring2 = "World"
mystring12 = mystring1+" "+mystring2+"!"


# You may define strings differently, and attach them using "+". You can remove a variable from the memory when you do not need, using "del"

# In[122]:

del mystring1, mystring2;


# In[123]:

print mystring12


# In[124]:

print mystring12[-1]


# In[125]:

print len(mystring12)


# In[126]:

print mystring12[0:-1]


# In[127]:

print mystring12[:]


# **Lists**
# 
# List a special case of array, except they can include variables with different types. You can easily append, delete, merge, different lists. You can even exchange the index number with a a string as a name. List is one of the most useful objects in Python.

# Index in list starts from zero unlike R. A string is actually a list. -1 shows the end of the list but the last. Range of indices is like [start, end[ so you do not get access to the last element.

# In[128]:

mylist = [1,2,3]


# In[129]:

print mylist[0]


# Here is a simple example that shows how a list is different with an array.
# 

# In[130]:

mylist=[1,2,3,"2", "HelloWorld", [1,2,3] ]


# In[131]:

print mylist


# In[132]:

print mylist[-1]*3


# The "zip" function pairs several lists of the same size.
# 
# ## Exercise
# Make two lists. First, a list of 4 of your best friends' first name. Second, a list of their family name. Then print their first name and last name.
# 

# In[133]:

firstname= ["John","Bruno", "Alan","Ali"]
lastname=["Smith", "Agard", "Turing","Bendavid"]


# In[134]:

print firstname


# In[135]:

print lastname 


# In[136]:

print zip(firstname,lastname,)


# You may insert several other elements to the list using "append", "insert", "index" and several others. See below for for more details
# 
# ```python
# list.append(x)
# ```
# Add an item to the end of the list; equivalent to a[len(a):] = [x].
# 
# ```python
# list.extend(L)
# ```
# Extend the list by appending all the items in the given list; equivalent to a[len(a):] = L.
# 
# ```python
# list.insert(i, x)
# ```
# Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).
# 
# ```python
# list.remove(x)
# ```
# Remove the first item from the list whose value is x. It is an error if there is no such item.
# 
# ```python
# list.pop([i])
# ```
# Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)
# 
# ```python
# list.index(x)
# ```
# Return the index in the list of the first item whose value is x. It is an error if there is no such item.
# 
# ```python
# list.count(x)
# ```
# Return the number of times x appears in the list.
# 
# ```python
# list.sort(cmp=None, key=None, reverse=False)
# ```
# Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).
# 
# ```python
# list.reverse()
# ```
# 
# Reverse the elements of the list, in place.

# ##Exercise
# Add you new friend: 1) As the first element, 2) as the last element, 3) in the middle.
# 
# 
# 

# In[137]:

firstname.insert(2,"Martin")
print firstname 


# In[138]:

lastname.insert(2,"Trepanier")
print lastname


# # Conditions 
# Python uses boolean variables to evaluate conditions. Tab separates different code blocks, therefore there is no need for brackets.
# 

# In[139]:

x = 2
print x == 2 
print x<2
not x<2


# In[140]:

if x==2:
    print "x equals to two"
else:
        print "print x differs from two"


# In[141]:

if "John" in firstname:
    print "John is in the list"


# # For Loop
# The "for" loops iterate over a given sequence. 

# In[142]:

for i in range(len(firstname)):
    print firstname[i]


# In[143]:

for name in firstname:
    print name


# ## Exercise
# Create a new list in the form of firstname_lastname of your 5 friends.

# In[144]:

first_last=[""]*len(firstname)
for i in range(len(firstname)):
    first_last[i]=firstname[i]+"_"+lastname[i]
print first_last


# In[145]:

for name, family in zip (firstname, lastname):
    firstlast=name+"_"+family


# The "range" function is a very useful command in loops.

# In[146]:

print range(6)


# In[147]:

print range(2,6)


# In[148]:

print range(2,14,4)


# # Function definition
# The "def" command, can be used to define a function.

# In[149]:

def sq(x):
    return x**2
print sq(4)


# ## Exercise 
# Define a function that gives the square of a list elements.
# 

# In[150]:

def sqlist1(X):
    return [sq(x) for x in X]


# In[151]:

sqlist1(range(6))


# In[153]:

def sqlist2(X):
    Y=[0]*len(X)
    for i in range(len(X)): 
        Y[i]=sq(X[i])
    return Y


# In[154]:

sqlist2(range(6))

