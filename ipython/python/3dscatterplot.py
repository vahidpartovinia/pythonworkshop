
# coding: utf-8

# In[4]:

import numpy as np
zipdata=np.loadtxt("../data/zip.train")
from sklearn.decomposition import PCA
from sklearn.lda import LDA
import matplotlib.pyplot as plt

x=zipdata[:,1:]
y=zipdata[:,0]

lda=LDA(n_components=3)
zipdata_lda=lda.fit(x,y).transform(x)
from mpl_toolkits.mplot3d import Axes3D
fig=plt.figure()
ax=Axes3D(fig)
ax.scatter(zipdata_lda[y==5,0],zipdata_lda[y==5,1],zipdata_lda[y==5,2],edgecolor="r")
ax.scatter(zipdata_lda[y==2,0],zipdata_lda[y==2,1],zipdata_lda[y==2,2],edgecolor="b")
plt.show()


# In[ ]:



