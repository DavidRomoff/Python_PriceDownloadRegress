#!/usr/bin/env python
# coding: utf-8

# In[4]:


pip install pandas_datareader


# In[5]:


import pandas_datareader.data as dtr


# In[26]:


tickers = ['fb','aapl','amzn','nflx','goog','^gspc']


# In[27]:


D = dtr.DataReader(tickers,"yahoo")


# In[8]:


type(D)


# In[28]:


D.tail()


# In[29]:


P = D['Adj Close']


# In[30]:


P.tail()


# In[31]:


Returns = P  / P.shift(1) - 1


# In[32]:


Returns.head()


# In[33]:


R = P.pct_change()


# In[35]:


R.head()


# In[36]:


R2 = R.tail(100)


# In[37]:


R2.columns


# In[40]:


R2.rename(columns = {'^gspc':'SnP'},inplace=True)


# In[41]:


R2.tail()


# In[44]:


results = sm.ols(formula = 'fb ~ SnP',data = R2).fit()


# In[46]:


results.params


# In[51]:


mystocks = R.columns[:5]


# In[52]:


mystocks


# In[53]:


type(mystocks)


# In[60]:


betalist = []

for mystock in mystocks:
    myformula = mystock + " ~ SnP"
    print(myformula)
    results = sm.ols(formula = myformula,data = R2).fit()
    print(results.params['SnP'])
    betalist.append(results.params['SnP'])


# In[61]:


betalist


# In[63]:


import numpy as np
betavec = np.array(betalist)


# In[64]:


notional = 100
notional * betavec


# In[65]:


sum(notional * betavec)


# In[ ]:




