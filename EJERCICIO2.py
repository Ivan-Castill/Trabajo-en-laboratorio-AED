#Solicitar al usuario sus datos
print("\n-------------------------------------------")
print("--------BIENVENIDO QUERIDO USUARIO--------\n ") 
nombre= input("  Por favor ingrese su apellido y nombre:\n   ")
cedula= input("  Por favor ingrese su numero de cedula:\n   ")
salario= float(input("  Por favor ingrese su salario:\n   "))
telefono= input("  Por favor ingrese su numero de telefono:\n   ")
#Definir los porcentajes
incrementoPorcentaje= { "A":0.03, "B": 0.10 , "C": 0.25 , "D": 0.45}
#Ingresar el tipo de contrato
tipoContrato=input("  Ingrese su tipo de contrato \n   A = Inicial\n   B = Medio\n   C = Intermedio\n   D = Avanzado \n  Por favor escribalo con letras mayusculas \n  :")
#Realizar el procedimiento
if tipoContrato not in incrementoPorcentaje:
    print("Tipo de contrato no valido")
else:
    aumento=(salario*incrementoPorcentaje[tipoContrato])
    nuevoSaldo=(aumento+salario)
    incrementPorcentaje=incrementoPorcentaje[tipoContrato]*100

#Imprimir los resultados
print("  ....Nuevo salario....")
print("  Nombre: ", nombre)
print("  Cedula: ", cedula)
print("  Telefono: ", telefono)
print("  Su salario actual: ", salario, "$")
print("  Porcentaje añadido es: ", incrementPorcentaje, "%")
print("  Su nuevo salario es: ",nuevoSaldo, "$")
print("         ....Fin....\n ")