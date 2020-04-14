#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd

df = pd.read_csv (r'https://jobs.github.com/positions.json?description=python&location=new+york.csv')
print (df)


# In[20]:


df.columns


# In[21]:


df.head( )


# In[31]:


import pandas as pd
import mysql
import xlrd
data = pd.read_excel (r'D:\dataextraction\data.xlsx') 
df = pd.DataFrame(data, columns= ['id','type','url','created_at','company','company_url','location','title','description','experience','framework such as','Required skills','knowledge and Abilities','how_to_apply','company_logo'])
print (df)


# In[ ]:




