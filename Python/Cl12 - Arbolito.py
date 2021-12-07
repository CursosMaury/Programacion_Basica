v_filas = 0;
v_espacio = "";

v_filas = int(input("Ingrese el tamaño del arbol: "));

while (v_filas != 0):
    if (v_filas == 1):
        print(f"{v_espacio}\/", end="");
        v_filas -= 1;
    else:
        v_columnas = 2 * v_filas;

        while(v_columnas != 0):
            if(v_columnas == 2 * v_filas):
                print(f"{v_espacio}\\", end="");
            elif (v_columnas == 1):
                print("/", end="");
            else:
                print(v_filas - 1, end="");
        
            v_columnas -= 1;

        print("");
        v_espacio += " ";
        v_filas -= 1;