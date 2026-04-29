usuario = input("Ingrese su nombre: ")

if len(usuario) > 5 and len(usuario) < 15 and usuario[0].isalpha() and usuario.isalnum():
    print("Usuario valido")
    print(f"Su usuario es: {usuario}")
elif len(usuario) <= 5 or len(usuario) >= 15:
    print("Usuario invalido, la longuitud debe de ser entre 6 y 14 caracteres.")
else:
    print("El usuario debe de ser alfanumerico y empezar con letra")