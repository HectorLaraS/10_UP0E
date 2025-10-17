print("Argumentos Variables".center(50,"*"))

def superheroe_superpoder(superheroe, nombre, *args):
    print(f"Superheroe: {superheroe} - {nombre} - {args}")

    for poder in args:
        print(f"Poder: {poder}")

superheroe_superpoder("Superman", "Clark Kent", "volar", "Superfuerza")
