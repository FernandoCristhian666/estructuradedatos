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

# Ejemplo de uso
stack = ArrayStack()
stack.push(10)
stack.push(20)
print(stack.peek())  # Salida: 20
print(stack.pop())   # Salida: 20
print(stack.is_empty())  # Salida: False