import sys
from  utils import*

class Game:
    def __init__(self, nRows, nCols, points):
        self.nRows =  nRows
        self.nCols = nCols
        self.board = []
        #Decoding the solution of chromosome to a board of M[][]
        self.decodeChromosome(points,nRows,nCols)

    def decodeChromosome(self,points,nRows,nCols):
        for i in range(nRows):
            b = []
            for j in range(nCols):
                b.append([False])
            self.board.append(b)
            #end for
        #end for
        i = 0
        while i < len(points):
            self.board[i//nRows][i%nCols] = points[i]
            i += 1
    #end def
#end class
class Rules:
    def __init__(self,rows, cols):
        self.rows = rows
        self.cols = cols

if __name__ == "__main__":
    
    if len(sys.argv) != 3:
        print("Error. Verifique que se tenga el file de entrada y salida!")
        print("Sintaxis correcta: python3 nonogram.py input_name.txt output_name.ppm ")
        exit()
        
    M = [[0, 0, 0, 1, 1], 
         [1, 1, 1, 0, 0], 
         [1, 1, 0, 1, 0], 
         [1, 1, 1, 1, 0], 
         [1, 1, 0, 1, 1]]
    
    print_board(M)
    cols, rows = read_file(sys.argv[1])
    write_file(M, sys.argv[2])