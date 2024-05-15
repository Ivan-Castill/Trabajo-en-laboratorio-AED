#el área de la placa
#bienvenida al usuario
print("\n-------------------------------------------")
print("--------BIENVENIDO QUERIDO USUARIO--------\n \n---------------Programa.✨ ---------------\nCalcular el area de la placa en forma de trapecio.") 
base_mayor=float(input("\n-Ingrese el valor de la base mayor\n en centrimetros(cm): "))#optencion de datos para calcular el area
base_menor=float(input("\n-Ingrese el valor de la base menor\n en centrimetros(cm): "))
altura=float(input("\n-Ingrese el valor de la altura\n en centrimetros(cm): "))
area=((base_mayor+base_menor)*altura)/2

#final del programa con el resultado 
print(f"\n--- La area de la Placa es: {area} centrimetros cuadrados --- \n ")
print("--------QUE TENGA UN GRAN DIA--------\n")