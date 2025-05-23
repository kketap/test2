# Solicitar los nombres al usuario
nombres = []
for i in range(3):
    nombre = input(f"Introduce el nombre {i + 1}: ")
    nombres.append(nombre)

# Encontrar el nombre con mayor cantidad de caracteres
nombre_mayor_longitud = max(nombres, key=len)

# Mostrar el nombre con mayor cantidad de caracteres
print(f"El nombre con mayor cantidad de caracteres es: {nombre_mayor_longitud}")