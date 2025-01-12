#!/usr/bin/env python
# coding: utf-8

# In[92]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[ ]:


# This is our raw data.


# In[93]:


df1=pd.read_csv(r"C:\Users\Priya Tripathi\OneDrive\Desktop\dataset_1 - dataset_1.csv")
df1


# In[94]:


df1.drop('yr',axis=1,inplace=True)
df1


# In[95]:


df1.isnull().any()


# This is the function which has been used to find any null value in the data.


# In[ ]:


# Data sheet 1 has Zero null value and no duplicate values so, we can say that datasheet 1 have been cleaned.


# In[96]:


df2=pd.read_csv(r"C:\Users\Priya Tripathi\OneDrive\Desktop\dataset_2.xlsx - dataset_2.csv")


# In[97]:


df2


# In[98]:


df2.drop('Unnamed: 0',axis=1,inplace=True)
df2


# In[ ]:


# as we can say that in datasheet 2 has 11 null values on atemp, we have to replace by median and place it over null value.


# In[99]:


df2.isnull().sum()


# In[100]:


mdn=df2["atemp"].median()

mdn


# In[101]:


df2["atemp"] = df2["atemp"].replace(np.nan,0.197)
df2["atemp"]


# In[102]:


df2.isnull().sum()


# # Datasheet 1 and datasheet 2 being merged after cleaning datasheet 1 & datasheet 2

# In[103]:


merged =pd.merge(df1,df2,on='instant',how ='inner')


# In[104]:


merged


# In[105]:


df3=pd.read_csv(r"C:\Users\Priya Tripathi\OneDrive\Desktop\dataset_3 - dataset_3.csv")
df3


# In[106]:


df3.drop('yr',axis=1,inplace=True)
df3


# In[107]:


df3.isnull().sum()


# # After merging the datasheet 1 & 2 we will concat with datasheet 3 after cleaning all three of them.

# In[108]:


Final_data = pd.concat([merged,df3],ignore_index=True,sort=False)
Final_data


# In[109]:


Final_data.isnull().sum()


# In[110]:


Final_data.plot(x="mnth",y="temp",kind="hist");
plt.title("temp vs mnth")
plt.xlabel("mnth")
plt.ylabel("temp")
plt.show()


# In[111]:


sns.lineplot(Final_data,x="mnth",y="hum")
plt.title("Humidity vs Month")


# In[112]:


# This data shows exponential growth between month & Humidity it also reflect this data is a form of uniform motion.


# In[113]:


# data visualization through heatmap


# In[114]:


Final_data=Final_data.rename(columns={"hum":"humudity","cnt":"count","dteday":"day","mnth":"month","weathersit":"weather_situation","temp":"temperature","hr":"Hour"})
Final_data


# In[115]:


Final_data.plot(x="Hour",y="humudity",kind="scatter",color="green")
plt.title("Hour vs humudity",fontsize=22)
plt.show()


# In[116]:


import warnings
warnings.filterwarnings('ignore')
# warning removal code


sns.distplot(Final_data["season"])
#there is no outlier in the season column


# In[117]:


# As we can see there is no skwed on normal distribution on the column season so, we can say that there is no need to find any outlier over in this column.


# In[118]:


# now working on second column
import warnings
warnings.filterwarnings('ignore')
# warning removal code


sns.distplot(Final_data["month"])


# In[119]:


# We detected outlier through Z score and did capping over it.


# In[120]:


sns.boxplot(Final_data["weekday"])


# In[121]:


# As we can see there is no outlier in the column weekdays, so we don't need to find outlier over this column.


# In[122]:


sns.boxplot(Final_data["weather_situation"])


# In[123]:


# data before outlier 


# In[124]:


Q1=Final_data["weather_situation"].quantile(.25)
Q3=Final_data["weather_situation"].quantile(.75)
print(Q3,Q1)
IQR=Q3-Q1
print("IQR",IQR)
upper_value=Q3+1.5*IQR
lower_value=Q1-1.5*IQR
print("upper limit", upper_value, "lower_limit",lower_value)


# In[125]:


Final_data["weather_situation"]=np.where(Final_data["weather_situation"]>upper_value,upper_value,np.where(Final_data["weather_situation"]<lower_value,lower_value,Final_data["weather_situation"]))


# In[126]:


sns.boxplot(Final_data["weather_situation"])


# In[127]:


# data after capping


# In[128]:


sns.boxplot(Final_data["temperature"])


# In[129]:


# data after capping


# In[130]:


Q1=Final_data["temperature"].quantile(.25)
Q3=Final_data["temperature"].quantile(.75)
print(Q3,Q1)
IQR=Q3-Q1
print("IQR",IQR)
upper_value=Q3+1.5*IQR
lower_value=Q1-1.5*IQR
print("upper limit", upper_value, "lower_limit",lower_value)


# In[131]:


Final_data["temperature"]=np.where(Final_data["temperature"]>upper_value,upper_value,np.where(Final_data["temperature"]<lower_value,lower_value,Final_data["temperature"]))


# In[132]:


sns.boxplot(Final_data["temperature"])


# In[133]:


# data after capping


# In[134]:


