#!/usr/bin/env python
# coding: utf-8

# In[28]:


import pandas as pd 


# In[29]:


import matplotlib.pyplot as plt 


# In[30]:


url = "time_series_19-covid-Confirmed_archived_0325.csv"


# In[31]:


df= pd.read_csv(url)


# In[32]:


df.head(2)


# In[33]:


print (f"Shape: {df.shape}")


# In[34]:


cases_worldwide = df.iloc[:, 4:].sum(axis=0)
cases_worldwide.index = pd.to_datetime(cases_worldwide.index)


# In[35]:


print (cases_worldwide)


# In[36]:


plt.figure(figsize=(10,5))
plt.plot(cases_worldwide.index, cases_worldwide.values)
plt.title("Worldwide Confirmed COVID-19 Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Number of Cases")
plt.show()


# In[37]:


import pandas as pd
import matplotlib.pyplot as plt

# Load the data
url_new = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
dff = pd.read_csv(url)

# Group by Country and sum across provinces/states
df_country = dff.drop(columns=["Province/State", "Lat", "Long"])
df_country = df_country.groupby("Country/Region").sum()

# Transpose so dates become rows (index) and countries become columns
df_country = df_country.transpose()

# Convert index to datetime
df_country.index = pd.to_datetime(df_country.index)

# View the first few rows
print(df_country.head())


# In[38]:


# Get the top 5 countries by the most recent date
latest_totals = df_country.iloc[-1]
top_5_countries = latest_totals.sort_values(ascending=False).head(5).index

# Plot
plt.figure(figsize=(12, 6))
for country in top_5_countries:
    plt.plot(df_country.index, df_country[country], label=country)

plt.title("Top 5 Countries - COVID-19 Confirmed Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Confirmed Cases")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




