MENU = """
1) SUMAR
2) RESTAR
3) MULTIPLICAR
4) DIVIDIR
5) SALIR
"""
def validar_numero(mensaje: str, mensaje_error: str):
    usr_input = None
    usr_output = None
    while True:
        try:
            usr_input = input(f"{mensaje}: ")
            usr_output = round(float(usr_input),2)
            break
        except:
            print(f"{mensaje_error}")
    return usr_output

def sumar() -> float:
    mensaje_error = "Opcion no Valida!!!"
    numero_1 = validar_numero("ingrese primer numero", mensaje_error)
    numero_2 = validar_numero("Ingrese segundor numero", mensaje_error)
    return numero_1 + numero_2

def restar() -> float:
    mensaje_error = "Opcion no Valida!!!"
    numero_1 = validar_numero("ingrese primer numero", mensaje_error)
    numero_2 = validar_numero("Ingrese segundor numero", mensaje_error)
    return numero_1 - numero_2

def multiplicar() -> float:
    mensaje_error = "Opcion no Valida!!!"
    numero_1 = validar_numero("ingrese primer numero", mensaje_error)
    numero_2 = validar_numero("Ingrese segundor numero", mensaje_error)
    return numero_1 * numero_2

def dividir() -> float:
    mensaje_error = "Opcion no Valida!!!"
    numero_1 = validar_numero("ingrese numerador numero", mensaje_error)
    while True:
        numero_2 = validar_numero("Ingrese denominador numero", mensaje_error)
        if numero_2 != 0:
            break
        else:
            print("Ingrese un numero diferente de 0")
    return numero_1 / numero_2

def menu():
    salir = False
    while not salir:
        print(MENU)
        opcion = validar_numero("Ingrese la opcion que requiera", "Ingrese un numero")
        if opcion == 1:
            print(f"\n SU RESULTADO ES: {sumar()} \n")
        elif opcion == 2:
            print(f"\n SU RESULTADO ES: {restar()} \n")
        elif opcion == 3:
            print(f"\n SU RESULTADO ES: {multiplicar()} \n")
        elif opcion == 4:
            print(f"\n SU RESULTADO ES: {dividir()} \n")
        elif opcion == 5:
            print("ADIOS !!!")
            salir = True
        else: 
            print("SELECCIONE OPCION VALIDA!!!")


if __name__ == "__main__":
    menu()