sns.boxplot(x=Final_data["casual"])


# In[135]:


# as we witnessed there is some outliers skwid towards right hand side and we are trying to correct by using IQR method.


# In[136]:


Q1=Final_data["casual"].quantile(.25)
Q3=Final_data["casual"].quantile(.75)
print(Q3,Q1)
IQR=Q3-Q1
print("IQR",IQR)
upper_value=Q3+1.5*IQR
lower_value=Q1-1.5*IQR
print("upper limit", upper_value, "lower_limit",lower_value)


# In[137]:


Final_data["casual"]=np.where(Final_data["casual"]>upper_value,upper_value,np.where(Final_data["casual"]<lower_value,lower_value,Final_data["casual"]))


# In[138]:


sns.boxplot(x=Final_data["casual"])


# In[139]:


# oultliers removed successfully!


# In[140]:


sns.boxplot(x=Final_data["humudity"])


# In[141]:


# there is no outliers found in the humudity colummn so, we don't require capping over it.


# In[142]:


sns.boxplot(x=Final_data["registered"])


# In[143]:


Q1=Final_data["registered"].quantile(.25)
Q3=Final_data["registered"].quantile(.75)
print(Q3,Q1)
IQR=Q3-Q1
print("IQR",IQR)
upper_value=Q3+1.5*IQR
lower_value=Q1-1.5*IQR
print("upper limit", upper_value, "lower_limit",lower_value)


# In[144]:


Final_data["registered"]=np.where(Final_data["registered"]>upper_value,upper_value,np.where(Final_data["registered"]<lower_value,lower_value,Final_data["casual"]))


# In[145]:


sns.boxplot(x=Final_data["registered"])


# In[146]:


# outliers has been removed from IQR method.


# In[147]:


sns.boxplot(x=Final_data["atemp"])


# In[148]:


Q1=Final_data["atemp"].quantile(.25)
Q3=Final_data["atemp"].quantile(.75)
print(Q3,Q1)
IQR=Q3-Q1
print("IQR",IQR)
upper_value=Q3+1.5*IQR
lower_value=Q1-1.5*IQR
print("upper limit", upper_value, "lower_limit",lower_value)


# In[149]:


Final_data["atemp"]=np.where(Final_data["atemp"]>upper_value,upper_value,np.where(Final_data["atemp"]<lower_value,lower_value,Final_data["atemp"]))


# In[150]:


sns.boxplot(x=Final_data["atemp"])


# In[151]:


# outliers has been removed from IQR method.


# In[152]:


sns.boxplot(x=Final_data["count"])


# In[153]:


# data before capping


# In[154]:


Q1=Final_data["count"].quantile(.25)
Q3=Final_data["count"].quantile(.75)
print(Q3,Q1)
IQR=Q3-Q1
print("IQR",IQR)
upper_value=Q3+1.5*IQR
lower_value=Q1-1.5*IQR
print("upper limit", upper_value, "lower_limit",lower_value)


# In[155]:


Final_data


# In[156]:


import warnings
warnings.filterwarnings("ignore")

sns.distplot(Final_data['month'])

# The month column has some skewness in it, It could be remove by Z score or IQR but we prefer Z score for outlier detection and capping


# In[157]:


upper_limit=Final_data["month"].mean()+ 3*Final_data["month"].std()
lower_limit=Final_data["month"].mean()- 3*Final_data["month"].std()
print("upper_limt",upper_limit)
print("lower_limit",lower_limit)


# In[158]:


Final_data[(Final_data.month>upper_limit)|(Final_data.month<lower_limit)]


# In[159]:


import warnings
warnings.filterwarnings("ignore")

sns.distplot(Final_data['month'])


# In[160]:


Final_data["count"]=np.where(Final_data["count"]>upper_value,upper_value,np.where(Final_data["count"]<lower_value,lower_value,Final_data["count"]))


# In[161]:


sns.boxplot(x=Final_data["count"])


# In[162]:


# outliers has been removed from IQR method.


# In[163]:


sns.boxplot(x=Final_data["windspeed"])


# In[164]:


# data before capping


# In[165]:


Q1=Final_data["windspeed"].quantile(.25)
Q3=Final_data["windspeed"].quantile(.75)
print(Q3,Q1)
IQR=Q3-Q1
print("IQR",IQR)
upper_value=Q3+1.5*IQR
lower_value=Q1-1.5*IQR
print("upper limit", upper_value, "lower_limit",lower_value)


# In[166]:


Final_data["windspeed"]=np.where(Final_data["windspeed"]>upper_value,upper_value,np.where(Final_data["windspeed"]<lower_value,lower_value,Final_data["windspeed"]))


# In[167]:


sns.boxplot(x=Final_data["windspeed"])


# In[168]:


# outliers has been removed from IQR method.


# In[169]:


# Now, we have suceessfully corrected all the outliers in the whole data.


# # In this data we can visualize columns through Heatmap, it says as the humidity goes down the number of cyclist/bikers went up¶

# In[170]:


x=Final_data.pivot_table (index="weather_situation",columns="humudity",values="count")
plt.figure(figsize=(10,5))
sns.heatmap(x)


# In[ ]:





# In[ ]:




