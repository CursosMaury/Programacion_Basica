"""
Solicitar 5 nombres y 5 edades
y al final mostrar todos los nombres con su respectiva
edad
"""

nombres = [None, None, None, None, None];
edades = [None, None, None, None, None];

i = 0;

while (i < 5):
    nombres[i] = input("Ingrese un nombre: ");
    edades[i] = int(input("Ingrese su edad: "));

    i += 1

i = 0;

while(i < len(nombres)):
    print(f"nombre: {nombres[i]}, edad: {edades[i]}");

    i += 1;