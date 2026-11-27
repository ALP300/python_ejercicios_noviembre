'''
Sistema de clasificación de rendimiento: 
Solicita al usuario su nota (0-20) y su asistencia (%). Si la nota es mayor o igual a 11 y 
la asistencia es mayor o igual al 70%, se aprueba. De lo contrario, se desaprueba. 
Además, otorga menciones especiales para notas mayores a 17 con asistencia completa. 
'''
nota= int(input("Ingresa la nota: ")) #18
asistencia= float(input("Ingresa la asistencia: ")) #80

if nota<0 and nota>20 and asistencia>100 and asistencia<0:
    print("Datos inválidos")

elif nota>=11 and asistencia>= 70:
    print("Aprobado")
    if nota>17 and asistencia==100:
        print("ERES UN CRACK, MAESTRO, FIERA, TIFÓN")
else:
    print("Desaprobado")

