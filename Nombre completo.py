nombre = input("Ingrese su nombre: ")
if nombre == "":
    input("El nombre no puede estar vacio")
elif nombre.islower() or nombre.isupper():
    nombre_titulo = nombre.title()
    print (f"Su nombre formateado es: {nombre_titulo}")
else:
    print(f"Nombre aceptado tal cual: {nombre}")