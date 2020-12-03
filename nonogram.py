import sys
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

#La entrada inicial del tablero hay -1
def solveNonogram_aux(M, positions,i,cols, rows):
    if i == len(positions):
        return isValidNonogram(M, cols, rows)
    else:
        print("Iteracion i: ",i,)
        print("----------------------")
        print_board(M)
        print("----------------------")
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
            M[p[0]][p[1]] = 1
            return False
    #end if
#end def

def solveNonogram(col, rows):
    M = [[-1 for j in range(len(rows))] for i in range(len(cols))]
    positions = []
    for i in range(len(rows)):
        for j in range(len(cols)):
            positions.append([i,j])
    print(positions)
    print(solveNonogram_aux(M,positions,0,cols,rows))
    print_board(M)
    
    
#Validación
    #Convenciones:
        #-1 no he puesto nada
        #0 es negra
        #1 es vacia
def isValidNonogram(M,cols, rows):
    #Verficar por columnas
    is_valid_col = validate_col(M, cols)
    #Verificar por filas
    is_valid_row = validate_row(M, rows)
    return is_valid_col and is_valid_row
#end def 

def validate_row(M, rows):
    col_len = len(M[0])
    for row in range(len(rows)):
        ver = []
        start = False
        counter = 0
        for col in range(col_len):
            if M[row][col] == 0:
                start = True
                counter += 1    
            elif M[row][col] == 1:
                if start == True:
                    ver.append(counter)
                    counter = 0
                    start = False
            #end if
        #end for
        if start == True:
            ver.append(counter)
        #end if
        if not validate_arrays(ver, rows[row]):
            return False 
        #end if
    #end for              
    return True
#end def

def validate_col(M, cols):
    row_len = len(M)
    for col in range(len(cols)):
        ver = []
        start = False
        counter = 0
        for row in range(row_len):
            if M[row][col] == 0:
                start = True
                counter += 1    
            elif M[row][col] == 1:
                if start == True:
                    ver.append(counter)
                    counter = 0
                    start = False
        if start == True:
            ver.append(counter)
        if not validate_arrays(ver, cols[col]):
            return False                
    return True

def validate_arrays(A, B):
    if len(A) > len(B):
        return False
    for i in range(len(A)):
        if A[i] > B[i]:
            return False
    return True

def print_board(M):
    for i in range(len(M[0])):
        print()
        for j in range(len(M)):
            print(str(M[i][j]) + " ", end="")
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
    solveNonogram(cols,rows)
    print(isValidNonogram(M, cols, rows))
    write_file(M, sys.argv[2])