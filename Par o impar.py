while True:
    entrada = input("Introduce un número (o escribe 'salir'): ")

    if entrada.lower() == 'salir':
        print("Programa terminado.")
        break

    num = int(entrada)
    if num % 2 == 0:
        print("Es par")
    else:
        print("Es impar")



