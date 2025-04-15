# Funciones

import math

def recibir_float(mensaje):
    numero = float(input(mensaje))
    return numero

def recibir_int(mensaje):
    numero = int(input(mensaje))
    return numero

def imprimir_hola_mundo ():
    print("Hola Mundo!")

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

def calcular_area_circulo(radio):
    area = math.pi*(radio**2)
    return area

def calcular_perimetro_circulo(radio):
    perimetro = (2*radio)*math.pi
    return perimetro

def segundos_a_horas(segundos):
    horas = int(segundos)/3600
    return horas

def tabla_multiplicador(numero):
    for multiplicador in range(1, 11):
        print (f"{numero} X {multiplicador} = {multiplicador*numero}")

def operaciones_basicas(a, b):
    suma = a+b
    resta = a-b
    multiplicacion = a*b
    division = a/b
    calculos = (suma, resta, multiplicacion, division)
    print(f"{a} + {b} = {suma}")
    print(f"{a} - {b} = {resta}")
    print(f"{a} X {b} = {multiplicacion}")
    print(f"{a} / {b} = {division:.2f}")
    return calculos    

def calcular_imc(peso, altura):
    imc = peso / (altura**2)
    return imc

def celsius_a_fahrenheit(celsius):
    resultado = (celsius * 1.8) + 32
    return resultado

def calcular_promedio(a, b, c):
    suma = a + b + c
    promedio = suma / 3
    return promedio

# Programa principal

# -------------------------------------------------- #

# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

# imprimir_hola_mundo()

# -------------------------------------------------- #

# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver:
# “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

# saludar_usuario("Eugenia")

# -------------------------------------------------- #

# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir
# los datos al usuario y llamar a esta función con los valores ingresados.
# 
# nombre = input("Ingrese su nombre: ")
# apellido = input("Ingrese su apellido: ")
# edad = int(input("Ingrese su edad: "))
# residencia = input("Ingrese su ciudad de residencia: ")
# informacion_personal(nombre, apellido, edad, residencia)


# -------------------------------------------------- #

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio
# como parámetro y devuelva el área del círculo. calcular_perimetro_
# circulo(radio) que reciba el radio como parámetro y devuelva
# el perímetro del círculo. Solicitar el radio al usuario y llamar ambas
# funciones para mostrar los resultados.

# radio1 = recibir_float("Ingrese el radio del círculo para calcular el área: ")
# area = calcular_area_circulo(radio1)
# print(f"El área de un círculo con radio {radio1} es de {area:.2f}.")
# radio2 = recibir_float("Ingrese el radio del círculo para calcular el área: ")
# perimetro = calcular_perimetro_circulo(radio2)
# print(f"El perímetro de un círculo con radio {radio2} es de {perimetro:.2f}.")

# -------------------------------------------------- #

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar
# el resultado usando esta función.

# segundos = recibir_float("Ingrese segundos para convertir a hora(s): ")
# conversor = segundos_a_horas(segundos)
# print(f"{segundos} segundo(s) son el equivalente a {conversor:.2f} hora(s).")

# -------------------------------------------------- #

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la fun-
# ción.

# print("Tabla de multiplicar")
# numero = recibir_int("Ingrese un número para ver su tabla del 1 al 10: ")
# tabla = tabla_multiplicador(numero)
# print(tabla)

# -------------------------------------------------- #

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado
# de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados
# de forma clara.

# num1 = recibir_float("Ingrese el primer número: ")
# num2 = recibir_float("Ingrese el segundo número: ")
# operaciones = operaciones_basicas(num1, num2)

# -------------------------------------------------- #

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función
# para mostrar el resultado con dos decimales.

# peso = recibir_float("Ingrese su peso en kilogramos: ")
# altura = recibir_float("Ingrese su altura en metros: ")
# IMC = calcular_imc(peso, altura)
# print(f"Su IMC es {IMC:.2f}")

# -------------------------------------------------- #

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

# celsius = recibir_float("Conversor de grados Celsius a Fahrenheit: ")
# fahrenheit = celsius_a_fahrenheit(celsius)
# print(f"{celsius}° C es/son {fahrenheit:.2f}° F.")

# -------------------------------------------------- #

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

# num1 = recibir_float("Ingrese el primer número: ")
# num2 = recibir_float("Ingrese el segundo número: ")
# num3 = recibir_float("Ingrese el tercer número: ")
# promedio = calcular_promedio(num1, num2, num3)
# print(f"El promedio es {promedio}.")