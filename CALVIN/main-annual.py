from calvin.calvin import *
from calvin.postprocessor import *

eop = None
beginYear = 1922
endYear = 1925
dataDir = 'calvin/data/runBase'
saveDir = 'Results/runBase_test'
debugDir = 'Results/DebugedrunBase_test'

for i in range(beginYear, endYear):
    print('\nNowT running WY %d' % i)

    calvin = CALVIN(dataDir + '/linksWY%d.csv' % i, ic=eop)

    calvin.eop_constraint_multiplier(0.1)

    calvin.create_pyomo_model(debug_mode=True, debug_cost=2e8)
    calvin.solve_pyomo_model(solver='glpk', nproc=1, debug_mode=True, maxiter=25)
    postprocess(calvin.df, calvin.model, resultdir=debugDir + '/WY' + str(i), annual=True)

    calvin.create_pyomo_model(debug_mode=False)
    calvin.solve_pyomo_model(solver='glpk', nproc=1, debug_mode=False)

    # this will append to results files
    eop = postprocess(calvin.df, calvin.model, resultdir=saveDir + '/WY' + str(i), annual=True)
