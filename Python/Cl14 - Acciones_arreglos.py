nombres = [None, None, None, None, None] #5 posiciones

# Vamos a mostrar un menú que tenga 4 opciones
# 1. Agregar nombre
# 2. Modificar Nombre
# 3. Eliminar Nombre
# 4. Salir
# Quiero que este menu se muestre varias veces hasta que el usuario 
# seleccione la opción de salir.

# primer paso identificar el uso de un ciclo
# ciclo mientras (while) en este caso

opcion = 0;

while(opcion != 5):
    print("1. Agregar nombre\n2. Modificar nombre\n3. Eliminar nombre\n4. Mostrar nombres\n5. Salir\n")
    opcion = int(input("Ingrese una opción: "))

    if (opcion == 1):
        #Agregar Nombres
        nombre = input("\nIngrese el nombre a agregar: ");
        #Insertarlo en el primer espacio libre del arreglo

        i = 0;
        while (i < len(nombres)):

            if (nombres[i] == None):
                nombres[i] = nombre;
                break;

            i += 1;
        print();

    elif (opcion == 2):
        #Modificar el nombre

        nombre_modificar = input("\nIngrese el nombre a modificar: ");
        nuevo_nombre = input("Ingrese el nuevo nombre: ");

        i = 0;
        while(i < len(nombres)):

            if (nombres[i] == nombre_modificar):
                nombres[i] = nuevo_nombre;
                break;

            i += 1
        print();

    elif (opcion == 3):
        # Eliminar el nombre

        nombre_eliminar = input("\nIngrese el nombre a eliminar: ");

        i = 0;
        while(i < len(nombres)):

            if (nombres[i] == nombre_eliminar):
                nombres[i] = None;
                break;

            i += 1
        print();

    elif (opcion == 4):
        # Mostrar todos los nombres
        print();
        i = 0;
        while(i < len(nombres)):
            print(nombres[i]);
            i +=1

        print();

    elif (opcion == 5):
        #Salir
        print("\nGracias por visitarnos!");
    else:
        # Marcar un error en la eleccion.
        print("\nOpción incorrecta, por favor seleccione una opción del [1-5]\n");
