#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 13:16:04 2023

@author: francismac
"""


import pandas as pd
import yfinance as yf
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt



########################   PART 1 ####################################

# import the financial statements data for each company over 5 years


path = '/Users/francismac/Desktop/NEOMA/S2/Data Science for Finance/'

BABA_income = pd.read_excel(path+'BABA_IS.xlsx', index_col=(0))
BABA_balance = pd.read_excel(path+'BABA_BS.xlsx', index_col=(0))
BABA_cash = pd.read_excel(path+'BABA_CF.xlsx', index_col=(0))
BABA = pd.concat([BABA_income,BABA_balance,BABA_cash]).transpose()
BABA = BABA.loc[:, ~BABA.columns.duplicated()]

AMZN_income = pd.read_excel(path+'AMZN_IS.xlsx', index_col=(0))
AMZN_balance = pd.read_excel(path+'AMZN_BS.xlsx', index_col=(0))
AMZN_cash = pd.read_excel(path+'AMZN_CF.xlsx', index_col=(0))
AMZN = pd.concat([AMZN_income,AMZN_balance,AMZN_cash]).transpose()
AMZN = AMZN.loc[:, ~AMZN.columns.duplicated()]

JD_income = pd.read_excel(path+'JD_IS.xlsx', index_col=(0))
JD_balance = pd.read_excel(path+'JD_BS.xlsx', index_col=(0))
JD_cash = pd.read_excel(path+'JD_CF.xlsx', index_col=(0))
JD = pd.concat([JD_income,JD_balance,JD_cash]).transpose()
JD = JD.loc[:, ~JD.columns.duplicated()]

EBAY_income = pd.read_excel(path+'EBAY_IS.xlsx', index_col=(0))
EBAY_balance = pd.read_excel(path+'EBAY_BS.xlsx', index_col=(0))
EBAY_cash = pd.read_excel(path+'EBAY_CF.xlsx', index_col=(0))
EBAY = pd.concat([EBAY_income,EBAY_balance,EBAY_cash]).transpose()
EBAY = EBAY.loc[:, ~EBAY.columns.duplicated()]


###############      BABA  ###########################

# calculate Profitability Ratios          
BABA['Gross Profit Margin'] = BABA['Gross Profit']/BABA['Revenue']
BABA['Net Profit Margin'] = BABA['Net Income']/BABA['Revenue']
BABA['Return on Assets (ROA)'] = BABA['Net Income']/BABA['Total Assets']*100
BABA['Return on Equity (ROE)'] = BABA['Net Income']/BABA["Shareholders' Equity"]*100

# calculate Liquidity Ratios
BABA['Current Ratio'] = BABA['Total Current Assets']/BABA['Total Current Liabilities']
BABA['Quick Ratio'] = (BABA['Total Current Assets']-BABA['Inventory'])/BABA['Total Current Liabilities']

# Calculate valuation ratios
BABA['Price to Earnings Ratio (P/E)'] = BABA['Market Cap'] / BABA['Net Income']
BABA['Price to Sales Ratio (P/S)'] = BABA['Market Cap'] / BABA['Revenue']
BABA['Price to Book Ratio (P/B)'] = BABA['Market Cap'] / BABA["Shareholders' Equity"]
BABA['EV/EBITDA Ratio']= BABA['Enterprise Value']/BABA['EBITDA']
BABA['EV/EBIT Ratio'] = BABA['Enterprise Value'] /BABA['EBIT']
BABA['Debt/ Equity (D/E)'] = BABA['Total Debt'] / BABA["Shareholders' Equity"]
BABA['Debt/EBUTDA (D/EBITDA)'] = BABA['Total Debt']/BABA['EBITDA']



BABA_profitability_ratios = ['Gross Profit Margin', 'Net Profit Margin', 'Return on Assets (ROA)', 'Return on Equity (ROE)']
BABA_liquidity_ratios = ['Current Ratio', 'Quick Ratio']
BABA_valuation_ratios = ['Price to Earnings Ratio (P/E)', 'Price to Sales Ratio (P/S)', 'Price to Book Ratio (P/B)', 'EV/EBITDA Ratio', 'EV/EBIT Ratio']

# Create a figure for the first set of ratios
fig1 = plt.figure(figsize=(8, 5))
BABA[BABA_profitability_ratios].plot(title='BABA Profitability Ratios', grid=True)
plt.legend(loc='upper right', fontsize=8,)

# Create a figure for the second set of ratios
fig2 = plt.figure(figsize=(8, 5))
BABA[BABA_liquidity_ratios].plot(title='BABA Liquidity Ratios', grid=True)
plt.legend(loc='upper right', fontsize=8)

# Create a figure for the third set of ratios
fig3 = plt.figure(figsize=(8, 5))
BABA[BABA_valuation_ratios].plot(title='BABA Valuation Ratios', grid=True)
plt.legend(loc='upper right', fontsize=8)

# Show the plots
plt.show()


###############      AMAZN  ###########################

# calculate Profitability Ratios
AMZN['Gross Profit Margin'] = AMZN['Gross Profit']/AMZN['Revenue']
AMZN['Net Profit Margin'] = AMZN['Net Income']/AMZN['Revenue']
AMZN['Return on Assets (ROA)'] = AMZN['Net Income']/AMZN['Total Assets']*100
AMZN['Return on Equity (ROE)'] = AMZN['Net Income']/AMZN["Shareholders' Equity"]*100

# calculate Liquidity Ratios
AMZN['Current Ratio'] = AMZN['Total Current Assets']/AMZN['Total Current Liabilities']
AMZN['Quick Ratio'] = (AMZN['Total Current Assets']-AMZN['Inventory'])/AMZN['Total Current Liabilities']

# Calculate valuation ratios
AMZN['Price to Earnings Ratio (P/E)'] = AMZN['Market Cap'] / AMZN['Net Income']
AMZN['Price to Sales Ratio (P/S)'] = AMZN['Market Cap'] / AMZN['Revenue']
AMZN['Price to Book Ratio (P/B)'] = (AMZN['Market Cap'] / AMZN["Shareholders' Equity"])
AMZN['EV/EBITDA Ratio']= AMZN['Enterprise Value']/AMZN['EBITDA']
AMZN['EV/EBIT Ratio'] = AMZN['Enterprise Value'] /AMZN['EBIT']
AMZN['Debt/ Equity (D/E)'] = AMZN['Total Debt'] / AMZN["Shareholders' Equity"]
AMZN['Debt/EBUTDA (D/EBITDA)'] = AMZN['Total Debt']/AMZN['EBITDA']

AMZN_profitability_ratios = ['Gross Profit Margin', 'Net Profit Margin', 'Return on Assets (ROA)', 'Return on Equity (ROE)']
AMZN_liquidity_ratios = ['Current Ratio', 'Quick Ratio']
AMZN_valuation_ratios = ['Price to Earnings Ratio (P/E)', 'Price to Sales Ratio (P/S)', 'Price to Book Ratio (P/B)', 'EV/EBITDA Ratio', 'EV/EBIT Ratio']


# Create a figure for the first set of ratios
fig4 = plt.figure(figsize=(8, 5))
AMZN[AMZN_profitability_ratios].plot(title='AMZN Profitability Ratios', grid=True)
plt.legend(loc='upper right', fontsize=8,)

# Create a figure for the second set of ratios
fig5 = plt.figure(figsize=(8, 5))
AMZN[AMZN_liquidity_ratios].plot(title='AMZN Liquidity Ratios', grid=True)
plt.legend(loc='upper right', fontsize=8)

# Create a figure for the third set of ratios
fig6 = plt.figure(figsize=(8, 5))
AMZN[AMZN_valuation_ratios].plot(title='AMZN Valuation Ratios', grid=True)
plt.legend(loc='upper right', fontsize=8)

# Show the plots
plt.show()


###############      JD   ###########################

# calculate Profitability Ratios
JD['Gross Profit Margin'] = JD['Gross Profit']/JD['Revenue']
JD['Net Profit Margin'] = JD['Net Income']/JD['Revenue']
JD['Return on Assets (ROA)'] = JD['Net Income']/JD['Total Assets']*100
JD['Return on Equity (ROE)'] = JD['Net Income']/JD["Shareholders' Equity"]*100

# calculate Liquidity Ratios
JD['Current Ratio'] = JD['Total Current Assets']/JD['Total Current Liabilities']
JD['Quick Ratio'] = (JD['Total Current Assets']-JD['Inventory'])/JD['Total Current Liabilities']

# Calculate valuation ratios
JD['Price to Earnings Ratio (P/E)'] = JD['Market Cap'] / JD['Net Income']
JD['Price to Sales Ratio (P/S)'] = JD['Market Cap'] / JD['Revenue']
JD['Price to Book Ratio (P/B)'] = (JD['Market Cap'] / JD["Shareholders' Equity"])
JD['EV/EBITDA Ratio']= JD['Enterprise Value']/JD['EBITDA']
JD['EV/EBIT Ratio'] = JD['Enterprise Value'] /JD['EBIT']
JD['Debt/ Equity (D/E)'] = JD['Total Debt'] / JD["Shareholders' Equity"]
JD['Debt/EBUTDA (D/EBITDA)'] = JD['Total Debt']/JD['EBITDA']


JD_profitability_ratios = ['Gross Profit Margin', 'Net Profit Margin', 'Return on Assets (ROA)', 'Return on Equity (ROE)']
JD_liquidity_ratios = ['Current Ratio', 'Quick Ratio']
JD_valuation_ratios = ['Price to Earnings Ratio (P/E)', 'Price to Sales Ratio (P/S)', 'Price to Book Ratio (P/B)', 'EV/EBITDA Ratio', 'EV/EBIT Ratio']


# Create a figure for the first set of ratios
fig7 = plt.figure(figsize=(8, 5))
JD[JD_profitability_ratios].plot(title='JD Profitability Ratios', grid=True)
plt.legend(loc='upper right', fontsize=8,)

# Create a figure for the second set of ratios
fig8 = plt.figure(figsize=(8, 5))
JD[JD_liquidity_ratios].plot(title='JD Liquidity Ratios', grid=True)
plt.legend(loc='upper right', fontsize=8)

# Create a figure for the third set of ratios
fig9 = plt.figure(figsize=(8, 5))
JD[JD_valuation_ratios].plot(title='JD Valuation Ratios', grid=True)
plt.legend(loc='upper right', fontsize=8)

# Show the plots
plt.show()


###############      EBAY     ###########################

# calculate Profitability Ratios’
EBAY['Gross Profit Margin'] = EBAY['Gross Profit']/EBAY['Revenue']
EBAY['Net Profit Margin'] = EBAY['Net Income']/EBAY['Revenue']
EBAY['Return on Assets (ROA)'] = EBAY['Net Income']/EBAY['Total Assets']*100
EBAY['Return on Equity (ROE)'] = EBAY['Net Income']/EBAY["Shareholders' Equity"]*100

# calculate Liquidity Ratios
EBAY['Current Ratio'] = EBAY['Total Current Assets']/EBAY['Total Current Liabilities']
EBAY['Quick Ratio'] = (EBAY['Total Current Assets']-EBAY['Inventory'])/EBAY['Total Current Liabilities']

# Calculate valuation ratios
EBAY['Price to Earnings Ratio (P/E)'] = EBAY['Market Cap'] / EBAY['Net Income']
EBAY['Price to Sales Ratio (P/S)'] = EBAY['Market Cap'] / EBAY['Revenue']
EBAY['Price to Book Ratio (P/B)'] = (EBAY['Market Cap'] / EBAY["Shareholders' Equity"])
EBAY['EV/EBITDA Ratio']= EBAY['Enterprise Value']/EBAY['EBITDA']
EBAY['EV/EBIT Ratio'] = EBAY['Enterprise Value'] /EBAY['EBIT']
EBAY['Debt/ Equity (D/E)'] = EBAY['Total Debt'] / EBAY["Shareholders' Equity"]
EBAY['Debt/EBUTDA (D/EBITDA)'] = EBAY['Total Debt']/EBAY['EBITDA']


EBAY_profitability_ratios = ['Gross Profit Margin', 'Net Profit Margin', 'Return on Assets (ROA)', 'Return on Equity (ROE)']
EBAY_liquidity_ratios = ['Current Ratio', 'Quick Ratio']
EBAY_valuation_ratios = ['Price to Earnings Ratio (P/E)', 'Price to Sales Ratio (P/S)', 'Price to Book Ratio (P/B)', 'EV/EBITDA Ratio', 'EV/EBIT Ratio']


# Create a figure for the first set of ratios
fig10 = plt.figure(figsize=(8, 5))
EBAY[EBAY_profitability_ratios].plot(title='EBAY Profitability Ratios', grid=True)
plt.legend(loc='upper right', fontsize=8,)

# Create a figure for the second set of ratios
fig11 = plt.figure(figsize=(8, 5))
EBAY[EBAY_liquidity_ratios].plot(title='EBAY Liquidity Ratios', grid=True)
plt.legend(loc='upper right', fontsize=8)

# Create a figure for the third set of ratios
fig12 = plt.figure(figsize=(8, 5))
EBAY[EBAY_valuation_ratios].plot(title='EBAY Valuation Ratios', grid=True)
plt.legend(loc='upper right', fontsize=8)

# Show the plots
plt.show()




########################  PART 2 ####################################

# List of firms
firms = ['BABA', 'AMZN', 'JD', 'EBAY']

# Download stock price data over the past 5 years
start_date = '2018-01-01'
end_date = '2022-12-31'
prices = pd.DataFrame()

for firm in firms:
    data = yf.download(firm, start=start_date, end=end_date, progress=False)
    prices[firm] = data['Adj Close']

# Compute stock returns over the past 5 years
returns = np.log(prices / prices.shift(1))

# Compute average annualized returns
avg_returns = returns.mean() * 252

# Print the firms with the highest and lowest returns
print('Firm with highest return: ', avg_returns.idxmax())
print('Firm with lowest return: ', avg_returns.idxmin())


##############   Visualization of time series data    ########################

# BABA
data_1 = yf.download("BABA",
                     start="2018-01-01",
                     end="2022-12-31",
                     auto_adjust=False,
                     progress=False)

data_1["Simple_rtn"] = data_1["Adj Close"].pct_change()
data_1 = data_1.dropna()


data_1["Adj Close"].plot(title = "BABA Time Series 2018-2022")
(
 data_1[["Adj Close","Simple_rtn"]]
 .plot(subplots = True, sharex = True,
       title = "BABA Time Series 2018-2022")
 )




# AMZN

data_2 = yf.download("AMZN",
                     start="2018-01-01",
                     end="2022-12-31",
                     auto_adjust=False,
                     progress=False)

data_2["Simple_rtn"] = data_2["Adj Close"].pct_change()
data_2 = data_2.dropna()


data_2["Adj Close"].plot(title = "AMZN Time Series 2018-2022")
(
 data_2[["Adj Close","Simple_rtn"]]
 .plot(subplots = True, sharex = True,
       title = "AMZN Time Series 2018-2022")
 )


# JD 

data_3 = yf.download("JD",
                     start="2018-01-01",
                     end="2022-12-31",
                     auto_adjust=False,
                     progress=False)

data_3["Simple_rtn"] = data_3["Adj Close"].pct_change()
data_3 = data_3.dropna()


data_3["Adj Close"].plot(title = "JD Time Series 2018-2022")
(
 data_3[["Adj Close","Simple_rtn"]]
 .plot(subplots = True, sharex = True,
       title = "JD Time Series 2018-2022")
 )



# EBAY

data_4 = yf.download("EBAY",
                     start="2018-01-01",
                     end="2022-12-31",
                     auto_adjust=False,
                     progress=False)

data_4["Simple_rtn"] = data_4["Adj Close"].pct_change()
data_4 = data_4.dropna()


data_4["Adj Close"].plot(title = "EBAY Time Series 2018-2022")
(
 data_4[["Adj Close","Simple_rtn"]]
 .plot(subplots = True, sharex = True,
       title = "EBAY Time Series 2018-2022")
 )




############   Calculating the tchnical indicator ########################

import talib 


data_1["sma_90"]= talib.SMA(data_1["Close"],timeperiod = 90)
(
 data_1[["Close","sma_90"]]
 .plot(title = "BABA 90-days Simple Moving Average (SMA)")
 )


data_2["sma_90"]= talib.SMA(data_2["Close"],timeperiod = 90)
(
 data_2[["Close","sma_90"]]
 .plot(title = "AMZN 90-days Simple Moving Average (SMA)")
 )



data_3["sma_90"]= talib.SMA(data_3["Close"],timeperiod = 90)
(
 data_3[["Close","sma_90"]]
 .plot(title = "JD 90-days Simple Moving Average (SMA)")
 )


data_4["sma_90"]= talib.SMA(data_4["Close"],timeperiod = 90)
(
 data_4[["Close","sma_90"]]
 .plot(title = "EBAY 90-days Simple Moving Average (SMA)")
 )


#############  calculate and plot the relavent strengh index  ########################




data_1["rsi"] = talib.RSI(data_1["Close"])

fig, ax = plt.subplots()
data_1["rsi"].plot(ax=ax, 
               title="BABA Relative Strength Index (RSI)")
ax.hlines(y=30, 
          xmin=data_1.index.min(), 
          xmax=data_1.index.max(), 
          color="red")
ax.hlines(y=70, 
          xmin=data_1.index.min(), 
          xmax=data_1.index.max(), 
          color="red")

sns.despine()
plt.tight_layout()
# plt.savefig("images/figure_5_3", dpi=200)


data_2["rsi"] = talib.RSI(data_2["Close"])

fig, ax = plt.subplots()
data_2["rsi"].plot(ax=ax, 
               title="AMZN Relative Strength Index (RSI)")
ax.hlines(y=30, 
          xmin=data_2.index.min(), 
          xmax=data_2.index.max(), 
          color="red")
ax.hlines(y=70, 
          xmin=data_2.index.min(), 
          xmax=data_2.index.max(), 
          color="red")

sns.despine()
plt.tight_layout()
# plt.savefig("images/figure_5_3", dpi=200)

data_3["rsi"] = talib.RSI(data_3["Close"])

fig, ax = plt.subplots()
data_3["rsi"].plot(ax=ax, 
               title="JD Relative Strength Index (RSI)")
ax.hlines(y=30, 
          xmin=data_3.index.min(), 
          xmax=data_3.index.max(), 
          color="red")
ax.hlines(y=70, 
          xmin=data_3.index.min(), 
          xmax=data_3.index.max(), 
          color="red")

sns.despine()
plt.tight_layout()
# plt.savefig("images/figure_5_3", dpi=200)

data_4["rsi"] = talib.RSI(data_4["Close"])

fig, ax = plt.subplots()
data_4["rsi"].plot(ax=ax, 
               title="EBAY Relative Strength Index (RSI)")
ax.hlines(y=30, 
          xmin=data_4.index.min(), 
          xmax=data_4.index.max(), 
          color="red")
ax.hlines(y=70, 
          xmin=data_4.index.min(), 
          xmax=data_4.index.max(), 
          color="red")

sns.despine()
plt.tight_layout()
# plt.savefig("images/figure_5_3", dpi=200)



