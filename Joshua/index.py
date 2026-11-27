# Solicitar año de nacimiento
anio = int(input("Ingrese su año de nacimiento: "))

# Verificar si es año bisiesto
if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print("El año de nacimiento es bisiesto")
else:
    print("El año de nacimiento no es bisiesto")

# Calcular edad
edad = 2026 - anio

print("Su edad es:", edad, "años")

# Verificar mayoría de edad
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")