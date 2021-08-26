
def main():
    #Escribe tu código debajo de esta línea
    edad = int(input("Ingresa tu edad: "))
    if edad >= 1 and edad < 18:
        print("No cumples requisitos")
    elif edad < 1:
        print("Respuesta incorrecta")
    else:
        idn = str(input("¿Tienes identificación oficial? (s/n): "))
        if idn == "s":
            print("Trámite de licencia concedido")
        elif idn == "n":
            print("No cumples requisitos")
        elif idn != "s" or idn != "n":
            print("Respuesta incorrecta")
    pass


if __name__ == '__main__':
    main()
