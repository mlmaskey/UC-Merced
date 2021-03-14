# from gurobipy import *
# 09092020 2:42
from calvin import CALVIN, postprocess

dataDir = 'calvin/data/runBase'
saveDir = 'runBase'
setName = 'linksWY19212003'
calvin = CALVIN(dataDir + '/' + setName + '.csv')
# calvin.create_pyomo_model(debug_mode=True, debug_cost=2e8)
# calvin.solve_pyomo_model(solver='gurobi', nproc=2, debug_mode=True, maxiter=15)
# calvin.solve_pyomo_model(solver='cbc', nproc=10, debug_mode=True, maxiter=15)
# calvin.solve_pyomo_model(solver='glpk', nproc=1, debug_mode=True, maxiter=15)

calvin.create_pyomo_model(debug_mode=False)
# calvin.solve_pyomo_model(solver='glpk', nproc=1, debug_mode=False)
calvin.solve_pyomo_model(solver='gurobi', nproc=2, debug_mode=False)
# calvin.solve_pyomo_model(solver='cbc', nproc=10, debug_mode=False)
postprocess(calvin.df, calvin.model, resultdir=saveDir + '/Perfect' + setName)
