from calvin import *
from postprocessor import *

calvin = CALVIN('calvin/data/annual/linksWY1950.csv')

# run in debug mode. reduces LB constraints.
calvin.create_pyomo_model(debug_mode=True, debug_cost=2e10)
calvin.solve_pyomo_model(solver='glpk', nproc=1, debug_mode=True)

# run without debug mode (should be feasible)
calvin.create_pyomo_model(debug_mode=False)
calvin.solve_pyomo_model(solver='glpk', nproc=1, debug_mode=False)

postprocess(calvin.df, calvin.model, resultdir='example-results1950')