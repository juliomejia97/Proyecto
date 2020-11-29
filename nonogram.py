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

#La entrada inicial del tablero hay -1
def solveNonogram_aux(M, positions,i,cols, rows):
    if i == len(positions):
        return isValidNonogram(M, cols, rows)
    else:
        p = positions[i]
        v = 0
        stop = False
        while v < 2 and not stop:
            M[p[0]][p[1]] = v
            if isValidNonogram(M, cols, rows):
                #Caso 1:
                    # Ver si vector está en 0, paso al la columna siguiente
                #Caso 2
                    # Si llene pero faltan más cuadrados pongo un espacio en mi siguiente fila
                if solveNonogram_aux(M,positions,i+1,cols, rows):
                    stop = True
                else:
                    v +=1
                #end if
            else: #No soy valido
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
        #Genero todas las posibles posibles combinaciones
    
#Validación
#Convenciones:
    #-1 no he puesto nada
    #0 es negra
    #1 es vacia
def isValidNonogram(M,cols, rows):
    #Casos que no son válidos
        #1. Verificar números aislados, si no llegan a 0 no sirven
        #2. Si llego a 0 y tengo un número siguiente, la siguiente casilla debe ser 0
    #Verificar por filas        
    #Verficar por columnas
#Salida a formato PGM
