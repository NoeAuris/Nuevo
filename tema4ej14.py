def es_subconjunto(subconjunto, conjunto):
    for i in subconjunto:
        for j in conjunto:
            if i != j:
                return False
    return True
es_subconjunto([5, 0, 3, 33],[5, 0, 3,33,4])

# ESTE NO ME SALIO.