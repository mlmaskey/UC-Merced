from revin import*
from postREVIN import*
eop = None
beginYear = 1922
endYear = 2003
dataDir = r'D:\PostDocResearch\UC Merced\importCALVIN\NOAA\runRechargeCookie'
saveDir = 'Results/runRechargeCookie'

for i in range(beginYear,endYear):

  print('\nNow running WY %d' % i)

  revin = REVIN(dataDir + '/linksWY%d.csv' % i, ic=eop)

  revin.eop_constraint_multiplier(0.1)

  revin.create_pyomo_model(debug_mode=True, debug_cost=2e8)
  # revin.solve_pyomo_model(solver='glpk', nproc=1, debug_mode=True, maxiter=15)

  # revin.create_pyomo_model(debug_mode=False)
  revin.solve_pyomo_model(solver='glpk', nproc=1, debug_mode=False)

  # this will append to results files
  eop = postprocess(revin.df, revin.model, resultdir= saveDir + '/WY' + str(i), annual=True) 
