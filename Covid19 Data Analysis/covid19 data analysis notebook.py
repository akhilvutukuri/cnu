#!/usr/bin/env python
# coding: utf-8

# # Welcome to Covid19 Data Analysis Notebook
# ------------------------------------------

# ### Let's Import the modules 

# In[1]:


import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 
print('Modules are imported.')


# ## Task 2 

# ### Task 2.1: importing covid19 dataset
# importing "Covid19_Confirmed_dataset.csv" from "./Dataset" folder. 
# 

# In[3]:


co=pd.read_csv("Datasets/covid19_Confirmed_dataset.csv")
co.head(5)


# #### Let's check the shape of the dataframe

# In[4]:


co.shape


# ### Task 2.2: Delete the useless columns

# In[10]:


co.drop(["Lat","Long"], axis=1,inplace=True)


# In[11]:





# ### Task 2.3: Aggregating the rows by the country

# In[16]:


co_agg= co.groupby("Country/Region").sum()


# In[17]:


co_agg.head()


# In[ ]:





# ### Task 2.4: Visualizing data related to a country for example China
# visualization always helps for better understanding of our data.

# In[19]:


co_agg.loc["China"].plot()
co_agg.loc["Italy"].plot()
co_agg.loc["India"].plot()
plt.legend()


# ### Task3: Calculating a good measure 
# we need to find a good measure reperestend as a number, describing the spread of the virus in a country. 

# In[20]:


co_agg.loc['China'].plot()


# In[21]:


co_agg.loc['China'][:3].plot() #first three days


# ### task 3.1: caculating the first derivative of the curve

# In[22]:


co_agg.loc['China'].diff().plot()


# ### task 3.2: find maxmimum infection rate for China,Italy,India

# In[24]:


co_agg.loc['China'].diff().max()


# In[25]:


co_agg.loc['Italy'].diff().max()


# In[26]:


co_agg.loc['India'].diff().max()


# ### Task 3.3: find maximum infection rate for all of the countries. 

# In[31]:


Countries=list(co_agg.index)
max_infection_rate=[]
for c in Countries:
    max_infection_rate.append(co_agg.loc[c].diff().max())


# In[34]:


co_agg["Maximum_infected_rate"]= max_infection_rate
co_agg.head()


# ### Task 3.4: create a new dataframe with only needed column 

# In[35]:


corona_data=pd.DataFrame(co_agg["Maximum_infected_rate"])


# In[36]:


corona_data


# ### Task4: 
# - Importing the WorldHappinessReport.csv dataset
# - selecting needed columns for our analysis 
# - join the datasets 
# - calculate the correlations as the result of our analysis

# ### Task 4.1 : importing the dataset

# In[37]:


happiness_report_csv=pd.read_csv("Datasets/worldwide_happiness_report.csv")


# In[38]:


happiness_report_csv.head(5)


# ### Task 4.2: let's drop the useless columns 

# In[41]:


happiness_report_csv.drop(["Overall rank","Score","Generosity","Perceptions of corruption"],axis=1,inplace=True)


# In[43]:


happiness_report_csv.head(5)


# ### Task 4.3: changing the indices of the dataframe

# In[56]:


happiness_report_csv.set_index("Country or region",inplace=True)


# ### Task4.4: now let's join two dataset we have prepared  

# #### Corona Dataset :

# In[50]:


corona_data.head()


# In[52]:


corona_data.shape


# #### wolrd happiness report Dataset :

# In[58]:


happiness_report_csv.head()


# In[59]:


happiness_report_csv.shape


# In[57]:


data=corona_data.join(happiness_report_csv,how="inner")
data.head()


# ### Task 4.5: correlation matrix 

# In[62]:


data.corr()


# ### Task 5: Visualization of the results
# our Analysis is not finished unless we visualize the results in terms figures and graphs so that everyone can understand what you get out of our analysis

# In[63]:


data.head()


# ### Task 5.1: Plotting GDP vs maximum Infection rate

# In[66]:


x=data["GDP per capita"]
y=data["Maximum_infected_rate"]
sns.scatterplot(x,np.log(y))


# In[67]:


sns.regplot(x,np.log(y))


# ### Task 5.2: Plotting Social support vs maximum Infection rate

# In[68]:


x=data["Social support"]
y=data["Maximum_infected_rate"]
sns.scatterplot(x,np.log(y))


# In[69]:


sns.regplot(x,np.log(y))


# ### Task 5.3: Plotting Healthy life expectancy vs maximum Infection rate

# In[70]:


x=data["Healthy life expectancy"]
y=data["Maximum_infected_rate"]
sns.scatterplot(x,np.log(y))


# In[71]:


sns.regplot(x,np.log(y))


# ### Task 5.4: Plotting Freedom to make life choices vs maximum Infection rate

# In[72]:


x=data["Freedom to make life choices"]
y=data["Maximum_infected_rate"]
sns.scatterplot(x,np.log(y))


# In[73]:


sns.regplot(x,np.log(y))

