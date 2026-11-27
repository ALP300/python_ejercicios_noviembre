usuario=input("Ingresa el usuario:")
contraseña=input("Ingresa la contraseña: ")
rol=input("Ingresa el rol: ")

if usuario== "admin" and contraseña=="editor" and rol == "visitante" :
   print("Permiso disponible") 

else :
   print("No esta disponible")