Algoritmo Si_anidado
	
	Definir v_numero Como Entero
	
	Escribir "Ingrese un n�mero:"
	Leer v_numero
	
	Si v_numero > 10 Entonces
		Escribir "El n�mero es mayor a 10";
	Sino
		Si v_numero < 10 Entonces
			Escribir "El n�mero es menor a 10";
		SiNo
			Escribir "El n�mero es igual a 10";
		FinSi
	FinSi
	
	Si v_numero >= 10 Entonces
		Si v_numero == 10 Entonces
			Escribir "El n�mero es igual a 10";
		SiNo
			Escribir "El n�mero es mayor a 10";
		FinSi
	Sino
		Escribir "El n�mero es menor a 10";
	FinSi
	
FinAlgoritmo