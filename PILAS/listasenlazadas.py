class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("La pila está vacía.")
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("La pila está vacía.")
        return self.top.value

    def is_empty(self):
        return self.top is None

# Ejemplo de uso
stack = LinkedListStack()
stack.push(10)
stack.push(20)
print(stack.peek())  # Salida: 20
print(stack.pop())   # Salida: 20
print(stack.is_empty())  # Salida: False