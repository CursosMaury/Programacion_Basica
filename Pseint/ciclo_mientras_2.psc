Algoritmo Tablas_multiplicar
	
	Definir v_tabla Como Entero;
	Definir v_contador Como Entero;
	
	Escribir "Ingrese la tabla de multplicar a mostrar: ";
	Leer v_tabla
	
	v_contador = 1;
	
	Mientras v_contador <= 1 Hacer
		
		Escribir v_tabla, " X ", v_contador, " = ", (v_contador * v_tabla)
		
		v_contador = v_contador + 1;
	FinMientras
	
FinAlgoritmo