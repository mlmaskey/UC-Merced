from calvin import *

eop = None

for i in range(1990,2004):

  print('\nNow running WY %d' % i)

  calvin = CALVIN('calvin/data/annual/linksWY%d.csv' % i, ic=eop)

  calvin.create_pyomo_model(debug_mode=True)
  calvin.solve_pyomo_model(solver='glpk', nproc=1, debug_mode=True)

  eop = postprocess(calvin.df, calvin.model, resultdir=('result/annual/WY%d' % i)) 
