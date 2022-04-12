#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('casestudy.csv')


# In[3]:


df.head()


# # Total Net Revenue for the Current Year (2017)

# In[ ]:


"""
QUESTION 1
"""
sum1 = 0
for index,row in df.iterrows():
    if (row["year"]==2017):
        sum1+=row["net_revenue"]
print(sum1)


# # New Customer Revenue

# In[29]:


"""
QUESTION 2
"""
dict2015 = {}
for index,row in df.iterrows():

    if(row["year"]==2015):
        if row["customer_email"] not in dict2015:
            dict2015[row["customer_email"]] = [row["net_revenue"]]
        else:
            dict2015[row["customer_email"]].append(row["net_revenue"])
            
dict2016 = {}
for index,row in df.iterrows():

    if(row["year"]==2016):
        if row["customer_email"] not in dict2016:
            dict2016[row["customer_email"]] = [row["net_revenue"]]
        else:
            dict2016[row["customer_email"]].append(row["net_revenue"])

dict2017 = {}
for index,row in df.iterrows():

    if(row["year"]==2017):
        if row["customer_email"] not in dict2017:
            dict2017[row["customer_email"]] = [row["net_revenue"]]
        else:
            dict2017[row["customer_email"]].append(row["net_revenue"])

net2016=0
j=0
k=0
for key,value in dict2016.items():
    if key not in dict2015:
        for j in range(len(value)):
            net2016+=value[j]
net2017= 0
for key,value in dict2017.items():
    if key not in dict2016:
        for k in range(len(value)):
            net2017+=value[k]

#print(net2016)
#print(net2017)
    
print(net2016+net2017)


# # Existing Customer Growth

# In[19]:


"""
Question 3
"""

sum2 = 0
for index,row in df.iterrows():
    if (row["year"]==2016):
        sum1+=row["net_revenue"]

print(sum1 - sum2)


# # Existing Customer revenue for Current Year and Prior Year

# In[32]:


"""
Question 5, 6
"""
existcustomer2016={}
existcustomer2017={}
existSum2016 = 0
existSum2017 =0
for key,value in dict2016.items():
    if key in dict2015 and key in dict2016:
        existcustomer2016[key]= value

for key,value in dict2017.items():
    if key in dict2016 and key in dict2017:
        existcustomer2017[key]= value
        
# print(existcustomer2016)
j,k=0,0
# print(existcustomer2017)
for key, value in existcustomer2016.items():
    for j in range(len(value)):
        existSum2016+=value[j]
for key, value in existcustomer2017.items():
    for k in range(len(value)):
        existSum2017+=value[k]

print("The Prior Year 2016 Customer revenue is "+str(existSum2016))
print("The Current Year 2017 Customer revenue is "+str(existSum2017))

        
        


# # Total Customer for Current Year

# In[28]:


#total customer current year
"""
QUESTION 7
"""
customer = 0
for k,v in dict2017.items():
        customer+=1
print(customer)


# # Total Customer Previous Year 2016

# In[23]:


customer2017Total = customer 
#total customer previous year 2016
"""
QUESTION 8
"""
customer = 0
for k,v in dict2016.items():
        customer+=1
print(customer)


# # Total number of New Customer

# In[25]:


customer2016Total = customer 
#New Customer 
"""
QUESTION 9
"""
newCustomer = 0
newCustomer = customer2017Total - len(existcustomer2017)
print(newCustomer)


# # Total number of lost Customer

# In[38]:


#lost custoner
"""
QUESTION 10 
"""
lostCustomer = 0
l = {}
for key,value in dict2016.items():
    if key in dict2016 and key not in dict2017:
        l[key]= value
# print(len(l))
k = {}
for key,value in dict2015.items():
    if key in dict2015 and key not in dict2016:
        k[key]= value
# print(len(k))

print(len(l)+len(k))


# # Revenue lost from attrition

# In[46]:


"""
QUESTION 4
"""
lostCustomer = 0
m = {}
for key,value in dict2015.items():
    if key in dict2015 and key not in dict2016:
        m[key]= value
print(len(m))



# In[47]:


totalLoss = 0 

for key,value in m.items():
    for j in range(len(value)):
        totalLoss+=value[j]
for key,value in l.items():
    for j in range(len(value)):
        totalLoss+=value[j]
print(totalLoss)

