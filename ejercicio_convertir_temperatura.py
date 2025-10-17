def convertir_temperatura_farenheit(temperatura):
    return (temperatura * (9/5)) + 32

def convertir_temperatura_celcius(temperatura):
    return (temperatura - 32) * (5/9)

def main():
    while True:
        entrada_selector = input("Quiere Convertir C -> F | F -> C (1 o 2): ")
        if entrada_selector == "1": 
            entrada_temperatura = float(input("Ingrese temperatura en Celcius: "))
            temperatura_nueva = convertir_temperatura_farenheit(entrada_temperatura)
            print(f"usted ingreso: {entrada_temperatura}°C en Farenheit es {temperatura_nueva}")
        elif entrada_selector == "2":
            entrada_temperatura = float(input("Ingrese temperatura en Farenheit: "))
            temperatura_nueva = convertir_temperatura_celcius(entrada_temperatura)
            print(f"usted ingreso: {entrada_temperatura}°F en Celcius es {temperatura_nueva}")
        else:
            print("opcion no valida")

if __name__ == "__main__":
    main()