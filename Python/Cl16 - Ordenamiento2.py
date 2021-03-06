## Ordenamiento de burbuja (BubbleSort)

"""

-------------------------
| 4 | 3 | 1 | 5 | 0 | 2 | 6 posiciones 0, 1, 2, 3, 4, 5 -> ascendente
-------------------------

1ra iteración - primer while

  j  j+1
-------------------------
| 4 | 3 | 1 | 5 | 0 | 2 | si (4 > 3) -> cambiar
-------------------------

  j  j+1
-------------------------
| 3 | 4 | 1 | 5 | 0 | 2 | cambio 
-------------------------

      j  j+1
-------------------------
| 3 | 4 | 1 | 5 | 0 | 2 | si (4 > 1) -> no se hace nada
-------------------------

          j  j+1
-------------------------
| 3 | 4 | 1 | 5 | 0 | 2 | si (1 > 5) -> no se hace nada 
-------------------------

              j  j+1
-------------------------
| 3 | 4 | 1 | 5 | 0 | 2 | si (5 > 0) -> cambiar
-------------------------

              j  j+1
-------------------------
| 3 | 4 | 1 | 0 | 5 | 2 | cambio
-------------------------

                  j  j+1
-------------------------
| 3 | 4 | 1 | 0 | 5 | 2 | si (5 > 2) -> cambiar
-------------------------

                  j  j+1
-------------------------
| 3 | 4 | 1 | 0 | 2 | 5 | cambio
-------------------------

2da iteración

  j  j+1
-------------------------
| 3 | 4 | 1 | 0 | 2 | 5 | si (3 > 4) -> no se hace nada
-------------------------

      j  j+1
-------------------------
| 3 | 4 | 1 | 0 | 2 | 5 | si (4 > 1) -> cambiar
-------------------------

      j  j+1
-------------------------
| 3 | 1 | 4 | 0 | 2 | 5 | cambio
-------------------------

          j  j+1 
-------------------------
| 3 | 1 | 4 | 0 | 2 | 5 | si (4 > 0) -> cambiar
-------------------------

          j  j+1
-------------------------
| 3 | 1 | 0 | 4 | 2 | 5 | cambio
-------------------------

              j  j+1
-------------------------
| 3 | 1 | 0 | 4 | 2 | 5 | si (4 > 2) -> cambiar
-------------------------

              j  j+1                
-------------------------
| 3 | 1 | 0 | 2 | 4 | 5 | cambio
-------------------------



3ra iteración

  j  j+1
-------------------------
| 3 | 1 | 0 | 2 | 4 | 5 | si (3 > 1) -> cambiar
-------------------------

  j  j+1
-------------------------
| 1 | 3 | 0 | 2 | 4 | 5 | cambio
-------------------------

      j  j+1
-------------------------
| 1 | 3 | 0 | 2 | 4 | 5 | si (3 > 0) -> cambiar
-------------------------

      j  j+1     
-------------------------
| 1 | 0 | 3 | 2 | 4 | 5 | cambio
-------------------------

          j  j+1
-------------------------
| 1 | 0 | 3 | 2 | 4 | 5 | si (3 > 2) -> cambiar
-------------------------

          j  j+1
-------------------------
| 1 | 0 | 2 | 3 | 4 | 5 | cambio
-------------------------

4ta Iteración

  j  j+1
-------------------------
| 1 | 0 | 2 | 3 | 4 | 5 | si (1 > 0) -> cambiar
-------------------------

  j  j+1
-------------------------
| 0 | 1 | 2 | 3 | 4 | 5 | cambio
-------------------------

"""

        #  0  1  2  3  4  5
arreglo = [4, 3, 1, 5, 0, 2];


i = 0;
j = 0;

print(arreglo);

while (i < 5):
    while (j < 5 - i):
        if (arreglo[j] > arreglo[j+1]): # Si esto es verdadero se hace el cambio
            temp = arreglo[j];
            arreglo[j] = arreglo[j+1];
            arreglo[j+1] = temp;

        j += 1;
    i += 1;
    j = 0;

print(arreglo);