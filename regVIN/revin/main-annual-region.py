from regvin import*
from postREVIN import*
eop = None
beginYear = 1922
endYear = 2004
dataDir = r'D:\PostDocResearch\UC Merced\importCALVIN\NOAA\runBaseRegion'
saveDir = '../Results/runBaseRegion'
iNboundNode = ['C37', 'C301', 'C307', 'A204', 'A207', 'C20', 'C67', 'D43',
               'D42', 'HSU204C67', 'HSD204', 'D509', 'HGR08']
outboundNode = ['D517', 'C20', 'C38', 'D511', 'D55', 'D507']
    
for i in range(beginYear,endYear):

  print('\nNow running WY %d' % i)

  regvin = REGVIN(dataDir + '/linksWY%d.csv' % i, iNboundNode, outboundNode, ic=eop)

  regvin.eop_constraint_multiplier(0.1)

  regvin.create_pyomo_model(debug_mode=True, debug_cost=2e8)
  regvin.solve_pyomo_model(solver='glpk', nproc=1, debug_mode=True, maxiter=50)

  regvin.create_pyomo_model(debug_mode=False)
  regvin.solve_pyomo_model(solver='glpk', nproc=1, debug_mode=False)

  # this will append to results files
  eop = postprocess(regvin.df, regvin.model, resultdir= saveDir + '/WY' + str(i), annual=True) 
