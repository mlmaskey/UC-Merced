from calvin import *

eop = None
beginYear = 1922
endYear = 2004
dataDir = r'C:\Users\Water Management Lab\Documents\Maskey\NOAA\CALVIN\oldCalvinMM\calvin\data\runBase'
saveDir = r'C:\Users\Water Management Lab\Box\ManuscriptFolder\InitialCALVIN\ArchiveResults\runBaseWhy'
debugDir = r'C:\Users\Water Management Lab\Box\ManuscriptFolder\InitialCALVIN\ArchiveResults\runBaseWhy'
for i in range(1990,2004):

  print('\nNow running WY %d' % i)

  calvin = CALVIN(dataDir + '/linksWY%d.csv' % i, ic=eop)

  calvin.create_pyomo_model(debug_mode=True)
  calvin.solve_pyomo_model(solver='glpk', nproc=1, debug_mode=True)

  eop = postprocess(calvin.df, calvin.model, resultdir=('result/annual/WY%d' % i)) 
