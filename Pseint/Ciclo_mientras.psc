Algoritmo Ciclos
	
	Definir v_numero Como Entero;
	
	Definir v_contador Como Entero;
	Definir v_acumuladora Como Entero;
	
	v_numero = 10;
	
	//Ciclo mientras
	
	Mientras v_numero > 0 Hacer
		Escribir v_numero
		v_numero = v_numero - 1; //10 - 1
	Fin Mientras
	
	//Variables pueden servir para diferente proposito
	
	// Variables normales - generales 
	// Varaibles contadoras
	// Variables acumuladoras
	
	// Imprimir la suma de los primeros 10 números
	v_contador = 1
	v_acumuladora = 0
	
	Mientras v_contador <= 10 Hacer
		v_acumuladora = v_acumuladora + v_contador;
		v_contador = v_contador + 1;
	FinMientras
	
	Escribir "La suma de los primeros 10 números es: ", v_acumuladora; 
	
FinAlgoritmo