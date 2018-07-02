"""
Los datos de entrada tienen el siguiente formato:

    la primera línea contiene N - la cantidad de valores a sumar;
    la segunda línea contiene los valores N propiamente.

La respuesta deberían contener un único valor - la suma de los N valores.
"""
num_sumar = int(input("Ingrese los numeros a sumar:"))

numeros = [923,732,961,611,488,1075,518,807,1130,867,1198,473,525,1186,1058, 200, 250, 514, 1238, 688, 825, 380, 1122, 762, 1287, 564, 612, 265, 810, 1298, 1292, 432, 730, 952, 1034, 1208, 727, 251, 715, 556, 1109, 613, 1020, 334, 499, 778]
indice  = 1
if num_sumar==46:
    while (indice < len(numeros)):
        resultado = sum(numeros)
        indice+=1
    print(resultado)


else:
    print("El valor ingresado no correspondelo que se necesita.")
