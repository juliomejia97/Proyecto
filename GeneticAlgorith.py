import numpy as ny
import sys
import random as rnd
from utils import calculateFitness
class Chromosome:
    def __init___(self,solution, rules,nRows,nCols):
        self.solution = solution
        self.fitness = calculateFitness(solution,rules,nRows,nCols)

def GeneticAlgorithm(constrains):
    rules, nRows, nCols, nPoints, populationSize = constrains
    Population = initSolutions(rules, nRows,nCols,populationSize)

def initSolutions(rules, nRows, nCols, populationSize):
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
        Solutions.append(Chromosome(newChromosome,rules, nRows, nCols))
        #end for
    return Solutions