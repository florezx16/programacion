num_sumar = int(input("Ingrese los numeros a sumar:"))
contenido = ([-6534428,2013204],[-3621801,3366987],[18295,560],[13823,1302],[-1816392,-1626988],[695716,1084886],[6254570,-3359382],[8365,1196],[16627,1196],[5548085,232],[5159,1048],[4141485,2237740],[4703659,617],[-3097945,-2690371],[17155,1424])

if num_sumar==15:
    for i in contenido:
         num1 = i[0]
         num2 = i[1]
         resultado = num1/num2
         print(round(resultado))


else:
    print("El numero ingresado no corresponde con el que se solicita.")
