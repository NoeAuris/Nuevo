def es_palindromo(palabra):
    reverso_palabra = palabra[::-1]
    if palabra == reverso_palabra:
        print(palabra)
        return True
    return False
es_palindromo('SomoS')

# ESTE SI ME SALIOO SII.
