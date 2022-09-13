 # Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia
print ("Bienvenido a la trivia.")
print ("Pondre a prueba tus conocimientos")

print ("Entonces, nos gustaria saber tu nombre.")

nombre = input("\nNombre: ")

# Es importante dar instrucciones sobre cómo jugar:
print ("\nHola", nombre,",","responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n")

# OJO, el \n al final de la línea 6 es para dar un "salto de línea"

# Pregunta 1
print ("1) ¿Quien fue el creador de python?")
print ("a) Alan Kay")
print ("b) Dennis M. Ritchie")
print ("c) Guido V. Rossum")
print ("d) Alan Cooper")

# Almacenamos la respuesta del usuario en la variable "respuesta_1"
respuesta_1 = input("\nTu respuesta: ")

while respuesta_1 not in ("a","b","c","d"):
  respuesta_1 = input("Se responde solo con a,b,c,d. Ingresa nuevamente tu respuesta: ")

#respuestas

if respuesta_1 == "c":
  print("R.1: Muy bien!", nombre)
else:
  print("R.1: Incorrecto")



# Pregunta 2

print ("\n2) ¿Cuando se implemento (python) por primera vez en la historia?")
print ("a) Diciembre, 1989")
print ("b) febrero, 1991")
print ("c) entre a) y b) ???")
print ("d) Adios mundo cruel")

respuesta_2 = input("\nTu respuesta: ")

# el loop "ciclo de validacion"
while respuesta_2 not in ("a","b","c","d"):
  respuesta_2 = input("Se responde solo con a,b,c,d. Ingresa nuevamente tu respuesta: ")

#respuesta
if respuesta_2 == "a":
  print("R.2: Muy bien!", nombre) 
if respuesta_2 == "b":
  print ("Cerca, pero wikipedia gana")
else:
  print("R.2: Incorrecto") 
if respuesta_2 == "d":
  print ("Espero que estemos bromeando")
if respuesta_2 == "c":
  print ("podria ser, pero no, relee la pregunta y lamentate")


#ultima pregunta

print ("\n3) ¿Que es mas dificil: matematicas, programacion?")
print ("a) Matematicas")
print ("b) Lenguajes con mucho ingles")
print ("c) Ambos, no nos mentimos")
print ("d) Se suficiente logica")

respuesta_3 = input("\nTu respuesta: ")

while respuesta_3 not in ("a","b","c","d"):
  respuesta_3 = input("Se responde solo con a,b,c,d. Ingresa nuevamente tu respuesta: ")


if respuesta_3 == "d":
  print("R.3: Muy bien!", nombre)
if respuesta_3 == "a":
  print ("R.3: Empieza de primaria", nombre)
if respuesta_3 == "b":
    print ("R.3: Ya somos dos", nombre)
if respuesta_3 == "c":
      print ("R.3: Bueno, lo ultimo que muere es la esperanza")

  

  
  
  
  
  
  #respuestas

print("\n\nEn resumen")

if respuesta_1 == "c":
  print("\nR.1: Muy bien!", nombre)
else:
  print("R.1: Incorrecto")



if respuesta_2 == "a":
  print("R.2: Muy bien!", nombre)
else:
  print("R.2: Incorrecto")


  

if respuesta_3 == "d":
  print("R.3: Muy bien!", nombre)
if respuesta_3 == "a":
  print ("R.3: Corrigo, empecemos de primaria", nombre)
if respuesta_3 == "b":
    print ("R.3: Ya somos dos", nombre)
if respuesta_3 == "c":
      print ("R.3: Solo estudiemos")


