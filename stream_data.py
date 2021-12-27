# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 15:50:29 2021

@author: monob
"""

import pandas as pd
import yfinance as yf

from datetime import date



def Stream():
    
        df = yf.download(
        tickers = ["ETH-USD", "BTC-USD","XRP-USD","XLM-USD","LTC-USD","PA=F","GC=F","^GSPC","^N225","NVDA","AMD"],
        start = "2017-01-02",
        end = str(date.today()),
        interval = "1d"    
        )
        
        counts = []
        for col in df.Close.columns:
            na_count = df.Close[df.Close[col].isna()].shape[0]
            counts.append(na_count)

        pd.DataFrame(counts, index=df.Close.columns, columns=['NA'])
        df_original = df.Close.copy()
        df_original.rename(columns = {'ETH-USD':'ETH', 'BTC-USD':'BTC', 'GC=F':'Gold', 'LTC-USD':'LTC','XLM-USD':'XLM', 'XRP-USD':'XRP','^GSPC':'SP500', '^N225':'N225','PA=F':'Palladium', 'NVDA':'NVIDIA'}, inplace = True)
        for column_name in df_original.columns:
            df_original[column_name].fillna(method='ffill', inplace=True)
            df_original[column_name].fillna(method='backfill', inplace=True)
            
        
        df_original.to_csv('data.csv')    