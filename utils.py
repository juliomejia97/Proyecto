import nonogram as ng
import numpy as numpy
import sys

def calculateFitness(solution, rules,nRows,nCols):
    #Contar cuántas pistas se están cumpliento
    FO = 0
    game = ng.Game(nRows,nCols,solution)
    solEvaluate = solution
    
    #Contar reglas que se cumplen en filas
    for i in range(nRows):
        nReglas = len(rules.rows[i])
        columnIndex = 0
        indexR = 0
        while columnIndex < nCols or indexR < nReglas:
            contP = 0
            #Si no tengo más reglas en mi solución
            if (indexR  < nReglas):
                reglaActual = rules.rows[i][indexR]
            else:
                reglaActual = 0
            #Verificar espacios
            while columnIndex < nCols and not solEvaluate[i*nCols + columnIndex]:
                columnIndex +=1
            #end while
            #Verificar negritos
            while columnIndex < nCols and solEvaluate[i*nCols + columnIndex]:
                contP += 1
                columnIndex +=1
            #end while
            FO += abs(reglaActual - contP)
            indexR +=1
        #end while
    #end for

    #Contar reglas que se cumplen en columnas
    for j in range(nCols):
        nReglas = len(rules.cols[j])
        rowIndex = 0
        indexR = 0
        while rowIndex < nRows or indexR  < nReglas:
            contP = 0
            if (indexR  < nReglas):
                reglaActual = rules.cols[j][indexR]
            else:
                reglaActual = 0
            #Verficar Espacios
            while rowIndex < nRows and not solEvaluate[rowIndex*nRows + j]:
                rowIndex +=1
            #end while
            #Verificar negritos
            while rowIndex < nRows and solEvaluate[rowIndex*nRows + j]:
                contP += 1
                rowIndex += 1
            #end while
            FO += abs(reglaActual - contP)
            indexR +=1
        #end while
    #end for
    return 1/FO if FO!=0 else 0
                
        
        


#Lectura de archivo
def read_file(input):
    
    cols = []
    rows = []
    
    with open (input) as file_input:
        file_col = file_input.readline()
        file_row = file_input.readline()
    
    file_input.close()
    
    #Split inicial de cada fila o columna
    ind_col = file_col.split(" ")
    ind_row = file_row.split(" ")
    
    #Se hace el split final del pipe a los elementos de cada fila o columna si es necesario
    for i in ind_col:
        col = i.strip()
        cols.append(col.split("|"))
        for c in cols:
            for c2 in range(len(c)):
                c[c2] = int(c[c2])
        #end for
    #end for
        
    for i in ind_row:
        row = i.strip()
        rows.append(row.split("|"))
        for r in rows:
            for r2 in range(len(r)):
                r[r2] = int(r[r2])
            #end for
        #end for
    #end for
    
    return cols, rows
#end def

def print_board(M):
    for i in range(len(M[0])):
        print()
        for j in range(len(M)):
            print(str(M[i][j]) + "\t", end="")
    print()

#Salida a formato PGM
def write_file(M, output):
    with open(output, "w") as file_output:
        file_output.write("P5\n")
        file_output.write(str(len(M[0])) + " " + str(len(M)) + "\n")
        file_output.write("255\n")
        for row in range(len(M)):
            for col in range(len(M[0])):
                if M[row][col] == 0:
                    file_output.write("0 ")
                else:
                    file_output.write("255 ")
    file_output.close()
