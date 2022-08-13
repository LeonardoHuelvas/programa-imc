print ("Bienvenido a tu Calculadora de IMC \n")
respuesta = "S"
while respuesta != "N":

    peso = float(input("Ingrese su peso en kg: "))
    alturaEnCm = int (input ("Ingrese su altura en cm: "))
    alturaEnMetros = alturaEnCm / 100

    imc = peso / (alturaEnMetros * alturaEnMetros)


    print ("Su indice de masa corpotal es " + str(imc))
   


    if imc < 20:
        print ("Estado de Bajo peso")
    if imc>= 20 and imc <26:
        print ("Peso normal ")
    if imc >= 26 and imc < 30:
        print ("Estado de Sobre peso")    
    if imc >= 30:
        print ("Estado de Obesidad")    
    respuesta = input("¿Desea calcular otro IMC? (s/n)").upper()