"""
Los Datos de entrada contendrá el número de casos de prueba en la primera línea.
Las siguientes líneas tendrán los pares de números que habrá que comparar entre sí.
Para la Respuesta por favor introduce la misma cantidad de mínimos separados por espacios
"""
num_sumar = int(input("Ingrese los numeros a sumar:"))
contenido = ([-4326419,3584985],[-2612810,-1285715],[-5587439,-9587497],[-4949203,5416260],[-4607413,4042805],[-3668454,4785435],[3111790,5575069],[9162561,-3085978],[-5562478,-8503978],[-9323622,6426800],[-9605902,-5979329],[4682426,-1124930],[8802658,2259703],[-8100610,-1029910],[-4091717,6761267],[4308246,1581863],[346252,-8304563],[-9703851,4758813],[-7892060,-4653055],[175073,-2499474],[9389750,6506618],[-7714039,2501540])

if num_sumar==22:
    for i in contenido:
         num1 = i[0]
         num2 = i[1]
         if num1<num2:
             print(num1)
         else:
            print(num2)

else:
    print("El numero ingresado no corresponde con el que se solicita.")
