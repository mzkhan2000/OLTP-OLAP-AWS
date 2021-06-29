#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import re, string # using to remove regular expression, special characters in the csv files/ -Monir


# In[9]:


# importing csv files to the repositery as data frames/ -Monir
monir_df_order = pd.read_csv("ffa_order.csv")


# In[10]:


monir_df_order.head()


# In[13]:


monir_df_order['start_date'] = pd.to_datetime(monir_df_order['start_date'])


# In[ ]:


monir_df_order['end_date'] = pd.to_datetime(monir_df_order['end_date'])


# In[16]:


monir_df_order['calendar_quarter'] = monir_df_order['start_date'].dt.quarter


# In[19]:


monir_df_order['calendar_year'] = monir_df_order['start_date'].dt.year


# In[21]:


monir_df_order['calendar_month'] = monir_df_order['start_date'].dt.month


# In[24]:


monir_df_order.head()


# In[6]:


monir_df_order['project_id'].isnull().sum()


# In[7]:


monir_df_order.isnull().sum()


# In[25]:


monir_df_order.to_csv("ffa_order_new.csv") # Saving as csv file/ Monir 


# In[26]:


monir_df_project = pd.read_csv("ffa_project.csv")


# In[27]:


monir_df_project.head()


# In[28]:


monir_df_project['start_date'] = pd.to_datetime(monir_df_project['start_date'])


# In[29]:


monir_df_project['end_date'] = pd.to_datetime(monir_df_project['end_date'])


# In[30]:


monir_df_project['project_duration'] =  monir_df_project['end_date'] - monir_df_project['start_date']


# In[31]:


monir_df_project.head()


# In[33]:


monir_df_project.isnull().sum()


# In[32]:


monir_df_project.to_csv("ffa_project_new.csv") # Saving as csv file/ Monir 


# In[ ]:




