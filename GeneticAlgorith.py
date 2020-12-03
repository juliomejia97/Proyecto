import numpy as ny
import sys
import random as rnd
from utils import calculateFitness
class Chromosome:
    def __init___(self,solution, constrains):
        self.solution = solution
        #TODO: Acá se calcula el fitness del chormosoma
        self.fitness = calculateFitness(solution, constrains)

def GeneticAlgorithm(constrains):
    rules, nRows, nCols, nPoints, populationSize = constrains
    Population = initSolutions(constrains)



def initSolutions(constrains):
    rules, nRows, nCols, nPoints, populationSize = constrains
    Solutions = []
    print("Initializating the population ==> with size: ",populationSize)
    for c in range(populationSize):
        newChromosome = []
        for i in range(nCols*nRows):
            #init of each positions of de chromosome
            if rnd.random() <= 0.5:
                newChromosome.append(True)
            else:
                newChromosome.append(False)
            #end if
        Solutions.append(Chromosome(newChromosome,constrains))
        #end for
    return Solutions