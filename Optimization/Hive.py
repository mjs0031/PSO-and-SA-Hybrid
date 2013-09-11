""" Python Package Support """
import random

""" Internal Package Support """
from FunctionOne import FunctionOne
from FunctionTwo import FunctionTwo
from SimulatedAnnealing import SimulatedAnnealing

"""
    @author:     Matthew J Swann
    @version:    1.0, Last Update: 2012-11-30
    
    Program:     Particle Swarm Optimization for Continuous Function
    Integration: Tier 2A/B      
 """

class Hive(object):
    
    """ 
     Constructor taking a parameter for the size of the
     population.
     
     @param popSize: Size of the hive cluster.
     """
    def __init__(self, popSize, funcNum):
        self.function = funcNum
        self.populationSize = popSize
        self.population = list()
        """ Initialization """
        self.setup()
        

    
    """
     Initializes the hive cluster with particles containing
     random starting values. Best values are set within the
     appropriate values for the hive cluster itself.
     """
    def setup(self):
        for i in range (self.populationSize):
            particle = Particle(self.function)
            particle.setID(i)
            self.population.append(particle)
    
    
    """
     Sorts the population based off fitness.
     """
    def sortListFitness(self):
        for i in range (len(self.population)):
            for j in range (len(self.population)):
                if (self.population[i].getBestCost()) < (self.population[j].getBestCost()):
                    swap = self.population.pop(i)
                    self.population.insert(j, swap)
                    

    """
     Runs an SA on each particle.
     """
    def SimAnn(self):
        sim = SimulatedAnnealing(self.function, 100, 1000, 250, 
                                 .975, True, True)
        for i in range (len(self.population)):
            #print(sim.FX.getX())
            sim.setVariables(self.population[i].FX.getX(), self.population[i].FX.getY())
            sim.SA()
            self.population[i].FX.setVars(sim.getBestX(), sim.getBestY())
            self.population[i].FX.bestSolution = sim.bestSolution
            #print(self.population[i].FX.getX())
        self.sortListFitness()
        self.hiveAdmin()
        
    """
     Returns the population list.
     
     @return: Returns the population list.
     """    
    def getPopulation(self):
        return self.population

    
    """
     Calls particleAdmin() for each particle.
     """
    def hiveAdmin(self):
        for i in range (len(self.population)):
            self.population[i].particleAdmin()

"""
---------------------------------------
CLASS :: Particle
---------------------------------------

 Serves as a Hive entity.
 """
class Particle(object):

    """
     Constructor setting sentinel values. Also, calls
     for setup() generating random starting values and
     self evaluation. 
     """
    def __init__(self, funcNum):
        self.function = funcNum
        self.bestCost = 10000
        self.particleID = None
        self.velocity = None
        self.xVelocity = 0
        self.yVelocity = 0
        """ Initialization """
        self.setup()
        
        
    """
     Initialization for the particle object. Sets random
     values within specified range, solves and sets the
     initial solved values for as the currently best values.
     """
    def setup(self):
        if(self.function == 1):
            self.FX = FunctionOne()
        else:
            self.FX = FunctionTwo()

    
    """
     Sets x velocity value.    

     @param vel: X Velocity
     """
    def setXVelocity(self, vel):
        self.xVelocity = vel


    """
     Sets y velocity value.    

     @param vel: Y Velocity
     """
    def setYVelocity(self, vel):
        self.yVelocity = vel
    
    
    """
     Returns x velocity.
     
     @return: Returns the x velocity
     """
    def getXVelocity(self):
        return self.xVelocity
    
    
    """
     Returns y velocity.
     
     @return: Returns the y velocity
     """
    def getYVelocity(self):
        return self.yVelocity
    
        
    """
     Sets particle ID number
    
     @param value: Particle ID number
     """
    def setID(self, value):
        self.particleID = value
    
        
    """
     Returns particle ID number.
     
     @return: Returns particle ID number.
     """
    def getID(self):
        return self.particleID
    
 
    """
     Prints an admin output.
     """
    def particleAdmin(self):
        print("*** Particle Printout Start: %s -->" % self.particleID)
        print(self.FX.admin())
    
    """
     Returns bestCost, X and Y.
     
     @return: Best cost.
     @return: Best X
     @return: Best Y
     """
    def getBestCost(self):
        return self.FX.getBestCost()
    
    def getCurrentCost(self):
        return self.FX.getCurrentCost()
    
    def getBestX(self):
        return self.FX.getBestX()
    
    def getBestY(self):
        return self.FX.getBestY()
        