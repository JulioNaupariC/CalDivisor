def calcular_divisores(numero):
    divisores = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)
    return divisores

while True:
    try:
        # Pedir un número al usuario
        numero = int(input("Ingrese un número natural: "))
        if numero <= 0:
            raise ValueError("Debe ser un número natural positivo.")
        # Calcular y mostrar los divisores
        divisores = calcular_divisores(numero)
        print(f"Los divisores de {numero} son: {divisores}")
        break
    except ValueError as e:
        print(f"Error: {e}. Intente nuevamente.")