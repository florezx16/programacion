"""
Los Datos de entrada están en el siguiente formato:

    la primera línea contiene N - el número de valores a procesar;
    y después siguen N líneas que describen los valores para los cuales la suma de dígitos debe ser calculada mediante 3 enteros A B C;
    para cada caso, necesitarás multiplicar A por B y sumar C (ej.: A * B + C) - luego calcular la suma de dígitos del resultado.

La Respuesta debería constar de N resultados, separados también por espacios.
"""
numeros = ([322,143,41],[312,291,49],[245,217,114],[383,196,145],[301,139,17],[265,174,192],[193,163,44],[219,192,192],[57,234,34],[30,26,134])
for i in numeros:
    p1 = i[0]
    p2 = i[1]
    p3 = i[2]
    r1 = p1*p2+p3
    num = str(r1)
    lista = []
    for n in num:
        lista.append(int(n))

    print(sum(lista))
