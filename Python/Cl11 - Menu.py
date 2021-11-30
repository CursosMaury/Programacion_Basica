# Caracteres de escape
# "" ''
# Esto es   un tabulador
# Esto es
# un salto de linea
# \ -> backslash

# print("\"Hola\"");
# print("\tEsto es una tabuluación"); #-> tabulación horizontal
# print("Esto es\nun salto de linea"); # -> salto de linea




v_terminacion = "";

v_menu = "1. Saludar\n2. Agradecer\n3. Salir";

while (v_terminacion != "N"): # v_terminacion diferente a "N"
    print(v_menu);
    v_opcion = int(input("Ingrese una opción [1-3]: "))

    if (v_opcion == 1):
        print("Holi :3");
    elif (v_opcion == 2):
        print("Muchas gracias :)");
    elif (v_opcion == 3):
        print("Vuelva pronto");
        v_terminacion = "N";
    else:
        print("Opción no encontrada, por favor escoga una de las opciones disponibles");
        v_terminacion = input("Escriba N para terminar: ");




