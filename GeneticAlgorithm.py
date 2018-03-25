#-------------------------------------------------------------
#               Genetic Algorithm (GA)
#-------------------------------------------------------------
# To solve optimization problem (minimization) using GA.
#-------------------------------------------------------------
# Python version used: 2.6 / 2.7
#-------------------------------------------------------------


#-------------------------------------------------------------
# Step 1: Library Inclusion                             
#-------------------------------------------------------------
import random
import time
from copy import deepcopy
import PathMaker as pm 


class Individual:
    def __init__(self, C, F):
        self.chromosome=C
        self.fitness=F


class GenAlgo:
    def __init__(self,Grid,grid_array):
        self.p=pm.Path(Grid,grid_array)
        self.CR = 0.9  	
        self.MR = 0.9      
        self.iterations  = 50     
        self.popSize = 100       
        self.pop = []       
        self.maxFunEval = 900000    
        self.funEval = 0		
        self.bestFitness = 99999999  
        self.bestChromosome = []     
        self.no_of_cells=self.p.getNoOfCells()

    def Init(self):
        for i in range (0, self.popSize):
            chromosome = self.p.makeRandomPath()
            fitness=self.p.pathFitness(chromosome)
            self.funEval = self.funEval + 1
            newIndividual = Individual(chromosome,fitness)
            self.pop.append(newIndividual)
        
    def MemoriseGlobalBest(self):
        for pi in self.pop:
            if pi.fitness < self.bestFitness:
                self.bestFitness=pi.fitness
                self.bestChromosome = deepcopy(pi.chromosome)

    def Crossover(self):
        for i in range(0,self.popSize):
    
            if (random.random() <= self.CR):
    
                # Choose two random indices
                i1,i2=random.sample(range(0,self.popSize), 2)
    
                # Parents
                p1=deepcopy(self.pop[i1])
                p2=deepcopy(self.pop[i2])
    
                # Choose a crossover point 
                pt = random.randint(1,self.no_of_cells)
    
                # Generate new childs 
                c1=p1.chromosome[0:pt] + p2.chromosome[pt:]
                c2=p2.chromosome[0:pt] + p1.chromosome[pt:]
    
                # Get the fitness of childs 
                c1Fitness=self.p.pathFitness(c1)
                self.funEval = self.funEval + 1
                c2Fitness=self.p.pathFitness(c2)
                self.funEval = self.funEval + 1
    
                # Select between parent and child
                if c1Fitness < p1.fitness:
                    self.pop[i1].fitness=c1Fitness
                    self.pop[i1].chromosome=c1
                    
                if c2Fitness < p2.fitness:
                    self.pop[i2].fitness=c2Fitness
                    self.pop[i2].chromosome=c2


# Function 5: Perform Mutation Operation
    def Mutation(self):
        for i in range(0,self.popSize):
    
            if (random.random() <= self.MR):
                
                # Choose random index
                r=random.randint(0,self.popSize-1)
    
                # Choose a parent
                p=deepcopy(self.pop[r])
    
                # Choose mutation point 
                pt = random.randint(0,self.no_of_cells-1)    
                
                # Generate new childs
                c=deepcopy(p.chromosome)
    
                # Mutation
                c[pt] = round(random.randint(1,8))
    
                #Get the fitness of childs
                cFitness=self.p.pathFitness(c)
                self.funEval = self.funEval + 1
                # Select between parent and child
                if cFitness < p.fitness:
                    self.pop[r].fitness=cFitness
                    self.pop[r].chromosome=c
  


    def DoOptimization(self):
        self.Init()
        self.globalBest=self.pop[0].chromosome
        self.globalBestFitness=self.pop[0].fitness
        self.MemoriseGlobalBest()
        
        
        for i in range(0,self.iterations):
            self.Crossover()
            self.Mutation()
            self.MemoriseGlobalBest()
        	
            if self.funEval >= self.maxFunEval:
                break
        
            if i%10==0:
                print "Iter done:",i,"\t Fitness:", self.bestFitness
                
        
        print "Iterations total:",i+1,"\t Fitness:", self.bestFitness

        
        print "Done"
        print "\nBestFitness:", self.bestFitness
        print "Best chromosome:", self.bestChromosome
        print "cell coverred" ,self.p.checkPathCells(self.bestChromosome)
        print "optimization efficiency",float(self.p.checkPathCells(self.bestChromosome))/float(self.no_of_cells)*100," %"
        print "Total Function funEval: ",self.funEval






# -*- coding: utf-8 -*-

