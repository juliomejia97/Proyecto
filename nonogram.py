#La entrada inicial del tablero hay -1
import sys
#Lectura de archivo
def read_file(input):
    
    cols = []
    rows = []
    
    with open (input) as file_input:
        file_col = file_input.readline()
        file_row = file_input.readline()
    
    #Split inicial de cada fila o columna
    ind_col = file_col.split(" ")
    ind_row = file_row.split(" ")
    
    #Se hace el split final del pipe a los elementos de cada fila o columna si es necesario
    for i in ind_col:
        col = i.strip()
        cols.append(col.split("|"))
        
    for i in ind_row:
        row = i.strip()
        rows.append(row.split("|"))
    
    return cols, rows

    
def solveNonogram_aux(M, positions,i,constrains):
    if i == len(positions):
        return isValidNonogram(M, constrains)
    else:
        p = positions[i]
        v = 0
        stop = False
        while v < 2 and not stop:
            M[p[0]][p[1]] = v
            if isValidNonogram(M, constrains):
                if solveNonogram_aux(M,positions,i+1,constrains):
                    stop = True
                else:
                    v +=1
                #end if
            else:
                v +=1
            #end if
        #end while
        if stop:
            return True
        else:
            M[p[0]][p[1]] = 0
            return False
    #end if
#end def

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("Error. Se necesita un argumento con el input a leer!")
    else:
        cols, rows = read_file(sys.argv[1])
    
#Validación
def isValidNonogram(M,constrains):
    return True
#Salida a formato PGM
