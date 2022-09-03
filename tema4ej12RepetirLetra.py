def repetir_letras(palabra, cantidad):
    resultado = []
    for letras in palabra:
        resultado += letras * cantidad
        print(resultado)
    return resultado
    
repetir_letras('¡Ada es genial!', 3)


'''Crear una función repetir_letras que tome como argumento un string palabra
y un número entero cantidad, y devuelva una string donde cada letra de palabra 
esté repetida cantidad de veces.

repetir_letras('hola', 2) # 'hhoollaa'
repetir_letras('ada', 3) # 'aaadddaaa'
repetir_letras('ah!', 5) # 'aaaaahhhhh!!!!!'
repetir_letras('basta', 1) # 'basta'
'''

