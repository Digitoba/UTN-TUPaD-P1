# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

# edad = int(input("Ingrese su edad: "))
# if edad > 18:
#     print("Es mayor de edad.")

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.

# nota = int(input("Ingrese su nota: "))
# if nota >= 6:
#     print("Aprobado.")
# else:
#     print("Desaprobado.")

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.

# numero = float(input("Ingrese un número par: "))
# if numero % 2 == 0:
#     print("Ha ingresado un número par.")
# else:
#     print("Por favor, ingrese un número par.")

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

# edad = int(input("Ingrese su edad: "))
# if edad > 0 and edad < 12:
#     print("Ud. es un/a niño/a.")
# elif edad >= 12 and edad < 18:
#     print("Ud. es un/a adolescente.")
# elif edad >= 18 and edad < 30:
#     print("Ud. es un/a adulto/a joven.")
# elif edad >= 30:
#     print("Ud. es un/a adulto/a.")
# else:
#     print("Ud. es un feto o un viajero del tiempo.")

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.

# contrasenia = str(input("Ingrese su contraseña: "))
# if len(contrasenia) >= 8 and len(contrasenia) <= 14:
#     print("Ha ingresado una contraseña correcta.")
# else:
#     print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# Definir la lista numeros_aleatorios de la siguiente forma:

# # importaciones
# import random
# from statistics import mode, median, mean
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# print(numeros_aleatorios)
# # Asignamos mean, mode y median a variables.
# media = mean(numeros_aleatorios)
# moda = mode(numeros_aleatorios)
# mediana = median(numeros_aleatorios)
# print(f"""La media es: {media}
# La mediana es: {mediana}
# La moda es: {moda}""")
# # condicional
# if media > mediana and mediana > moda:
#     print("Hay sesgo positivo.")
# elif media < mediana and mediana < moda:
#     print("Hay sesgo negativo.")
# else:
#     print("No hay sesgo.")

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

# frase_pal = input("Ingrese una frase o una palabra: ").lower()
# ultima_letra = frase_pal[-1]
# if (ultima_letra) == "a" or (ultima_letra) == "e" or (ultima_letra) == "i" or (ultima_letra) == "o" or (ultima_letra) == "u":
#     print(f"{frase_pal}!")
# else:
#     print(f"{frase_pal}")

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

# nombre = input ("Ingrese su nombre: ")
# print("""1. Nombre en mayúsculas.
# 2. Nombre en minúsculas.
# 3. Primera letra en mayúscula.""")
# opcion = int(input("Ingrese la opción que desea: "))
# if opcion == 1:
#     print(nombre.upper())
# elif opcion == 2:
#     print(nombre.lower())
# elif opcion == 3:
#     print(nombre.title())
# else:
#     print("Escriba una opción válida.")

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala)

# magnitud = float(input("Ingrese la magnitud del terremoto [escala Ritcher]: "))
# if magnitud < 3:
#     print("Muy leve, imperceptible.")
# elif magnitud >= 3 and magnitud < 4:
#     print("Leve, ligeramente perceptible.")
# elif magnitud >= 4 and magnitud < 5:
#     print("Moderado, sentido por personas, pero generalmente no causa daños.")
# elif magnitud >= 5 and magnitud < 6:
#     print("Fuerte, puede causar daños en estructuras débiles.")
# elif magnitud >= 6 and magnitud < 7:
#     print("Muy fuerte, puede causar daños significativos.")
# else:
#     print("Extremo, puede causar graves daños a gran escala.")

# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

# hemisferio = str(input("Ingrese el hemisferio en el que se encuentra: ").lower())
# dia = int(input("Ingrese el día actual: "))
# mes = int(input("Ingrese el mes actual: "))

# dic = [12]
# eneFeb = [1, 2]
# mar = [3]
# abrMay = [4, 5]
# jun = [6]
# julAgo = [7, 8]
# sep = [9]
# octNov = [10, 11]

# # Condicional anidado
# if hemisferio == "sur":
#     if mes in dic and dia >= 21:
#         print("Es verano.")
#     elif mes in eneFeb:
#         print("Es verano.")
#     elif mes in mar and dia <= 20:
#         print("Es verano.")
#     elif mes in mar and dia >= 21:
#         print("Es otoño.")
#     elif mes in abrMay:
#         print("Es otoño.")
#     elif mes in jun and dia <= 20:
#         print("Es otoño.")
#     elif mes in jun and dia >= 21:
#         print("Es invierno.")
#     elif mes in julAgo:
#         print("Es invierno.")
#     elif mes in sep and dia <= 20:
#         print("Es invierno.")
#     elif mes in sep and dia >= 21:
#         print("Es primavera.")
#     elif mes in octNov:
#         print("Es primavera.")
#     elif mes in dic and dia <= 20:
#         print ("Es primavera.")
# else:
#     if mes in dic and dia >= 21:
#         print("Es invierno.")
#     elif mes in eneFeb:
#         print("Es invierno.")
#     elif mes in mar and dia <= 20:
#         print("Es invierno.")
#     elif mes in mar and dia >= 21:
#         print("Es primavera.")
#     elif mes in abrMay:
#         print("Es primavera.")
#     elif mes in jun and dia <= 20:
#         print("Es primavera.")
#     elif mes in jun and dia >= 21:
#         print("Es verano.")
#     elif mes in julAgo:
#         print("Es verano.")
#     elif mes in sep and dia <= 20:
#         print("Es verano.")
#     elif mes in sep and dia >= 21:
#         print("Es otoño.")
#     elif mes in octNov:
#         print("Es otoño.")
#     elif mes in dic and dia <= 20:
#         print ("Es otoño.")