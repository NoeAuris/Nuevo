def sumar_impares_hasta(numero):
    contador = 0
    while 0 < numero:
        if numero % 2 != 0:
            contador = contador + numero
        numero -= 1
        print(contador)
    return contador
sumar_impares_hasta(5)
#ME SALIO.


#LO INTENTE HACER CON UNA LISTA PERO NO ME SALIO.
'''def sumar_impares_hasta(numero):
        lista = [0, 2, 6, 5, 9, 11, 13, 15, 17, 4, 9]
        x = 0
        sumalist_impar = lista % 2
        for num in lista:
            sumalist = x + num
            x = num
            if sumalist_impar % 3 == 0:
                return x + sumalist_impar

sumar_impares_hasta(numero)

def sumar_impares_hasta(numero):
'''
'''
Crear una función sumar_impares_hasta que tome como argumento un 
número numero y que devuelva la suma de todos los impares empezando
 desde 0 hasta dicho numero inclusive.
'''