# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 13:11:11 2020

@author: Mahesh
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def plotSeries(dateString, qtyvalue, ylblStr, ttleStr, saveFigName):
    ndata = len(dateString)
    plt.figure(figsize = (12,5))
    plt.plot(dateString, qtyvalue)
    plt.axis([dateString[0], dateString[ndata-1], qtyvalue.min(), qtyvalue.max()])
    plt.xlabel('Month', fontsize=18)
    plt.ylabel(ylblStr, fontsize=18)
    plt.title(ttleStr, fontsize = 20)
    plt.show()
    plt.savefig(saveFigName)
        
        
fp = 'result'

# importing evaporation data
F = pd.read_csv(fp + '/flow.csv', index_col=0, parse_dates=True)
dataF = F.filter(regex ='INFLOW-SR_FOL')

dateString = dataF.index
FolQIn = np.array(dataF)
plotSeries(dateString, FolQIn, 'Inflow, TAF', 
           ttleStr = 'Inflow from Folsom reservoir', 
           saveFigName =  'Graphs/FolsomINFLOW.png')


# importing evaporation data
    
ET = pd.read_csv(fp + '/evaporation.csv', index_col=0, parse_dates=True)
dataET = ET.filter(regex='SR_')

ET_FOL =dataET.filter(regex ='_FOL')
dateString = dataET.index
ET_FOL = np.array(ET_FOL)
plotSeries(dateString, ET_FOL, 'Evaporation Loss, %', 
           ttleStr = 'Evaporation from Folsom reservoir', 
           saveFigName =  'Graphs/FolsomET.png')

# importing storage data
storage = pd.read_csv(fp + '/storage.csv', index_col=0, parse_dates=True)
dataStorage = storage.filter(regex='SR_')
# surface water reservoir behind the dam
srFOL =dataStorage.filter(regex ='_FOL')
srFOL = np.array(srFOL)

# groundwater reservoir behind the dam
gwFOL =storage.filter(regex ='GW_09')
gwFOL = np.array(gwFOL)

dfData=pd.DataFrame({'ST' : np.ndarray.flatten(srFOL), 
                 'GW' : np.ndarray.flatten(gwFOL)})

fig, ax1 = plt.subplots(figsize=(12,5))

ax2 = ax1.twinx()
ax1.plot(dateString, dfData.ST, 'blue')
ax2.plot(dateString, dfData.GW, 'red')

ax1.set_xlabel('Months')
ax1.set_ylabel('Surface  water', color='blue')
ax2.set_ylabel('Groundwater', color='red')
plt.title('Storage in ac-ft', fontsize = 20)

plt.show()
plt.savefig('Graphs/FolsomStorageGWSR.png')
