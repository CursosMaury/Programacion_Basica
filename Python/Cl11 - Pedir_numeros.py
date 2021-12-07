v_numeros = int(input("Cuantos notas desea ingresar: "))

v_contador = 1;

v_par = 0;

while(v_contador <= v_numeros):
    v_numero = int(input(f"Ingrese la nota {v_contador}: "))

    if (v_numero % 2 == 0): # % -> modulo 
        # 2/2 -> cociente: 1 residuo: 0
        # 5/2 -> cociente: 2 residuo: 1
        v_par += 1

    v_contador += 1

print(f"La cantidad de notas pares es: {v_par}");
