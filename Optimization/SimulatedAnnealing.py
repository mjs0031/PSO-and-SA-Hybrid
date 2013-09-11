""" Python Package Support """
import random
import math
import sys

""" Internal Package Support """
from FunctionOne import FunctionOne
from FunctionTwo import FunctionTwo


"""
    @author:     Matthew J Swann
    @version:    1.0, Last Update: 2012-11-30
    
    Program:     Reflective Optimization
    Integration: Tier 1A
    
    Simulated Annealing algorithm used to solve the continuous space
    problems. This SA follows a very basic structure and confirms with
    the generally accepted implementation of SA at large.    
"""

class SimulatedAnnealing(object):

    """
     Initialization for the BASIC SA level
     
     @param funcNum: Number 1 or (other) :: control for the Function
         class to be evaluated
     @param initTemp:    Initial temperature
     @param extIters:    External iterations
     @param intIters:    Internal iterations
     @param moveCont:    Alpha value // move control
     @param localSearch: Local Search control
     @param expand:      Re-heat // tempering mechanism
     """
    def __init__(self, funcNum, initTemp, extIters, intIters, 
                 moveCont, localSearch, expand):
        """ Parameters """
        if(funcNum == 1):
            self.FX = FunctionOne()  # Six Hump Camelback Function for Eval
            self.range = 0.5
            self.goal = -1.031628453488552
        else:
            self.FX = FunctionTwo()  # Branin Function for Eval
            self.range = 1.5
            self.goal = 0.39788735775266204
        self.initialTemp = initTemp  # Initial temperature
        self.external = extIters     # External Iterations for the SA Algorithm
        self.internal = intIters     # Internal iterations for the SA Algorithm
        self.alpha = moveCont        # Alpha value // Move control
        self.drillBit = localSearch  # Control for local search
        self.expansion = expand      # Re-heat
        """ Instance variables """
        self.currentTemp = self.initialTemp    # Current temperature tracking
        self.currentSolution = None            # Current solution
        self.bestSolution = 9999               # Best solution found
        self.bestX = None                      # X coord for best solution
        self.bestY = None                      # Y coord for best solution
        self.totalMoves = 0                    # Attempted moves
        self.movesAccepted = 0                 # Accepted moves
        self.movesToTarget = 0                 # Moves to goal value
        self.targetHits = 0                    # Times landed on target
        self.resets = 0                        # Temperature resets
        self.SA()    

    """
     The Simulated Annealing Algorithm itself.
     """
    def SA(self):
        import time
        time.clock()
        for i in range (self.external):
            for j in range (self.internal):
                """ saving values if needed later """
                xStore = self.FX.getX()
                yStore = self.FX.getY() 
                
                self.randomStep()
                if(self.currentSolution < self.bestSolution):
                    self.bestSolution = self.currentSolution
                    self.bestX = self.FX.getX()
                    self.bestY = self.FX.getY()
                    self.totalMoves = self.totalMoves + 1
                    self.movesAccepted = self.movesAccepted + 1
                    if ((self.goal - self.currentSolution) > -0.00005):
                        print("<------GOAL------->")
                        print(self.goal-self.currentSolution)
                        if(self.movesToTarget == 0):
                            self.movesToTarget = self.movesAccepted            
                else:
                    randomNum = random.uniform(0, 1)
                    if(randomNum > math.exp((self.currentSolution-self.bestSolution)/self.currentTemp)):
                        self.FX.setVars(xStore, yStore)
                        self.totalMoves = self.totalMoves + 1
                    else:
                        self.totalMoves = self.totalMoves + 1
                        self.movesAccepted = self.movesAccepted + 1                        
            """ Temperature Updates """           
            self.currentTemp = self.currentTemp*self.alpha
            if(self.currentTemp < 1):
                self.currentTemp = self.initialTemp
                self.resets = self.resets + 1
        print("-----------------------")
        print("best solution: %s" % self.bestSolution)
        print("time:")
        print(time.clock())
        
        if ('time' in sys.modules.keys()):
            del(sys.modules['time'])

    """
     Random neighborhood step based off the range of the neighborhood
     set in the SA constructor.
     
     Sets the currentSolution variable.
     """
    def randomStep(self):
        """ X update """
        x = self.FX.getX()
        if random.randint(0, 1) == 1:
            if(self.drillBit):
                x = (x - random.uniform(0, self.range)*self.currentTemp/self.initialTemp)
            else:
                x = (x - random.uniform(0, self.range))
        else:
            if(self.drillBit):
                x = (x + random.uniform(0, self.range)*self.currentTemp/self.initialTemp)
            else:
                x = (x + random.uniform(0, self.range))
        """ Y update """
        y = self.FX.getY()
        if random.randint(0, 1) == 1:
            if(self.drillBit):
                y = (y - random.uniform(0, self.range)*self.currentTemp/self.initialTemp)
            else:
                y = (y - random.uniform(0, self.range))
        else:
            if(self.drillBit):
                y = (y + random.uniform(0, self.range)*self.currentTemp/self.initialTemp)
            else:
                y = (y + random.uniform(0, self.range))
        """ Process updates """
        self.currentSolution = self.FX.processValues(x, y)


    """
     Resets the instance variables and sets the FX coords to the
     pass parameters.
     
     @param xCoord: associated x coord
     @param yCoord: associated y coord
     """
    def setVariables(self, xCoord, yCoord):
        """ reset instance variables """
        self.currentTemp = self.initialTemp    # Current temperature tracking
        self.currentSolution = None            # Current solution
        self.bestSolution = 9999               # Best solution found
        self.bestX = None                      # X coord for best solution
        self.bestY = None                      # Y coord for best solution
        self.totalMoves = 0                    # Attempted moves
        self.movesAccepted = 0                 # Accepted moves
        self.movesToTarget = 0                 # Moves to goal value
        self.targetHits = 0                    # Times landed on target
        self.resets = 0                        # Temperature resets
        """ set Function coords """
        self.FX.setVars(xCoord, yCoord)


    """
     Sets basic algorithmic values
     
     @param value: New value for the algorithmic control
     values.
     """
    def setInitTemp(self, value):
        self.initialTemp = value
        self.currentTemp = value
        
    def setMoveControl(self, value):
        self.alpha = value
        
    def setExternal(self, value):
        self.external = value
        
    def setInternal(self, value):
        self.internal = value
        
    """
     Returns algorithmic values
     
     @return: Returns the algorithmic values.
     """
    def getInitTemp(self):
        return self.initialTemp
    
    def getMoveControl(self):
        return self.alpha
    
    def getExternal(self):
        return self.external
    
    def getInternal(self):
        return self.internal

    """
     Basic accessor methods.
     
     @return: currentTemp --   current system temperature
     @return: bestSolution --  best known solution
     @return: bestX --         x coord for best solution
     @return: bestY --         y coord for best solution
     @return: totalMoves --    total moves attempted
     @return: movesAccepted -- accepted moves
     @return: movesToTarget -- moves to target value
     """
    def getCurrentTemp(self):
        return self.currentTemp
    
    def getBestSolution(self):
        return self.bestSolution
    
    def getBestX(self):
        return self.bestX
    
    def getBestY(self):
        return self.bestY
    
    def getTotalMoves(self):
        return self.totalMoves
    
    def getMovesAccepted(self):
        return self.movesAccepted
    
    def getMovesToTarget(self):
        return self.movesToTarget
