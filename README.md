# How To Install Python 2.7 Anaconda

We suggest installing Anaconda. Installation of Python using Anaconda is local and does not require administrator rights.<br>
The graphical installer for Windows, MacOS, or Linux is [here](https://www.anaconda.com/download/).

Choose your operating system and download the Anaconda installer for Python 2.7 version.<br>


Then, for Windows and MacOS, double click the installer to launch and simply follow the instructions.<br>


For Linux, open a terminal window and enter the following to install Anaconda for Python 2.7: <br>
bash ~/Downloads/Anaconda2-4.4.0-Linux-x86_64.sh

This installation includes Jupyter and Python 2.7. 


<br>


Now, we will need to install some Python libraries in order to be ready for the workshop. <br>
To do so, please open a terminal window if you are working with MacOS or Linux. <br>

For those that are working with Windows, you can go to Windows Start menu located in the lower left portion of the desktop and search for ‘Command Prompt’ in the search box located at the bottom of the menu. <br>
Only for Windows users, before installing anything, we have to write the following command into the ‘Command Prompt’:<br>
conda config --add channels conda-forge<br>

This way, we can use the fowlling command in order to install the packages we need:<br> 
conda install PACKAGENAME.<br>

Here is the list of libraries we need :<br>
-keras<br> that will automatically install theano, and <br>
-tensorflow

For example, type the command: conda install keras <br>
and you will probably need to answer by "y" to a question about updating or installing other related libraries that will be suggested to you.

You can now open a Jupyter notebook to get started with the following command: jupyter-notebook

<br>

For those that want to work later on different Python platforms more adapted to your work, you can refer to: <br>
1. [Sublime](http://www.sublimetext.com/), 
2. [Pycharm](https://www.jetbrains.com/pycharm/), and
3. [Rodeo](http://rodeo.yhat.com/). 

You also may use [online jupyter](https://try.jupyter.org) if you do basic operations and you do not require large data handling.

# Sublime
Sublime can be used to program many different languages. We suggest installing [sublime](http://www.sublimetext.com) text editor which includes Python highlighting and many others. You must configure the sublime editor first. 
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

Save "untitled.sublime-build" as "conda.sublime-build" and always use this build to run your python codes. Sublime configuration may vary a bit in "path" if you use Linux, Mac, or Windows system. For Windows system sublime configuration might become tricky. 

```
{
	"cmd": ["python", "-u", "$file"],
	"file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
	"path": "c:\\myconda", "selector": "source.python"
}
```

In the case that you cannot configure your sublime text editor, try using browser-based Python by typing "jupyter notebook" in the command line.


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







