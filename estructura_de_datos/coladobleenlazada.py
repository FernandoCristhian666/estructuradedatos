class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

class ColaDoblementeEnlazada:
    def __init__(self):
        self.frente = None
        self.atras = None

    def encolar(self, valor):
        nodo = Nodo(valor)
        if self.atras is None:
            self.frente = nodo
            self.atras = nodo
        else:
            self.atras.siguiente = nodo
            nodo.anterior = self.atras
            self.atras = nodo

    def desencolar(self):
        if self.frente is None:
            return None
        valor = self.frente.valor
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.atras = None
        else:
            self.frente.anterior = None
        return valor


# EJEMPLO

cola = ColaDoblementeEnlazada()
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)

print(cola.desencolar()) 
print(cola.desencolar()) 
print(cola.desencolar()) 