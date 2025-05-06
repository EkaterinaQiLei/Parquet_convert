#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os 
import glob


# In[2]:


files = glob.glob("parquet/*.parquet")
out_csv = pd.DataFrame()
files


# In[3]:


i = 0
for file in files:
    fl = pd.read_parquet(file)
    out_csv = pd.concat([out_csv, fl])
    i+=1
    print(f"{i} of {len(files)}")
        
out_csv.to_csv("parquet_to_csv.csv", index=False)
out_csv.to_excel("parquet_to_excel.xlsx", index=False)

