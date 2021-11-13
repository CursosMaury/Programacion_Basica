# sintaxys de if
# 'if' '(' <condicion> ')' ':'
#       //código de ser verdadera
# 'else' ':'
#       //código de ser falsa

v_numero = int(input("Ingrese un número: "));

if (v_numero >= 10):

    if (v_numero == 10):
        print("El número es igual a 10");
    else:
        print("El número es mayor a 10");
else: 
    print("El número es menor a 10");

# 'elif'

if (v_numero > 10):
    print("El número es mayor a 10");
elif (v_numero == 10):
    print("El número es igual a 10");
elif (v_numero != 10):
    print("El número es diferente de 10");
else:
    print("El número es menor a 10");

# Pasar todos los programas que tienen de pseint
# a python
