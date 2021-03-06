""" Python Package Support """
import random
import numpy
import math

""" Internal Package Support """
#Not Applicable

"""
    @author:     Matthew J Swann
    @version:    1.0, Last Update: 2012-11-30
    
    Program:     Reflective Optimization
    Integration: Tier 1B-Beta
    
    Representation of the second of two Continuous Space problems to be
    encoded and solved via Simulated Annealing. Greater integration into
    a set of five algorithmic comparisons for reflective optimization
    upon the Simulated Annealing algorithm itself.  
    
    This is the Branin Function. 
    Known optima at ::    (9.42478, 2.475)
                          (pi , 2.275)
                          (-pi , 12.275)
 """

class FunctionTwo(object):

    """
     Object initialization. Sentinel values set on bestSolution.
     Random uniform generation for each coordinate value.
     """
    def __init__(self):
        """ random seed generation """
        self.x = random.uniform(-2, 3)
        self.y = random.uniform(-2, 3)
        """ variable initialization """
        self.currentSolution = 0
        self.bestSolution = 100
        self.bestX = 0
        self.bestY = 0
        """ setup """
        self.solve()
        
        
    """
     Solves the Six Hump CamelBack Function for the current X & Y 
     coordinate values. Also updates superlative variables.
     
     @return: currentSolution -- current cost evaluation
     """
    def solve(self):
        x = self.x
        y = self.y
        self.currentSolution = (numpy.square(y-(5.1/(4*numpy.square(math.pi)))*numpy.square(x) +
                (5/math.pi)*x - 6) + 10*(1-(1./(8*math.pi)))*numpy.cos(x) + 10)
        
        if self.currentSolution < self.bestSolution:
            self.bestSolution = self.currentSolution
            self.bestX = x
            self.bestY = y 
        return self.currentSolution


    """
     Checks the passed value for both X and Y and then sets the
     variables appropriately.
     
     @param newX: New value to be assigned to the x coord.
     @param newY: New value to be assigned to the y coord.
     """
    def processValues(self, newX, newY):
        self.checkSetX(newX)
        self.checkSetY(newY)
        return self.solve()


    """
     Verifies the value passed as a number within the range of
     -5 to 10.
    
     @param newInput: Value to be verified and assigned to the
     x coord.
     """ 
    def checkSetX(self, newInput):
        if newInput > 10:
            self.x = newInput-15
        elif newInput < -5:
            self.x = newInput+15
        else:
            self.x = newInput
            
 
    """
     Verifies the value passed as a number within the range of
     0 to 15.
    
     @param newInput: Value to be verified and assigned to the
     y coord.
     """           
    def checkSetY(self, newInput):
        if newInput > 15:
            self.y = newInput -15
        elif newInput < 0:
            self.y = newInput+15
        else:
            self.y = newInput


    """
     Sets the X & Y coords. Used to reset values if move is NOT
     made.
     
     @param xVar: old X coord value
     @param yVar: old Y coord value
     """
    def setVars(self, xVar, yVar):
        self.x = xVar
        self.y = yVar


    """
     Prints an updated administrative report.
     """
    def admin(self):
        print("<-- Function Two Report -->")
        print("  BestSol: %s" % self.getBestCost())
        print("  Best X:  %s" % self.getBestX())
        print("  Best Y:  %s" % self.getBestY())


    """
     Basic accessor methods.
     
     @return: x -- current x coord
     @return: y -- current y coord
     @return: currentSolution -- current cost evaluation
     @return: bestX -- x coord for best solution
     @return: bestY -- y coord for best solution
     @return: bestSolution -- best cost evaluation
     """        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y 
    
    def getCurrentCost(self):
        return self.currentSolution
    
    def getBestX(self):
        return self.bestX
    
    def getBestY(self):
        return self.bestY
    
    def getBestCost(self):
        return self.bestSolution
        