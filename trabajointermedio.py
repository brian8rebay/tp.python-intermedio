#ejercicio1
try:
   numero1 = int(input("ingrese el primer numero:"))
   numero2 = int(input("ingrese el segundo numero"))

   resultado = numero1 / numero2

   print("el resultado es :", resultado)

except ZeroDivisionError:
   print("error: no se puede dividir por cero.") 


#ejercicio2
try:
   numero = 10
   texto = "hola"

   resultado = numero+texto

   print("el resultado es:", resultado)

except TypeError:
   print("error: no se puede sumar un numero con una cadena de texto.")


#ejercicio3
try:
   persona = {
    "nombre": "brian", "edad": 24
   }

   print(persona["apellido"])

except KeyError:
   print("error: esa clave no existe en el diccionario.")


#ejercicio4
try:
   archivo = open("archivo.txt", "r")
   contenido = archivo.read()

   print("contenido del archivo")
   print(contenido)

   archivo.close()

except FileNotFoundError:
   print("Error: el archivo no existe.")
   print("Creando el archivo...")

   archivo = open("archivo.txt", "w")
   archivo.write("este archivo fue creado por el programa.")
   archivo.close()

   print("archivo creado correctamente.")   