# Variables de almacenamiento para el registro de usuario
emailSG = ""
passwrdSG = ""
boolean = True

print("\n-------------------------------------------")
print("--------BIENVENIDO QUERIDO USUARIO--------\n ") 

while boolean:
    # Solicitar acción al usuario
    action = input("  ¿Desea iniciar sesión (LOGIN) o registrarse (SIGNUP)?:\n  ").upper()
    if action == "LOGIN":
        emailLG = input("  Ingrese su correo electrónico:\n  ")
        passwrdLG = input("  Ingrese su contraseña:\n  ")
        #tomar en cuenta que el correo es (email12) y la contraseña es (passwrdS23).
        if (emailLG == "email12") and (passwrdLG == "passwrdS23"): 
            print("  --------Inicio de sesión exitoso, ¡Bienvenido!--------")
            boolean = False
        else:
            print("  --------Correo electrónico o contraseña inválidos--------")
    elif action == "SIGNUP": #registro del ususario
        emailSG = input("  Ingrese su correo electrónico:\n ")
        passwrdSG = input("Ingrese su contraseña:\n ")
        print("  --------Registro exitoso. Ahora puede iniciar sesión.--------")
    else:
        print("  --------Ocurrió un error. Por favor, inténtelo nuevamente.--------")
