v_filas = int(input("Ingrese el tamaño del árbol: "));

v_i = 1;

v_figura = "*";
v_espacios = v_filas - 1;

v_estrella = " " * v_espacios + "X";

print(v_estrella);

while(v_i <= v_filas):
    print(" " * v_espacios + v_figura);
    v_figura += "**";
    
    v_espacios -= 1;
    v_i += 1;

print(" " * (v_filas - 1) + "*");
#  X
#  *
# ***
#*****
#  *

# la cantidad de asteriscos no va ser igual a la cantidad de filas
#   *       # 1 + 2
#  ***      # 3 + 2
# *****     # 5 + 2
#*******    # 7 + 2

#    *
#   ***
#  *****
# *******
#*********


