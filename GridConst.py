# -*- coding: utf-8 -*-

import GridDetails as g
import numpy as np


class GridMaker:
    
    #constructor to make the grid
    def __init__(self):            
        self.v_size=0
        self.h_size=0
        self.grid=None
        
    #main method to constuct the entire grid    
    def MakeGrid(self,grid):
        [self.v_size,self.h_size]=grid.getSize()
        self.grid_array=np.zeros((self.v_size,self.h_size),dtype=np.uint8)
        self.end_pts=grid.getEndPts()
        self.markEndPts()
        self.makeEdges()
        self.fillAdjacent()

    #to mark the end points on the grid
    def markEndPts(self):
        for pt in self.end_pts:
            self.grid_array[pt[0],pt[1]]=1
            
    #make boundary connecting between these points        
    def makeEdges(self):
        for pt1 in self.end_pts:
            for pt2 in self.end_pts:
                if pt1!=pt2:
                    x1=float(pt1[0])
                    y1=float(pt1[1])
                    x2=float(pt2[0])
                    y2=float(pt2[1])
                    if y1!=y2:
                        n=x2-x1
                        d=y2-y1
                        m=n/d
                        for x in range(min(int(x1),int(x2)),max(int(x1),int(x2))):
                            for y in range(min(int(y1),int(y2)),max(int(y1),int(y2))):
                                if (x==int(m*(y-y1)+x1)):
                                    self.grid_array[x,y]=1
                    else:
                        for x in range(min(int(x1),int(x2)),max(int(x1),int(x2))):
                            self.grid_array[x,int(y1)]=1
    
    #fill the area of grid inside the boundary         
    def fillAdjacent(self):    
        new_grid=None
        while not np.array_equal(new_grid,self.grid_array):
            new_grid=self.grid_array
            for epr in range(1,self.h_size-1):
                for ept in range(1,self.v_size-1):
                    top=self.grid_array[ept,epr-1]
                    bottom=self.grid_array[ept,epr+1]
                    left=self.grid_array[ept-1,epr]
                    right=self.grid_array[ept+1,epr]
                    total=top+bottom+left+right
                    if total>=3:
                        self.grid_array[ept,epr]=1
    
    #print the grid on the console    
    def printGrid(self):
        print self.grid_array
            
    #return the grid constucted        
    def getGrid(self):
        return self.grid_array