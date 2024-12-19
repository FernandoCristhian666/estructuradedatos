from collections import deque

class AnalizadorSintactico:
    def __init__(self):
        self.pila = deque()  # Pila para paréntesis
        self.operandos = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")  # Operandos válidos
        self.operadores = set("+-*/^")  
    
    def validar(self, expresion):
        
        for caracter in expresion:
            if caracter == "(":
                self.pila.append(caracter)
            elif caracter == ")":
                if not self.pila or self.pila[-1] != "(":
                    return "Error: Paréntesis desbalanceados"
                self.pila.pop()

        if self.pila:
            return "Error: Paréntesis desbalanceados"
        
        
        for i in range(len(expresion) - 1):
            if (expresion[i] in self.operadores and expresion[i+1] in self.operadores) or \
               (expresion[i] == "(" and expresion[i+1] == ")"):
                return "Error: Operadores mal ubicados o paréntesis mal usados"
        
        return "Expresión válida"
    
# EJEMPLO
analizador = AnalizadorSintactico()
expresion = "((a + b) * c)"
resultado = analizador.validar(expresion)
print(resultado)
