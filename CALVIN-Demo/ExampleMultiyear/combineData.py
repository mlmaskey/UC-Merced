# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 10:22:25 2020

@author: Mahesh Maskey
"""
import pandas as pd
def read_combine(yearList, param): 
    resultdir=('result/annual/WY%d' % yearList[0])
    F = pd.read_csv(resultdir + '/' + param + '.csv', index_col=0, parse_dates=True)
    
    
    for i in yearList:    
      print('\nNow running WY %d' % i)
      resultdir=('result/annual/WY%d' % i)
      F2 = pd.read_csv(resultdir + '/' + param + '.csv', index_col=0, parse_dates=True)
      F = pd.concat([F, F2], axis=0)      
    F.to_csv('result/' + param + '.csv', index=True)
    
# The years inside the paranthesis after "range" shall be the same as 
#in line 6 of the script "main-annual.py"   

yearList = [i for i in range(1990, 2004)]
read_combine(yearList, 'dual_lower')
read_combine(yearList, 'dual_node')
read_combine(yearList, 'dual_upper')
read_combine(yearList, 'evaporation')
read_combine(yearList, 'flow')
read_combine(yearList, 'shortage_cost')
read_combine(yearList, 'shortage_volume')
read_combine(yearList, 'storage')
