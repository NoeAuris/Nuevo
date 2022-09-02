def repetir(valor, cantidad):
    lista = []
    while cantidad > 0:
        lista.append(valor)
        cantidad -= 1
    return lista
repetir('Gato', 12)

'''
Crear una función repetir que tome como argumento un valor
valor y un número entero cantidad, y devuelva una lista con valor repetido cantidad de veces.

'''