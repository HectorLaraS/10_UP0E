def es_par(numero: int) -> bool:
    res = False
    if numero % 2 == 0:
        res = True
    else: 
        res = False
    return res

if __name__ == "__main__":
    numero_in = int(input("Proporciona numero entero: "))
    print(f"Tu numero es par? = {es_par(numero_in)}")