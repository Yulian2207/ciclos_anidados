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