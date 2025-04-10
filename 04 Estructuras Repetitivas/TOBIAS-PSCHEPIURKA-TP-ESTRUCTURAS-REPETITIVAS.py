# Resultados de aprendizaje:
# 1. Diseño y Desarrollo de Algoritmos Eficientes: El estudiante será capaz de diseñar y
# desarrollar algoritmos utilizando estructuras de control repetitivas (FOR, WHILE) para
# resolver problemas matemáticos y de lógica, aplicando
# correctamente operaciones matemáticas y cálculos.
# 2. Escritura Eficaz de Pseudocódigo y Documentación: El estudiante podrá escribir
# pseudocódigo de manera estructurada y clara, utilizando comentarios para explicar el
# funcionamiento de cada parte del algoritmo.
# 3. Interacción con el Usuario y Validación de Datos: El estudiante será capaz de
# diseñar programas que interactúen con el usuario, solicitando datos de entrada y
# proporcionando resultados claros y concisos.

# /////////////

# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

# for num in range(101): #Empezamos el ciclo for con límite en 101 (no incluído)
#     print(num) #Imprimimos todos los números dados

# /////////////

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

# numeroEj2 = int(input("Ingrese un número entero: ")) #Pedimos entero
# numeroEj2 = str(numeroEj2) #Pasamos el entero a string
# digitos = 0 #Inicializamos variable de digitos en cero

# for numeroEj2 in range(len(numeroEj2)): #Ciclo for que va de 0 a length de numero
#     digitos += 1 #se cuenta +1 en digitos

# print(digitos) #se imprime digitos

# /////////////

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

# numero1Ej3 = int(input("Ingrese un número entero: ")) #Ingresamos número 1
# numero2Ej3 = int(input("Ingrese otro número entero: ")) #Ingresamos número 2
# varTemporal = numero2Ej3    #alojamos en varTemporal el número 2
# if numero1Ej3 > numero2Ej3: #if, si el primer número es mayor se da vuelta.
#     numero2Ej3 = numero1Ej3
#     numero1Ej3 = varTemporal
# suma = 0 #Inicializamos suma en cero

# for internos in range(numero1Ej3+1, numero2Ej3): #ciclo for con "Internos" como elemento a procesar en ciclo
#     suma += internos #suma va incorporando los internos

# print(suma) #imprimimos suma total

# /////////////

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

# numeroEj4 = int(input("Ingrese un número entero (INGRESE UN CERO PARA DETENER EL PROGRAMA): ")) #Ingresamos número
# suma = 0 #Inicializamos suma en cero

# while numeroEj4 != 0:
#     suma += numeroEj4 # sumamos el número ingresado
#     numeroEj4 = int(input("Ingrese un número entero (INGRESE UN CERO PARA DETENER EL PROGRAMA): ")) #Ingresamos número

# print(f"El total acumulado es {suma}") #Imprimimos el resultado.

# /////////////

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

# import random #Importamos random

# num_correctoEj5 = random.randint(0,9)   #Preparamos el random entre 0 y 9
# num_usuarioEj5 = 0  #Inicializamos el número ingresado por usuario en 0
# contador = 0    #Inicializamos el contador de intentos en 0

# num_usuarioEj5 = int(input("Adivine el número entre 0 y 9: ")) #Pedimos primer ingreso de número
# while num_usuarioEj5 != num_correctoEj5:    #Ciclo while con condición para repetir: num usuario es distinto a num correcto
#         contador += 1   #Sumamos 1 intento en el ciclo (o sea solo si se equivocaron)
#         num_usuarioEj5 = int(input("Adivine el número entre 0 y 9: "))  #Pedimos ingreso nuevamente en ciclo

# print(f"Felicidades, el número correcto era {num_correctoEj5}. Ud. necesitó {contador} intento/s para llegar al mismo.") #Imprimimos resultado.

# /////////////

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

# for pares in range(100, -1, -2):
#     print(pares)

# /////////////

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

# numEj7 = int(input("Ingrese un número entero positivo: ")) #Usuario ingresa número
# suma = 0 #Suma inicializada en 0
# for iterador in range(0, numEj7+1): #ciclo for que itera por todos los números incluídos entre 0 y número dado +1
#     suma += iterador #suma incorpora iterador con suma

# print(suma) #Imprimimos el total

# /////////////

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

# contador = 0   #Inicializamos el contador (para determinar el largo de números ingresados)
# pares = 0   #Inicializamos pares, impares, positivos y negativos.
# impares = 0
# positivos = 0
# negativos = 0

# while contador < 100:    #ciclo while mientras el número sea menor al pedido
#     numerosEj8 = int(input("Ingrese 100 números: "))    #Input de números
#     if numerosEj8 % 2 == 0: #if para determinar si es par o impar
#         pares += 1
#     else:
#         impares +=1
#     if numerosEj8 > 0:  #if para determinar si es positivo o negativo
#         positivos += 1
#     else:
#         negativos += 1
#     contador += 1   #contador + 1

# for contador in range(100):
#     numerosEj8 = int(input("Ingrese 100 números: "))    #Input de números
#     if numerosEj8 % 2 == 0: #if para determinar si es par o impar
#         pares += 1
#     else:
#         impares +=1
#     if numerosEj8 > 0:  #if para determinar si es positivo o negativo
#         positivos += 1
#     else:
#         negativos += 1

# print(f"Números pares: {pares};\nnúmeros impares: {impares};\nnúmeros positivos: {positivos};\nnúmeros negativos:{negativos}.")     #imprimimos resultado

# /////////////

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

# sumatoriaTotal = 0 #Sumatoria total para acumular cada número ingresado

# for iterador in range(100): #iterador en rango 100
#     numEj9 = int(input("Ingrese 100 números enteros: "))
#     sumatoriaTotal += numEj9 #se suman los números al total

# print(f"El promedio total es de {sumatoriaTotal/100}.") #se saca el promedio

# /////////////

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numEj10 = int(input("Ingrese un número: ")) #Pedimos el num
negativo = numEj10 < 0  #Alojamos en bool si es negativo
# largoNum = str(numEj10)
cargaNum = 0    #la carga de dígitos
numRevesStr = ""    #la carga de dígitos en string
numRevesInt = 0     #el dato final
numEj10 = abs(numEj10)  #convertimos a absoluto el número dado para no tener que dividir en 2 el condicional

# for iterador in range(len(largoNum)):
while numEj10 != 0:     #hasta que sea 0 el while funciona
    cargaNum = numEj10 % 10     #módulo 10 para extraer y alojar en cargaNum el dígito de la derecha
    numRevesStr += str(cargaNum)    #convertimos a string la cargaNum y la alojamos 1x1 en numRevesStr
    numEj10 = numEj10 // 10     #división baja para eliminar el dígito de la derecha

    # if numEj10 < 0:       #este if sólo funcionaba cuando no se usaba absolute
    #     cargaNum = numEj10 % -10
    #     numRevesStr += str(cargaNum)
    #     numEj10 = numEj10 // -10
    # else:
    #     cargaNum = numEj10 % 10
    #     numRevesStr += str(cargaNum)
    #     numEj10 = numEj10 // 10

numRevesInt = int(numRevesStr)      #convertimos a int el str
if negativo:        #si negativo es True, negamos el numRevesInt
    numRevesInt = -numRevesInt
print(numRevesInt)  #Imprimimos
