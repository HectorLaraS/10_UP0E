def factorial(numero: int):
    if numero == 1: 
        print(numero)
    else:
        factorial(numero - 1)
        print(numero)

def factorial_2(numero: int ):
    if numero == 1:
        return 1
    else:
        return numero * factorial_2(numero  - 1)

if __name__ == "__main__":
    factorial(5)
    res = factorial_2(5)
    print(res)