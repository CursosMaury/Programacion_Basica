Algoritmo Si_anidado
	
	Definir v_numero Como Entero
	
	Escribir "Ingrese un número:"
	Leer v_numero
	
	Si v_numero > 10 Entonces
		Escribir "El número es mayor a 10";
	Sino
		Si v_numero < 10 Entonces
			Escribir "El número es menor a 10";
		SiNo
			Escribir "El número es igual a 10";
		FinSi
	FinSi
	
	Si v_numero >= 10 Entonces
		Si v_numero == 10 Entonces
			Escribir "El número es igual a 10";
		SiNo
			Escribir "El número es mayor a 10";
		FinSi
	Sino
		Escribir "El número es menor a 10";
	FinSi
	
FinAlgoritmo