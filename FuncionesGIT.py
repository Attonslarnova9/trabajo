def dado6():
    from random import randint
    x = randint(1, 6)
    print(f"Resultado del dado: {x}")


def moneda():
    from random import randint
    x = randint(1, 2)
    if x == 1:
        print("Resultado: Cara")
    else:
        print("Resultado: Cruz")


def dado100():
    from random import randint
    x = randint(1, 100)
    print(f"Resultado del dado: {x}")
