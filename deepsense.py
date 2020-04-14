#!/usr/bin/env python
# coding: utf-8

# In[38]:


import pandas as pd
import io
import reques
url ="https://jobs.github.com/positions.json?description=python&location=new+york.csv"
read_data = requests.get(url).content
read_data


# In[44]:


address=pd.read_csv(io.StringIO(read_data.decode('utf-8')))
address.head()


# In[42]:


address.columns


# In[ ]:




