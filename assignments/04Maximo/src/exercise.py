def main():
    #escribe tu código abajo de esta línea
    x = int(input("Ingresa el primer número: "))
    y = int(input("Ingresa el segundo número: "))
    z = int(input("Ingresa el tercer número: "))
    if x <= y and x <= z and y <= z:
        print(x)
        print(y)
        print(z)
    elif x <= y and x <= z and z <= y:
        print(x)
        print(z)
        print(y)
    elif y <= x and y <= z and x <= z:
        print(y)
        print(x)
        print(z)
    elif y <= x and y <= z and z <= x:
        print(y)
        print(z)
        print(x)
    elif z <= x and z <= y and x <= y:
        print(z)
        print(x)
        print(y)
    elif z <= x and z <= y and y <= x:
        print(z)
        print(y)
        print(x)
    pass


if __name__=='__main__':
    main()
