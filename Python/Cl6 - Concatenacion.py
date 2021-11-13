## Formas de concatenar en python

v_nombre = "Elian";
v_edad = 21;


# Su nombre es: {v_nombre} y su edad es: {v_edad}

# 1ra con ','
print("Su nombre es:",v_nombre,"y su edad es:",v_edad);

# 2da con '+'

print("Su nombre es: " + v_nombre + " y su edad es: " + str(v_edad));

# conversiones
# str - int
# int - str
# float - int
# int - float
# int - bool
# bool - int
# todas - str

#str(v_edad);

# 3ra - con format

print("Su nombre es: {} y su edad es: {}".format(v_nombre, v_edad));

# 4to - con f-string

print(f"Su nombre es: {v_nombre} y su edad es: {v_edad}");