""" Python Package Support """
import random
import math
import abc

""" Internal Package Support """
from SimulatedAnnealing import SimulatedAnnealing as SimAnn


"""
    @author:     Matthew J Swann
    @version:    1.0, Last Update: 2012-11-20
    
    Program:     Reflective Optimization
    Integration: Tier 2
    
    Optimization classes to be run upon the SA Algorithm
    itself.  
"""

class SA_Omega(object):
    __metaclass__ = abc.ABCMeta

    """
     Constructor for the SA Optimizers.
     
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
        """ SA Initialization """
        self.SA = SimAnn(funcNum, initTemp, extIters,
                 intIters, moveCont, localSearch, expand)
        """ Instance variables """
        self.currentTemp = 100                 # Current temperature tracking
        self.currentSolution = None            # Current solution
        self.bestSolution = 999999             # Best solution found
        self.bestMoves = None                  #""" what is this for?? """
        
    @abc.abstractmethod
    def SA(self):
        """ Simulated Annealing Algorithm """
        return
        
    @abc.abstractmethod
    def randomMove(self):
        """ Random movement """
        return
        
    @abc.abstractmethod
    def getCurrentTemp(self):
        """ Returns current temp """
        return
    
    @abc.abstractmethod
    def getBestSolution(self):
        """ Returns best solution """
        return
    
    @abc.abstractmethod
    def getBestMoves(self):
        """ Returns number of attempts to best sol """
        return
"""
 External Iteration optimization
 
 Parent Class -- SA_Omega
 """           
class SA_Alpha(SA_Omega):    
    
    def SA(self):
        print("concrete SA")
    
    def randomMove(self):
        print("random")
 
 
    """
     Basic accessors.
     
     @return: currentTemp -- current temp
     @return: bestSolution -- best found solution
     @return: bestMoves -- how long to find best
     """    
    def getCurrentTemp(self):
        return self.currentTemp
    
    def getBestSolution(self):
        return self.bestSolution
    
    def getBestMoves(self):
        return self.bestMoves
        
        