# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 10:22:25 2020

@author: Mahesh L Maskey
"""
import pandas as pd
def dropDebug(fp):
    flow = pd.read_csv(fp + '/flow.csv', index_col=0, parse_dates=True)
    dual_upper = pd.read_csv(fp + '/dual_upper.csv', index_col=0, parse_dates=True)
    dual_lower = pd.read_csv(fp + '/dual_lower.csv', index_col=0, parse_dates=True)
    ObjectiveValue = pd.read_csv(fp + '/ObjectiveValue.csv', index_col=0, parse_dates=True)
    unitCost = pd.read_csv(fp + '/unitCost.csv', index_col=0, parse_dates=True)
    flow = dropColumns(flow, '-DBUGSNK')
    flow = dropColumns(flow, 'DBUGSRC-')
    flow = dropColumns(flow, 'DBUGSNK-')
    dual_upper = dropColumns(dual_upper, '-DBUGSNK')
    dual_upper = dropColumns(dual_upper, 'DBUGSRC-')
    dual_upper = dropColumns(dual_upper, 'DBUGSNK-')
    dual_lower = dropColumns(dual_lower, '-DBUGSNK')
    dual_lower = dropColumns(dual_lower, 'DBUGSRC-')
    dual_lower = dropColumns(dual_lower, 'DBUGSNK-')
    ObjectiveValue = dropColumns(ObjectiveValue, '-DBUGSNK')
    ObjectiveValue = dropColumns(ObjectiveValue, 'DBUGSRC-')
    ObjectiveValue = dropColumns(ObjectiveValue, 'DBUGSNK-')
    unitCost = dropColumns(unitCost, '-DBUGSNK')
    unitCost = dropColumns(unitCost, 'DBUGSRC-')   
    unitCost = dropColumns(unitCost, 'DBUGSNK-')   
    flow.to_csv(fp + '/flow.csv')
    dual_upper.to_csv(fp + '/dual_upper.csv')
    dual_lower.to_csv(fp + '/dual_lower.csv')    
    ObjectiveValue.to_csv(fp + '/ObjectiveValue.csv')    
    unitCost.to_csv(fp + '/unitCost.csv')    
    
def dropColumns(data, string):
    debugCols = data.filter(regex = string).columns
    data = data.drop(debugCols, axis=1)
    return(data)


def read_combine(yearList, param,resultdir): 
    resultdir1=(resultdir + '/WY%d' % yearList[0])
    F = pd.read_csv(resultdir1 + '/' + param + '.csv', index_col=0, parse_dates=True)
    
    
    for i in range(yearList[1],yearList[-1]):    
      print('\nNow running WY %d' % i)
      resultdir1=(resultdir + '/WY%d' % i)
      F2 = pd.read_csv(resultdir1 + '/' + param + '.csv', index_col=0, parse_dates=True)
      F = pd.concat([F, F2], axis=0)
      
    F.to_csv(resultdir + '/' + param + '.csv', index=True)
    
yearList = [i for i in range(1922, 2005)]
#yearList = [i for i in range(0, 9)]
resultDir ='Results/runRecharge_region_V4A'
read_combine(yearList, 'dual_lower', resultDir)
read_combine(yearList, 'dual_node', resultDir)
read_combine(yearList, 'dual_upper', resultDir)
read_combine(yearList, 'evaporation', resultDir)
read_combine(yearList, 'flow', resultDir)
read_combine(yearList, 'shortage_cost', resultDir)
read_combine(yearList, 'shortage_volume', resultDir)
read_combine(yearList, 'storage', resultDir) 
read_combine(yearList, 'ObjectiveValue', resultDir)
read_combine(yearList, 'unitCost', resultDir)
read_combine(yearList, 'MatrixModel', resultDir)
#dropDebug(resultDir)