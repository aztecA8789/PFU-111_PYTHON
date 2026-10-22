# Tarea de Python - 10 Ejercicios en Ejecución Secuencial
#ejercicio 1:
print("1: Imprimir números del 1 al 10")
for i in range(1, 11):
    print(i)

#ejercicio 2: 
print("2: Suma de una lista")
numeros = [5, 10, 15, 20]
suma = 0
for n in numeros:
    suma += n
print(f"Lista de números: {numeros}")
print(f"La suma total es: {suma}")

#ejercicio 3:
print("3: Recorrer una cadena")
palabra = "Python"
print(f"Palabra analizada: {palabra}")
for letra in palabra:
    print(letra)

#ejercicio 4:
print("4: Tabla de multiplicar")
num_tabla = 5
print(f"Mostrando la tabla del {num_tabla}:")
for i in range(1, 11):
    print(f"{num_tabla} x {i} = {num_tabla * i}")

#ejercicio 5:
print("5: Contar vocales")
frase = "Programacion en Python"
vocales = "aeiouáéíóú"
contador = 0
for letra in frase.lower():
    if letra in vocales:
        contador += 1
print(f"Frase: '{frase}'")
print(f"Cantidad total de vocales: {contador}")

#ejercicio 6:
print("6: Números pares del 1 al 20")
i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1

#ejercicio 7:
print("7: Menú interactivo (Demostración)")
print("Simulando selección de menú interactivo...")
opcion_menu = "salir"
print(f"Opción seleccionada: {opcion_menu}")
if opcion_menu == "salir":
    print("Saliendo del menú interactivo correctamente.")

#ejercicio 8:
print("8: Adivinar el número")
numero_secreto = 7
intento_usuario = 7
print(f"Número secreto a adivinar: {numero_secreto}")
print(f"Intento del usuario: {intento_usuario}")
if intento_usuario == numero_secreto:
    print("¡Felicidades, adivinaste el número!")

#ejercicio 9:
print("9: Cálculo de factorial")
n_fact = 5
factorial = 1
j = 1
while j <= n_fact:
    factorial *= j
    j += 1
print(f"El número ingresado es: {n_fact}")
print(f"El factorial de {n_fact} es: {factorial}")

#ejercicio 10:
print("10: Suma hasta número negativo")
valores_ingresados = [10, 20, 5, -1]
suma_acumulada = 0
idx = 0
print(f"Secuencia de números ingresados: {valores_ingresados}")
while idx < len(valores_ingresados):
    val = valores_ingresados[idx]
    if val < 0:
        print(f"Se detectó el número negativo ({val}), el bucle termina.")
        break
    suma_acumulada += val
    idx += 1
print(f"La suma acumulada de los valores positivos es: {suma_acumulada}")

