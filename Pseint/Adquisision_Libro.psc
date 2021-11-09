Algoritmo Adquisision_Libro
	
	//Numerico - 1, 2, 3, 4, 5.5
	//Cadena de texto - "hola", "adios"
	//Booleano - verdadero y falso
	
	Definir v_libro Como Caracter 
	
	Escribir "Nombre del libro:"
	Leer v_libro // "Principito"
	
	Escribir "Ya estamos en la librería."
	
	Si v_libro == "Principito"  Entonces // Si "Principito" == "Principito" entonces 
		Escribir "Se adquirio el libro"
	SiNo
		Escribir "No se adquirio el libro"
	Fin Si
	
	
FinAlgoritmo