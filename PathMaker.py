# -*- coding: utf-8 -*-

import GridDetails as gd
import GridConst as gc
import numpy as np
import random as r
from copy import deepcopy
class Path:
    def __init__(self,Grid,grid_array):
        self.grid=Grid
        self.grid_array=grid_array
        self.take_off_pt=[0,0]
        self.landing_pt=[0,0]
        self.no_of_cells=np.count_nonzero(self.grid_array)
        self.bounds=self.grid.getSize()        
        
    def makePath(self):
        self.take_off_pt=self.grid.getTakeOffPt()
        self.landing_pt=self.grid.getLandingPt()
        self.no_of_cells=np.count_nonzero(self.grid_array)
        #path=self.makeRandomPath()        
        #print path       
        pathcells=self.checkPathCells([8, 3, 5, 6.0, 7, 6, 8, 7, 5, 2.0, 2, 1.0, 3, 3.0, 5, 6, 5, 5, 5, 1, 5, 8, 7, 7, 7, 5, 6, 2, 1, 2, 4, 4, 6, 2, 6, 3, 8, 3, 7, 8, 7, 1, 7.0, 4, 7]
)
        print pathcells
        
    def makeRandomPath(self):
        #the commands to move in the path in direction 
        # 1 2 3
        # 4   5
        # 6 7 8
        #if it is at edge and direction of path is outside it is ignored
        path_command=[r.randint(1,8) for p in range(0,self.no_of_cells)]
        return path_command
        
    
    def checkPathCells(self,path):
        copy_grid=deepcopy(self.grid_array)
        curcell=self.take_off_pt
        copy_grid[curcell[0],curcell[1]]=0
        no_path_cells=1
        for d in path:
            if d==1 or d==2 or d==3:
                if curcell[0]!=0:
                    if d==2:
                        curcell=[curcell[0]-1,curcell[1]]
                    elif d==1:
                        if curcell[1]!=0:
                            curcell=[curcell[0]-1,curcell[1]-1]
                    elif d==3:
                        if curcell[1]!=self.bounds[1]-1:
                            curcell=[curcell[0]-1,curcell[1]+1]
            elif d==4 or d==5:
                    if d==4:
                        if curcell[1]!=0:
                            curcell=[curcell[0],curcell[1]-1]
                    elif d==5:
                        if curcell[1]!=self.bounds[1]-1:
                            curcell=[curcell[0],curcell[1]+1]
            elif d==6 or d==7 or d==8:
                if curcell[0]!=self.bounds[0]-1:
                    if d==7:
                        curcell=[curcell[0]+1,curcell[1]]
                    elif d==6:
                        if curcell[1]!=0:
                            curcell=[curcell[0]+1,curcell[1]-1]
                    elif d==8:
                        if curcell[1]!=self.bounds[1]-1:
                            curcell=[curcell[0]+1,curcell[1]+1]
            if copy_grid[curcell[0],curcell[1]]==1:
                no_path_cells=no_path_cells+1
                copy_grid[curcell[0],curcell[1]]=0
            #print copy_grid
            #print "next \n"
        return no_path_cells

    def pathFitness(self,path):
        nop=float(self.checkPathCells(path))
        noc=float(self.no_of_cells)
        fitness=noc/nop
        return fitness
    
    
    def getNoOfCells(self):
        return self.no_of_cells
                                                        


            