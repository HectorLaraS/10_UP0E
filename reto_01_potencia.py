def potencia(numero_base, potenciador):
    if potenciador == 1:
        return numero_base
    else:
        return numero_base * potencia(numero_base, potenciador-1)
    
if __name__ == "__main__":
    print(potencia(2,3))
    print(potencia(3,3))