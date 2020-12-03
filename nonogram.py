import sys
from utils import*
import numpy as ny
import random as rnd


class Game:
    def __init__(self, nRows, nCols, points):
        self.nRows = nRows
        self.nCols = nCols
        self.board = []
        # Decoding the solution of chromosome to a board of M[][]
        self.decodeChromosome(points, nRows, nCols)

    def decodeChromosome(self, points, nRows, nCols):
        for i in range(nRows):
            b = []
            for j in range(nCols):
                b.append([False])
            self.board.append(b)
            # end for
        # end for
        i = 0
        while i < len(points):
            self.board[i//nRows][i % nCols] = points[i]
            i += 1
    # end def
# end class
class Rules:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
class Chromosome:
    def __init__(self, solution, rules, nRows, nCols):
        self.solution = solution
        self.fitness = calculateFitness(solution, rules, nRows, nCols)
        print(self.fitness)
# end class
def GeneticAlgorithm(constrains):
    rules, nRows, nCols, nPoints, populationSize = constrains
    Population = initSolutions(rules, nRows, nCols, populationSize)

def initSolutions(rules, nRows, nCols, populationSize):
    Solutions = []
    print("Initializating the population ==> with size: ", populationSize)
    for c in range(populationSize):
        newChromosome = []
        for i in range(nCols*nRows):
            # init of each positions of de chromosome
            if rnd.random() <= 0.5:
                newChromosome.append(True)
            else:
                newChromosome.append(False)
            # end if
        print(newChromosome)
        C = Chromosome(newChromosome, rules, nRows, nCols)
        Solutions.append(C)
        # end for
    return Solutions
def createConstraints(rules, nPopulation):
    nRows = len(rules.rows)
    nCols = len(rules.cols)
    nPoints = 0
    #Numero de puntos que hay que pintar en el nonograma
    for i in rules.rows:
        for j in i:
            nPoints += j
    return (rules, nRows, nCols, nPoints, nPopulation)

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Error. Verifique que se tenga el file de entrada y salida!")
        print("Sintaxis correcta: python3 nonogram.py nPopulation input_name.txt output_name.ppm ")
        exit()

    cols, rows = read_file(sys.argv[2])
    rules = Rules(rows, cols)
    constraints = createConstraints(rules,int(sys.argv[1]))
    GeneticAlgorithm(constraints)