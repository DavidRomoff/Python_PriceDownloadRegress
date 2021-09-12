
pip install pandas_datareader



import pandas_datareader.data as dtr




tickers = ['fb','aapl','amzn','nflx','goog','^gspc']


D = dtr.DataReader(tickers,"yahoo")


type(D)



D.tail()



P = D['Adj Close']



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



R2.tail()




results = sm.ols(formula = 'fb ~ SnP',data = R2).fit()


results.params


mystocks = R.columns[:5]



mystocks




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
