from calvin import *

eop = None
beginYear = 1922
endYear = 2004
dataDir = r'C:\Users\Water Management Lab\Box\ManuscriptFolder\InitialCALVIN\data\dataRechargeV1'
saveDir = r'C:\Users\Water Management Lab\Box\ManuscriptFolder\InitialCALVIN\ArchiveResults\runRechargeV1Final'
debugDir = r'C:\Users\Water Management Lab\Box\ManuscriptFolder\InitialCALVIN\ArchiveResults\DebuggedrunRechargeV1Final'
for i in range(beginYear,endYear):

  print('\nNow running WY %d' % i)

  calvin = CALVIN(dataDir + '/linksWY%d.csv' % i, ic=eop)

  calvin.eop_constraint_multiplier(0.1)

  calvin.create_pyomo_model(debug_mode=True, debug_cost=2e8)
  calvin.solve_pyomo_model(solver='glpk', nproc=1, debug_mode=True, maxiter=15)
  postprocess(calvin.df, calvin.model, resultdir= debugDir + '/WY' + str(i), annual=True)


  calvin.create_pyomo_model(debug_mode=False)
  calvin.solve_pyomo_model(solver='glpk', nproc=1, debug_mode=False)

  # this will append to results files
  eop = postprocess(calvin.df, calvin.model, resultdir= saveDir + '/WY' + str(i))

