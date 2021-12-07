# Arreglos - son un espacio de memoria contiguo (seguidos)
# y que se pueden acceder por medio de indices, el acceso es directo
# en la memoria

"""
declarar una variable
a = 10;
a -> 0x00145

print(a);

Declarar arreglos
arreglo = [1, 2, 3, 4];
arreglo -> 0x00146

indice - empiezan en 0 hasta el tamaño del arreglo menos 1
0 - 3

[1, 2, 3, 4]
 0  1  2  3 -> indices

arreglo[0] -> acceder al primer indice osea el primer valor
arreglo[0] -> 1
arreglo[1] -> 2
arreglo[2] -> 3
arreglo[3] -> 4

arreglo[4] -> None - nulo - nada. lanza un error 
ya que el indice no existe

Memoria RAM - celda es epacio de memoria
celdas  posiciones
-----
|10 |   0x00145
-----
| 1 |   0x00146
-----
| 2 |   0x00147
-----
| 3 |   0x00148
-----
| 4 |   0x00149
-----
|   |   0x00150
-----

"""
        #  0  1  2  3   -> indices
        # -4 -3 -2 -1   -> indices inversos
arreglo = [1, 2, 3, 4];
#print(arreglo[-4]);

# declarar arreglos con tamaño fijo 
#<nombre_arreglo> '=' '[' <lista_None> ']'
# None -> nada vacio
# <lista_None> -> None, None, None, etc...

# Arreglo de 5 posiciones
arreglo_fijo = [None, None, None, None, None];

# como obtener el tamaño de un arreglo
# función len(<arreglo>);
#print(len(arreglo_fijo));

print(arreglo_fijo);
arreglo_fijo[0] = 1;    #-> se asignara un valor cuando este sea None
print(arreglo_fijo);

i = 0;
while (i < len(arreglo_fijo)):
    print(arreglo_fijo[i]);
    i += 1;
