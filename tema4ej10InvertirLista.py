lista = [0, 5, 33, 2, 17, 89, 40]

def invertir(lista):
    reverso = lista[::-1]
    return reverso
invertir(lista)
#ESTE ME SALIO DE DOS FORMAS.


lista = [0, 5, 33, 2, 17, 89, 40]
reverso = reversed(lista)
def invertir(lista):
    while True:
        try:
            elemento = next(reverso)
            contador = 0
            if elemento == 1:
                print(elemento)
        except StopIteration:
            break
invertir([0, 5, 33, 2, 17, 89, 40])

