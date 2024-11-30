def buscar_numero(lista, objetivo):
    
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

# Prueba del código optimizado
if __name__ == "__main__":
    lista = [1, 3, 5, 7, 9, 11, 13, 15]
    objetivo = 7
    resultado = buscar_numero(lista, objetivo)
    print(f"Resultado: {resultado}")  # Debería imprimir 3