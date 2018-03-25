# -*- coding: utf-8 -*-

import GridConst as gc
import GridDetails as gd
import PathMaker as pm
import GeneticAlgorithm as ga
import numpy as np
newflightData=gd.Grid()
#newflightData.setSize()
newflightData.setEndPts()
#newflightData.setTakeOffPt()
#newflightData.setLandingPt()

newflightGrid=gc.GridMaker()
newflightGrid.MakeGrid(newflightData)
newflightGrid.printGrid()

grid_array=newflightGrid.getGrid()
print np.count_nonzero(grid_array)

#pt=pm.Path(newflightData,grid_array)
#pt.makePath()
genAlgo=ga.GenAlgo(newflightData,grid_array)
genAlgo.DoOptimization()