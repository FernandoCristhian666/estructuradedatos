class ArrayStack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("La pila está vacía.")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("La pila está vacía.")
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

def evaluate_postfix(expression):
    stack = ArrayStack()
    operators = {'+': lambda x, y: x + y,
                 '-': lambda x, y: x - y,
                 '*': lambda x, y: x * y,
                 '/': lambda x, y: x / y}

    for char in expression.split():
        if char.isdigit():
            stack.push(int(char))
        elif char in operators:
            b = stack.pop()
            a = stack.pop()
            stack.push(operators[char](a, b))
        else:
            raise ValueError(f"Carácter desconocido: {char}")

    return stack.pop()

# Ejemplo de uso
expression = "5 6 + 3 *"  # Notación posfija de (5 + 6) * 3
result = evaluate_postfix(expression)
print("Resultado:", result)  # Salida: 33