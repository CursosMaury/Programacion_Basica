# Son algotimos que se encargan de ordenar de forma
# específica un arreglo (o lista) en un orden concreto.

# Ordenamientos de números, ascendente y descendete.


# Ordenamiento por Selección (Selectsort)

"""

-------------------------
| 4 | 3 | 1 | 5 | 0 | 2 | 6 posiciones 0, 1, 2, 3, 4, 5 -> ascendente
-------------------------

  -   - 
-------------------------
| 4 | 3 | 1 | 5 | 0 | 2 | si (4 > 3) 
-------------------------

  -   -
-------------------------
| 3 | 4 | 1 | 5 | 0 | 2 | cambio
-------------------------
  -       -
-------------------------
| 3 | 4 | 1 | 5 | 0 | 2 | si (3 > 1) -> cambiar
-------------------------

  -       -
-------------------------
| 1 | 4 | 3 | 5 | 0 | 2 | cambio
-------------------------

  -           -
-------------------------
| 1 | 4 | 3 | 5 | 0 | 2 | si (1 > 5) -> no se hace nada
-------------------------

  -               -
-------------------------
| 1 | 4 | 3 | 5 | 0 | 2 | si (1 > 0) -> cambiar
-------------------------

  -               -
-------------------------
| 0 | 4 | 3 | 5 | 1 | 2 | cambio 
-------------------------
  -                   -
-------------------------
| 0 | 4 | 3 | 5 | 1 | 2 | si (0 > 2) -> no se hace nada
-------------------------

      -   -
-------------------------
| 0 | 4 | 3 | 5 | 1 | 2 | si (4 > 3) -> cambiar
-------------------------

      -   -
-------------------------
| 0 | 3 | 4 | 5 | 1 | 2 | cambio
-------------------------

      -       -
-------------------------
| 0 | 3 | 4 | 5 | 1 | 2 | si (3 > 5) -> no se hace nada
-------------------------

      -           -
-------------------------
| 0 | 3 | 4 | 5 | 1 | 2 | si (3 > 1) -> cambiar
-------------------------

      -           -
-------------------------
| 0 | 1 | 4 | 5 | 3 | 2 | cambio
-------------------------

      -               -
-------------------------
| 0 | 1 | 4 | 5 | 3 | 2 | si (1 > 2) -> no se hace nada
-------------------------

          -   -
-------------------------
| 0 | 1 | 4 | 5 | 3 | 2 | si (4 > 5) -> no se hace nada
-------------------------

          -       -
-------------------------
| 0 | 1 | 4 | 5 | 3 | 2 | si (4 > 3) -> cambiar 
-------------------------

          -       -
-------------------------
| 0 | 1 | 3 | 5 | 4 | 2 | cambio
-------------------------

          -           -
-------------------------
| 0 | 1 | 3 | 5 | 4 | 2 | si (3 > 2) -> cambiar
-------------------------

          -           -
-------------------------
| 0 | 1 | 2 | 5 | 4 | 3 | cambio 
-------------------------

              -   -
-------------------------
| 0 | 1 | 2 | 5 | 4 | 3 | si (5 > 4) -> cambiar
-------------------------

              -   -
-------------------------
| 0 | 1 | 2 | 4 | 5 | 3 | cambio
-------------------------

              -       -
-------------------------
| 0 | 1 | 2 | 4 | 5 | 3 | si (4 > 3) -> cambiar
-------------------------

              -       -
-------------------------
| 0 | 1 | 2 | 3 | 5 | 4 | cambio 
-------------------------

                  -   -
-------------------------
| 0 | 1 | 2 | 3 | 5 | 4 | si (5 > 4) -> cambiar
-------------------------

                  -   -
-------------------------
| 0 | 1 | 2 | 3 | 4 | 5 | cambio
-------------------------

El arreglo esta ordenado :3

-------------------------
| 0 | 1 | 2 | 3 | 4 | 5 | 
-------------------------

"""
        #  0  1  2  3  4  5 
arreglo = [4, 3, 1, 5, 0, 2];

i = 0;
j = i + 1;

# i empiza en 0 y termina en la penultima posición
# j empieza en i + 1 y termina en la última posición

print(arreglo)

while (i < 5):
    while(j < 6):

        if (arreglo[i] < arreglo[j]): # si es verdadero se hace el cambio
            temp = arreglo[i] # 4
            arreglo[i] = arreglo[j] # 4, 3 -> arreglo[i] = 3, arreglo[j] = 3
            arreglo[j] = temp # -> arreglo[j] = 4

        j += 1
    i += 1
    j = i + 1;

print(arreglo)