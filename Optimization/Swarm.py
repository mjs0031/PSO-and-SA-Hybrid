""" Python Package Support """
import random

""" Internal Package Support """
from Hive import Hive

"""
    @author:     Matthew J Swann
    @version:    1.0, Last Update: 2012-11-30
    
    Program:     Reflective Optimization
    Integration: Tier 3
    
    Swarm representation for the swarm/annealing
    hybrid. 
 """
 
class Swarm(object):
     
    """
     Constructor for the swarm.
     
     @param popSize:        Swarm size
     @param phi_One:        Phi1 multiplier
     @param phi_Two:        Phi2 multiplier
     @param inertia_value:  Omega dampening multiplier
     @param constant_value: Kappa value
     """
    def __init__(self, popSize, phi_One, phi_Two, inertia_value,
                 constant_value, funcNum):
        """ Constructor Parameters """
        self.populationSize = popSize
        self.phiOne = phi_One
        self.phiTwo = phi_Two
        self.intertia = inertia_value
        self.constant = constant_value
        """ Best Values """
        self.bestX = 5000
        self.bestY = 5000
        self.bestCost = 5000
        self.bestParticle = 0
        """ Function Variable """
        self.iterations = 1
        self.theHive = Hive(popSize, funcNum)
        self.theHive.sortListFitness()
        self.population = self.theHive.getPopulation()
        self.adminUpdate()


    """
     Updates the velocities and then anneals at the new locations. 
     Finally, sorts based on fitness
     """
    def updateWithVels(self):
        self.iterations = self.iterations + 1
        for i in range (len(self.population)):
            newx = self.calcXVelocity(self.population[i])
            newx = self.population[i].FX.getBestX()+newx
            newy = self.calcYVelocity(self.population[i])
            newy = self.population[i].FX.getBestY()+newy
            self.population[i].FX.setVars(newx, newy)
        self.theHive.population = self.population
        self.theHive.SimAnn()
        self.theHive.sortListFitness()
        self.population = self.theHive.getPopulation()
        self.adminUpdate()

        

    """
     Calculates the current velocity for X based on global statistics.
     
     @param particle: The particle to be evaluated.
     
     @return: Returns the new velocity for X.
     """
    def calcXVelocity(self, particle):
        Xbest = particle.FX.getBestX()
        Xcurrent = particle.FX.getX()
        Xvel = particle.FX.getXVelocity()
        velocity  = (self.constant*((self.intertia)*Xvel + 
                     self.phiOne*random.uniform(0, 1)*(self.bestX - Xcurrent) + 
                     self.phiTwo*random.uniform(0, 1)*(Xbest - Xcurrent)))
        if(velocity < -.15):
            velocity = -.15
        if(velocity > .15):
            velocity = .15
        return velocity

    
    """
     Calculates the current velocity for Y based on global statistics.
     
     @param particle: The particle to be evaluated.
     
     @return: Returns the new velocity for Y.
     """
    def calcYVelocity(self, particle):
        Ybest = particle.FX.getBestY()
        Ycurrent = particle.FX.getY()
        Yvel = particle.FX.getYVelocity()
        velocity  = (self.constant*((self.intertia)*Yvel + 
                     self.phiOne*random.uniform(0, 1)*(self.bestY - Ycurrent) + 
                     self.phiTwo*random.uniform(0, 1)*(Ybest - Ycurrent)))
        if(velocity < -1):
            velocity = -1
        if(velocity > 1):
            velocity = 1
        return velocity
    
    """
     Updates the best and second best variables.
     """
    def adminUpdate(self):
        for i in range (len(self.population)):
            self.checkSetBest(self.population[i].FX.getBestCost(), 
                              self.population[i].FX.getBestX(),
                              self.population[i].FX.getBestY(), 
                              self.population[i].FX.getID())
        self.swarmAdmin()
        
    """
     Checks and sets best values.
     
     @param value:  Current cost value.
     @param Xval:   X coord associated with current cost.
     @param Yval:   Y coord associated with current cost.
     @param pardId: Particle ID for tracking and selfless 
                     swarm option.
     """
    def checkSetBest(self, value, Xval, Yval, partId):
        if(value < self.bestCost):
            """ Update Best Set """
            self.bestCost = value
            self.bestParticle = partId
            self.bestX = Xval
            self.bestY = Yval
        else:
            """ Do nothing """
            pass

    """
     Returns the Hive object.
     
     @return: Returns theHive.
     """
    def getHive(self):
        return self.theHive
    
    """
     Outstream of important swarm statistics
     """
    def swarmAdmin(self):
        print("Swarm Admin -->>")
        print("        Iterations :: %s" % self.iterations)
        print("Best Sol: %s" % self.getBestCost())
        print("Best ID:  %s" % self.getBestParticle())
        print("Best X:   %s" % self.getBestX())
        print("Best Y:   %s" % self.getBestY())
 
       
    """
     Returns basic administrative variables.
     
     @return: bestCost - best known cost
     @return: bestPart - best known particle ID
     @return: bestX    - x coord for bestCost
     @return: bestY    - y coord or bestCost
     """
    def getBestCost(self):
        return self.bestCost
    
    def getBestParticle(self):
        return self.bestParticle
    
    def getBestX(self):
        return self.bestX
    
    def getBestY(self):
        return self.bestY
