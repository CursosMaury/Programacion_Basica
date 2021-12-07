Algoritmo Rango_tablas_multiplicar
	
	//Definir las variables que obtendran el valor de inico 
	//y de fin;
	Definir v_inicio Como Entero;
	Definir v_fin Como Entero;
	
	//Definir la variable que contara
	Definir v_contador_tablas Como Entero;
	Definir v_contador Como Entero;
	
	Escribir "Ingrese la tabla de inicio: ";
	Leer v_inicio
	Escribir "Ingrese la tabla de fin: ";
	Leer v_fin
	
	v_contador_tablas = v_inicio;
	
	// arriba - abajo
	// v_contador_tablas >= v_fin  --
	
	//abajo - arriba
	// v_contador_tablas <= v_fin ++
	
	v_contador = 1;
	
	Si v_inicio > v_fin Entonces
		Mientras v_contador_tablas >= v_fin Hacer
			Escribir "TABLA DEL: ", v_contador_tablas;
			Mientras v_contador <= 10 Hacer
				
				Escribir v_contador_tablas, " X ", v_contador, " = ", (v_contador_tablas * v_contador);
				
				v_contador = v_contador + 1;
			FinMientras
			
			v_contador = 1;
			v_contador_tablas = v_contador_tablas - 1;
		FinMientras
	SiNo
		Mientras v_contador_tablas <= v_fin Hacer
			Escribir "TABLA DEL: ", v_contador_tablas;
			Mientras v_contador <= 10 Hacer
				
				Escribir v_contador_tablas, " X ", v_contador, " = ", (v_contador_tablas * v_contador);
				
				v_contador = v_contador + 1;
			FinMientras
			
			v_contador = 1;
			v_contador_tablas = v_contador_tablas + 1;
		FinMientras
	FinSi
	
FinAlgoritmo