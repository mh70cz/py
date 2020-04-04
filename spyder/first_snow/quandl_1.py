# _NtHjpxNhDQawMqY3De-
# https://towardsdatascience.com/time-series-analysis-in-python-an-introduction-70d5a5b1d52a

import quandl
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
quandl.ApiConfig.api_key = '_NtHjpxNhDQawMqY3De-'

#tesla_orig = quandl.get('WIKI/TSLA')
#gm_orig = quandl.get('WIKI/GM')

tesla = tesla_orig.copy()
gm = gm_orig.copy()

# Quandl does not have number of shares data for free - estimation
# Yearly average number of shares outstanding for Tesla and GM
tesla_shares = {2018: 168e6, 2017: 162e6, 2016: 144e6, 2015: 128e6, 2014: 125e6, 2013: 119e6, 2012: 107e6, 2011: 100e6, 2010: 51e6}
gm_shares = {2018: 1.42e9, 2017: 1.50e9, 2016: 1.54e9, 2015: 1.59e9, 2014: 1.61e9, 2013: 1.39e9, 2012: 1.57e9, 2011: 1.54e9, 2010:1.50e9}

gm.tail(5)

plt.plot(gm.index, gm['Adj. Close'])
plt.title('GM Stock Price')
plt.ylabel('Price ($)')
plt.show()

plt.title('Tesla Stock Price')
plt.plot(tesla.index, tesla['Adj. Close'])
plt.ylabel('Price ($)')
plt.show()

# create a year, and a  cap column, reset index (create Data column)
tesla['Year'] = tesla.index.year
tesla['cap'] = 0
tesla.reset_index(inplace = True)

gm['Year'] = gm.index.year
gm['cap'] = 0
gm.reset_index(inplace = True)

#calculate market cap (shares * price )
for i, year in enumerate(tesla['Year']):
    shares = tesla_shares.get(year)
    tesla.loc[i, 'cap'] = shares * tesla.loc[i, 'Adj. Close']
    
for i, year in enumerate(gm['Year']):
    shares = gm_shares.get(year)
    gm.loc[i, 'cap'] = shares * gm.loc[i, 'Adj. Close']
    
#merge the datasets, rename columns, get only relevant columns
cars = gm.merge(tesla, how='inner', on='Date')    
cars.rename(columns = {"cap_x": "gm_cap",
                       "cap_y": "tesla_cap"}, inplace = True)
    
cars = cars.loc[:, ["Date", "gm_cap", "tesla_cap"]]

#divide to get market cap in billlons of dollars
cars["gm_cap"] = cars["gm_cap"]/1e9
cars["tesla_cap"] = cars["tesla_cap"]/1e9

plt.plot(cars.Date, cars.gm_cap, label = "GM")
plt.plot(cars.Date, cars.tesla_cap, label = "Tesla")
plt.title("Market capitalization")
plt.xlabel("Year")
plt.ylabel("Billions USD")
plt.legend(loc="upper left")
plt.show()

first_date = cars.loc[
        np.min(list(np.where(cars["tesla_cap"] > cars["gm_cap"])[0])), 
              "Date"]

last_date = cars.loc[
        np.max(list(np.where(cars["tesla_cap"] > cars["gm_cap"])[0])),
              "Date"]