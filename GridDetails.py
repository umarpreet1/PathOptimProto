# -*- coding: utf-8 -*- 

class Grid:
    #constructor intializing all the variables
    def __init__(self):
        self.h_size=9
        self.v_size=7
        self.end_pts_no=0
        self.end_pts=list()
        self.take_off_pt=[6,4]
        self.landing_pt=[0,2]
    
    #input the size of grid
    def setSize(self):
        self.v_size=int(raw_input("enter vertical size"))
        self.h_size=int(raw_input("enter horizontal size"))

    #return the size of grid
    def getSize(self):
        return [self.v_size,self.h_size]

    #set end points from end point file
    def setEndPts(self):
        pts_file=open("end_points.txt","r")
        for pt in pts_file:
            [x,y]=pt.split()
            [x,y]=[int(x),int(y)]
            self.end_pts_no=self.end_pts_no+1
            self.end_pts.append([x,y])
        pts_file.close()

    #get end points of the grid
    def getEndPts(self):
        return self.end_pts 

    #set take off position
    def setTakeOffPt(self):
        [x,y]=raw_input("enter take off position").split()
        [x,y]=[int(x),int(y)]
        self.take_off_pt=[x,y]
    
    #set landing position
    def setLandingPt(self):
        [x,y]=raw_input("enter Landing position").split()
        [x,y]=[int(x),int(y)]
        self.landing_pt=[x,y]

    #return take off coordinates
    def getTakeOffPt(self):
        return self.take_off_pt

    #return landing coordinates
    def getLandingPt(self):
        return self.landing_pt           
            
        
        
            
    