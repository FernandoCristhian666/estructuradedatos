class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolExpresion:
    def __init__(self):
        self.raiz = None

    def evaluar(self, nodo):
        if nodo is None:
            return 0
        if nodo.valor in ['+', '-', '*', '/']:
            if nodo.valor == '+':
                return self.evaluar(nodo.izquierda) + self.evaluar(nodo.derecha)
            elif nodo.valor == '-':
                return self.evaluar(nodo.izquierda) - self.evaluar(nodo.derecha)
            elif nodo.valor == '*':
                return self.evaluar(nodo.izquierda) * self.evaluar(nodo.derecha)
            elif nodo.valor == '/':
                return self.evaluar(nodo.izquierda) / self.evaluar(nodo.derecha)
        else:
            return nodo.valor

# EJEMPLO
arbol = ArbolExpresion()


raiz = Nodo('+')
raiz.izquierda = Nodo(3)

nodo_multiplicacion = Nodo('*')
nodo_multiplicacion.izquierda = Nodo(5)

nodo_resta = Nodo('-')
nodo_resta.izquierda = Nodo(2)
nodo_resta.derecha = Nodo(8)

nodo_multiplicacion.derecha = nodo_resta
raiz.derecha = nodo_multiplicacion

arbol.raiz = raiz

print(arbol.evaluar(arbol.raiz))