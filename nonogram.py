from utils import*
import sys
import numpy as ny
import random as rnd
class Game:
    def __init__(self, nRows, nCols, points):
        self.nRows = nRows
        self.nCols = nCols
        self.board = []
        # Decoding the solution of chromosome to a board of M[][]
        self.decodeChromosome(points, nRows, nCols)
    #end def

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
            #print(i//nRows," ",i%nCols)
            aux = i//(nRows+1) if nRows!=nCols else i//nRows 
            self.board[aux][i % nCols] = points[i]
            i += 1
        #end while
    # end def
    
# end class

class Rules:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
    #end def
    
#end class
class Chromosome:
    def __init__(self, solution, rules, nRows, nCols):
        self.solution = solution
        self.fitness = calculateFitness(solution, rules, nRows, nCols)
    #end def

    def recalculateFitness(self,rules, nRows,nCols):
        self.fitness = calculateFitness(self.solution, rules, nRows, nCols)
    #end def
    
# end class

def GeneticAlgorithm(constrains):
    rules, nRows, nCols, nPoints, populationSize, probMutation, elitism = constrains
    #Init Population
    iterations = 1
    localIterations = 0
    localFO = 0
    Population = initSolutions(rules, nRows, nCols, populationSize)
    
    while not converge(Population):
        localFO = Population[0].fitness
        print("Generating the generation ==> ", iterations)
        #Cruzar
        Childs = cross(Population, populationSize, nPoints, rules, nRows, nCols)
        #Mutar
        mutation(Childs, probMutation, rules, nRows, nCols)
        #Escoger
        Population =  partialElitism(Population,Childs,elitism,populationSize,rules,nRows,nCols)
        print(Population[0].fitness)
        if localFO == Population[0].fitness:
            localIterations += 1
        
        if localIterations == 50:
            print("Initiating swap")
            swap(Population, localFO)
            localIterations = 0
        
        iterations += 1

    #end while
    return Game(nRows,nCols,Population[0].solution)
#end def

def initSolutions(rules, nRows, nCols, populationSize):
    Solutions = []
    print("Initializing the population ==> with size: ", populationSize)
    for c in range(populationSize):
        newChromosome = []
        for i in range(nCols*nRows):
            # init of each positions of de chromosome
            if rnd.random() <= 0.5:
                newChromosome.append(True)
            else:
                newChromosome.append(False)
            # end if
        C = Chromosome(newChromosome, rules, nRows, nCols)
        Solutions.append(C)
        # end for
    #end for
    return Solutions
#end def

def converge(P):
    if P[0].fitness == 0:
        return True
    return False

#TODO: Mejorar el cross
def cross(P,tamPopulation,nPoints,rules,nRows,nCols):
    
    Childs = []
    P.sort(key = lambda s: s.fitness,reverse = False)
    #Calcular el número de parejas
    sumFitness = sum(c.fitness for c in P)
    #TODO: Prob de padres 
    prob = [(i.fitness/sumFitness) for i in P]
    for p in range(tamPopulation//2):
        child1 = []
        child2 = []
        father1, father2 = ny.random.choice(P,p=prob,replace=False,size=2)
        for i in range(len(father1.solution)):
            #El hijo 1 hereda al mitad del p1 y la otra mitad del p2
            if(rnd.random() < 0.5):
                child1.append(father1.solution[i])
                child2.append(father2.solution[i])
            else:
                child1.append(father2.solution[i])
                child2.append(father1.solution[i])
            #end if
        #end for
        Childs.append(Chromosome(child1,rules,nRows,nCols))
        Childs.append(Chromosome(child2,rules,nRows,nCols))
    #end for
    return Childs
#end def

def mutation(Childs, probMutation,rules, nRows, nCols):
    for child in Childs:
        if rnd.random() < probMutation:
            pos = ny.random.randint(0, len(child.solution) - 1)
            if(child.solution[pos]):
                child.solution[pos] = False
            else:
                child.solution[pos] = True
            #end if
            child.recalculateFitness(rules, nRows, nCols)
        #end if
    #end for
#end def

def partialElitism(P,C,elitism, nPopulation, rules, nRows,nCols):
    unifided = P + C
    unifided.sort(key = lambda s: s.fitness,reverse = False)
    contPopulation = int(elitism*nPopulation)
    bests = unifided[:contPopulation]
    others = unifided[contPopulation:]
    nextPopulation = bests + ny.ndarray.tolist(ny.random.choice(others,size = nPopulation - contPopulation,replace=False))
    return nextPopulation
#end def

def swap(P, localFO):
    for i in range(len(P)):
        if P[i].fitness == localFO:
            P[i].solution = P[i].solution[len(P[i].solution) // 2:] + P[i].solution[:len(P[i].solution) // 2]
        #end if
    #end for
#end def
    
def createConstraints(rules, nPopulation, probMutation, elitism):
    nRows = len(rules.rows)
    nCols = len(rules.cols)
    nPoints = nRows*nCols
    #Numero de puntos que hay que pintar en el nonograma
    return (rules, nRows, nCols, nPoints, nPopulation,probMutation,elitism)
#end def

if __name__ == "__main__":

    if len(sys.argv) != 6:
        print("Error. Verifique que se tenga el file de entrada y salida!")
        print("Sintaxis correcta: python3 nonogram.py nPopulation probMutation elitsmPercentage input_name.txt output_name.ppm ")
        exit()

    cols, rows = read_file(sys.argv[4])
    rules = Rules(rows, cols)
    constraints = createConstraints(rules,int(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]))
    print(constraints)
    GameSolved = GeneticAlgorithm(constraints)
    print_board(GameSolved.board)
    write_file(GameSolved.board,sys.argv[5])
    