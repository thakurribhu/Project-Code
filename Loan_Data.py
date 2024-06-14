#!/usr/bin/env python
# coding: utf-8

# In[28]:


# Q1. Read the dataset.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[29]:


# Q2. Describe the dataset.
df=pd.read_csv("loan_data_set.csv")


# In[3]:


df


# In[16]:


df.describe(include = 'all')


# In[17]:


# Q3(1). Find mean,median and mode of columns.
df.mean()


# In[18]:


# Q3(2) Find mean,median and mode of columns.
df.median()


# In[19]:


# Q3(3). Find mean,median and mode of columns. 
df.mode()


# In[20]:


# Q4. Find the distribution of columns with numerical data. Evaluate if they are normal or not.
# Numeric Dataset and these features are normal
numeric = list(df._get_numeric_data().columns)
numeric


# In[22]:


# Q4. Find the distribution of columns with numerical data. Evaluate if they are normal or not.
# Ordinal columns
# columns which are not normal are ordinal
categorical = list(set(df.columns) - set(df._get_numeric_data().columns))
categorical


# In[23]:


df.plot.hist()


# In[24]:


df.plot.hist()


# In[25]:


# Q8(1). Compare different columns of dataset
comparison_column = np.where(df["ApplicantIncome"] == df["CoapplicantIncome"], True, False)
df["equal"] = comparison_column
df


# In[26]:


# Q8(1). Compare different columns of dataset
comparison_column = np.where(df["ApplicantIncome"] == df["CoapplicantIncome"], True, False)
df["equal"] = comparison_column
df


# In[ ]:




