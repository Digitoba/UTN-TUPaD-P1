# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

# print("Hola mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.

# nombre = input("Ingrese su nombre:")
# print(f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla

# nombre = input("Ingrese su nombre: ")
# apellido = input("Ingrese su apellido: ")
# edad = input("Ingrese su edad: ")
# pais = input("Ingrese su país de residencia: ")
# print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {pais}.")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.

# radio = int(input("Ingrese el radio del círculo: "))
# # radio = int(radio)
# pi = 3.1416
# diametro = radio * 2
# perimetro = round(pi * diametro, 2)
# area = round(pi * radio ** 2, 2)
# print (f"""Radio: {radio}
# Perimetro: {perimetro}
# Área: {area}""")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.

# segundos = input ("Ingrese una cantidad de segundos")
# segundos = int(segundos)
# horas = segundos / 3600
# print (f"{segundos} segundos equivalen a {round(horas,2)} horas.")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.

# numero = input("Ingrese un número para ver su tabla de multiplicar")
# numero = int(numero)
# print(f"""Tabla de multiplicar de {numero}
# {numero} X 1 = {numero*1}
# {numero} X 2 = {numero*2}
# {numero} X 3 = {numero*3}
# {numero} X 4 = {numero*4}
# {numero} X 5 = {numero*5}
# {numero} X 6 = {numero*6}
# {numero} X 7 = {numero*7}
# {numero} X 8 = {numero*8}
# {numero} X 9 = {numero*9}
# {numero} X 10 = {numero*10}
# """)

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos

# num1 = int(input("Ingrese un número distinto del 0: "))
# num2 = int(input("Ingrese otro número distinto del 0: "))
# print(f"""{num1} + {num2} = {num1+num2}
# {num1} / {num2} = {num1/num2}
# {num1} * {num2} = {num1*num2}
# {num1} - {num2} = {num1-num2}""")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
# modo:

# altura = input("Ingrese su altura: ")
# peso = input("Ingrese su peso: ")
# altura = float(altura)
# peso = int(peso)
# imc = peso / altura**2
# print(f"Su Índice de Masa Corporal es {round(imc, 2)}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:

# celsius = input("Ingrese temperatura en celsius: ")
# celsius = float(celsius)
# fahrenheit = celsius * 1.8 + 32
# print(f"{celsius} °C = {fahrenheit} °F")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.

# num1 = input("Ingrese el primer número: ")
# num2 = input("Ingrese el segundo número: ")
# num3 = input("Ingrese el tercer número: ")
# num1 = int(num1)
# num2 = int(num2)
# num3 = int(num3)
# # promedio = (num1+num2+num3)/3
# # print(f"El promedio de los tres números dados es: {round(promedio,2)}.")

# a = True
# b = False
# c = not a and b
# d = not (a and b)
# e = c or d and a or b
# print(e)