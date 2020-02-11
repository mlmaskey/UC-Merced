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

# importing watwr demand costs

dfSC = pd.read_csv(fp + '/shortage_cost.csv', index_col=0, parse_dates=True)
dfUrban_cost = dfSC.filter(regex = '_urban')
dfAGri_cost = dfSC.filter(regex = '_ag')
costUrbanRegion = dfUrban_cost.sum()
costAgriRegion = dfAGri_cost.sum()
dfCost=pd.DataFrame({'Urban' : np.array(costUrbanRegion), 
                 'Agriculture' :np.array(costAgriRegion)})
dfCost.index= ['SC', 'TB', 'SJSB', 'LSVD', 'USV']

## Plotting storage cost
regions = ['SC', 'TB', 'SJSB', 'LSVD', 'USV']
costUrban = np.array( dfCost.Urban)/1e6
costAgriculture = np.array(dfCost.Agriculture)/1e6
ind = [x for x, _ in enumerate(regions)]

plt.figure(figsize = (12,5))
plt.bar(ind, costUrban, width=0.8, label='Urban', color='red')
plt.bar(ind, costAgriculture, width=0.8, label='Agriculture', color='blue', bottom=costUrban)

plt.xticks(ind, regions)
plt.ylabel("Costs (Million$)")
plt.xlabel("Region")
plt.legend(loc="upper right")
plt.title('Water Storage cost from 1990-2003')

plt.show()

plt.savefig('Graphs/Storage costs.png')
