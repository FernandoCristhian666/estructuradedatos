def buscar_numero(lista, objetivo):
    """
    Busca un número en una lista usando búsqueda lineal.

    :param lista: Lista de números donde buscar.
    :param objetivo: Número a buscar.
    :return: Índice del número si se encuentra, -1 en caso contrario.
    """
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

# Prueba del código original
if __name__ == "__main__":
    lista = [1, 3, 5, 7, 9, 11, 13, 15]
    objetivo = 7
    resultado = buscar_numero(lista, objetivo)
    print(f"Resultado: {resultado}")