Algoritmo Es_mayor_de_edad
	
	//Se solicita el nombre y la edad
	//y si la edad es >= 18 es mayor de edad
	// sino es menor de edad.
	
	Definir v_nombre Como Caracter;
	Definir v_edad como Entero;
	
	Escribir "Ingrese su nombre:"
	Leer v_nombre
	Escribir "Ingrese su edad"
	Leer v_edad
	
	// 'Si' <condicion> 'Entonces'
	// <condicion> es una expresion que utiliza los 
	//siguientes operadores: 
	// <, >, <=, >= ó ==; 2 == 2 -> 2 es igual a 2
	
	Si v_edad > 18 Entonces
		// esto es un identado o tabulación.
		Escribir v_nombre, " es mayor de edad"
	SiNo
		Escribir v_nombre, " es menor de edad"
	FinSi
	
	Si v_edad < 18 Entonces
		Escribir v_nombre, " es menor de edad"
	SiNo
		Escribir v_nombre, " es mayor de edad"
	FinSi
	
	
FinAlgoritmo
