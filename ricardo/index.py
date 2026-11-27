## 3. Verificación de año bisiesto y edad legal:
## Pide el año de nacimiento y determina si es bisiesto. Luego calcula la edad del usuario
## y verifica si es mayor de edad (18+).
## Ricardo

anio_actual = 2026
anio_nacimiento = int(input("Ingresa año de nacimiento: "))
edad = anio_actual - anio_nacimiento

# 1. Validamos si es año bisiesto
if (anio_nacimiento % 4 == 0 and anio_nacimiento % 100 != 0) or (anio_nacimiento % 400 == 0):
    print(f"{anio_nacimiento} es un año bisiesto")
else:
    print(f"{anio_nacimiento} no es año bisiesto")

# 2. Validamos si es mayor de edad (sin repetir código)
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


