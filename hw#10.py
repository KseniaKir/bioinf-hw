#!/usr/bin/env python
# coding: utf-8

# In[5]:


#4
from scipy.stats  import t, norm
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

def variab(a):
    rv = t(1)
    arr = []
    for i in range (1000):
        sample = rv.rvs(size=a)
        s = np.mean(sample)
        arr.append(s)
    return arr

rv2 = t(1)
nums = [0]*1000
x=-3
for i in range (1000):
    nums[i]=x+0.006
    x+=0.006
df_d = pd.DataFrame({"x": nums})
df_d["PDF"] = rv2.pdf(df_d["x"])

def plots(a):
    sns.histplot(x=a, stat="density")
    sns.lineplot(data=df_d, x="x", y="PDF")
    plt.xlim(-5, 5)
    return plt.tight_layout()

arr2 = variab(2)
plots(arr2)


# In[2]:


arr5 = variab(5)
plots(arr5)


# In[ ]:


arr14 = variab(14)
plots(arr14)


# In[ ]:


arr100 = variab(100) 
plots(arr100)


# In[4]:


#5
from scipy.stats  import t, norm
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

rv = t(3)
n = 14 # = 2, =5, = 100
arr = []
for i in range (1000):
    sample = rv.rvs(size=n)
    s = np.mean(sample)
    arr.append(s)

sns.histplot(x=arr, stat="density")

nums = [0]*1000
x=-3
for i in range (1000):
    nums[i]=x+0.006
    x+=0.006
rv2 = norm(0, 1)
df_d = pd.DataFrame({"x": nums})
df_d["PDF"] = rv2.pdf(df_d["x"]) 

sns.lineplot(data=df_d, x="x", y="PDF")
plt.xlim(-5, 5)
plt.tight_layout()


# In[ ]:




