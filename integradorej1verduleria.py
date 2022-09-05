frutas = {'banana': 200, 'anana': 800, 'manzana': 300, 'naranja': 150, 'kiwi': 600}

def pide_frutas(nombre, cantidad):
    resultado = {}
    for fruta in frutas:
        if nombre == fruta:
            resultado = frutas[fruta] * cantidad
            return resultado
    return False
            
pide_frutas('manzana', 3)

#ESTE ME SALIO SI ES PARA UNA FRUTA CADA VEZ QUE SE EJECUTA.





#SEGUNDA FORMA NO TERMINADA HAY UN ERROR EN EL IF Y EN LA IGUALACION DE ELEMENTO.
#  elemento es un diccionario, le asignas valor de esta forma: elemento = dicc_frutas[nombre]
#y en un if lo comparas contra una cadena de texto, osea eso nunca va a dar True

frutas = {'banana':[200], 'anana':[800], 'manzana':[300], 'naranja': [150], 'kiwi': [600]}

def pide_frutas(nombre, cantidad):
    for fruta in frutas:
        elemento = frutas[nombre]
        resultado = cantidad * elemento
        if nombre == elemento:
            return resultado
        
    return 'Esa fruta no existe'

pide_frutas('naranja', 4)

# ESTA ES LA TERCER FORMA QUE CON EL GET NO ME SALIO.

frutas = {'banana':[200], 'anana':[800], 'manzana':[300], 'naranja': [150], 'kiwi': [600]}

def pide_frutas(nombre, indice, cantidad):
    if elemento == frutas:
        elemento = frutas.get(indice)
        resultado = elemento * cantidad
        return resultado
    else:
        return 'Esa fruta no existe'

pide_frutas('naranja', 3, 4)

