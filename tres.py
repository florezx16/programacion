num_sumar = int(input("Ingrese los numeros a sumar:"))
contenido = ([449884,715898],[541785,476785],[977499,397141],[166678,117362],[554100,307752],[548423,310636],[801883,895195],[404362,828397],[660414,486866],[550337,416142],[627714,57750])

if num_sumar==11:
    for i in contenido:
         print(sum(i))

else:
    print("El numero ingresado no corresponde con el que se solicita.")
