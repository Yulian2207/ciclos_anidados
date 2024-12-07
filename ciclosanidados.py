# Ciclo anidado.
# Es un ciclo que suele contener otros ciclos, es decir, hay uno externo y hay uno interno.
# (Esto no implica que solo puedan anidar 2).
# Se usan para procesar datos de diferentes niveles o dimensiones.


# for papa in range (3): 
#     for zanahoria in range (3):
#         print (f"i={papa}, j={zanahoria}")

# Para que se aplica...
# Procesar matrices, generar patrones visuales, resolver problemas jerarquicos como tableros o graficos.
        
# Concepto clave.
# Por cada iteración del ciclo externo, el ciclo internio se ejecuta completamente.
        

# Procesamientos de matrices con ciclos anidados.

# Matriz en IT:
# Es una lista [], donde cada elemento es una lista o una sublista, estas van a presentar una fila.

# Ejemplo 1: imprimir una matriz que quede reprsentada como su representación matématica.


# matriz = [
#      [1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]
#  ]
# for fila in matriz: 
#    for elemento in fila: 
#       print (elemento, end=" ")
#    print()

# suma = 0

# for fila in matriz: 
#    for elemento in fila:
#       suma += elemento

# print (f"Suma total: {suma}")

# contador_pares = 0 

# for fila in matriz:
#    for elemento in fila: 
#       if elemento % 2 == 0: 
#          contador_pares += 1

# print (f"Hay {contador_pares} numero pares en la matriz")

# Generación de patrones visuales con ciclos.

# Triangulo de números.

# n = int(input("Indicame el numero de pisos que tendra el triangulo: "))


# for numeros in range (1, n + 1):
#     for j in range (1, numeros + 1):
#         print (j, end=" ")
#     print ()
# Piramide invertida con piramide de espacios interna.
# m = 10 

# for i in range (m):
#     for j in range (1, m - i + 1):
#         print (j, end=" ")
#     print ("  " * (2 * i), end = " ")
#     for j in range (m - i, 0, -1):
#         print (j, end = " ")
#     print ()


# Tablero de ajedrez.
    
# n = 8

# for i in range (n):
#     for j in range (n):
#         if (i + j) % 2 == 0:
#             print ("  ", end="")
#         else:
#             print ("X", end="")
#     print ()

# Hacer transposicion de matrices, teniendo en cuenta la matriz previamente definida.
# matriz = [
#      [1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]
#  ]

# transpuesta =[[0]*3 for i in range (3)]

# for i in range (3):
#     for j in range (3):
#         transpuesta [j] [i] = matriz [i] [j]

# for fila in transpuesta:
#     print (fila)