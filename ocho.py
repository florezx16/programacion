"""
Los Datos de entrada contiene N+1 valores: el primero de ellos es N en sí (Nota que no deberías intentar convertirlo).
La Respuesta debería contener exactamente N resultados, redondeados al entero más cercano y separados por espacios.
"""
numeros = [305,497,115,270,469,430,343,152,74,344,51,392,77,559,121,266,140,585,595,417,38,93,279,512,175,584,154,59,543,448]
if len(numeros)==30:
    for i in numeros:
        F = (i-32)/1.8
        print(round(F))
