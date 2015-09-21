#How To Install Python 2.7 Anaconda

We suggest installing Anaconda. Installation of Python using Anaconda is local and does not require administrator rights. The graphical installer for Windows, Mac, or Linux is [here](http://continuum.io/downloads) the Anaconda quickstart  pdf file is available [here](https://store.continuum.io/static/img/Anaconda-Quickstart.pdf).


# Python IDE
We suggest installing [sublime](http://www.sublimetext.com) text editor which includes Python highlighting. You must configure the sublime editor first. 
1- Run sublime
2- Tools/Build System/New Build System 
3- 
Go to 

```
{
     "cmd": ["python2.7", "$file"],
     "path": "User/username/anaconda/bin:$PATH",
     "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
     "selector": "source.python"  
 }
```

Save "untitled.sublime-build" as "conda.sublime-build" and always use this build to run your python codes. Sublime configuration may vary a bit in "path" if you use Linux, Mac, or Windows system. For Windows system sublime configuration might become tricky. The 

```
{
	"cmd": ["python", "-u", "$file"],
	"file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
	"path": "c:\\myconda", "selector": "source.python"
}
```

In the case that you cannot configure your sublime text editor, try using browser-based Python by typing "ipython notebook" in the command line.


#Introduction to Python
Start testing your python by printing basic operations on numbers

**Numbers in Python**
Show $\beta$

```python
print "Hello World!"
Hello World!
print 2+2
    4
```







