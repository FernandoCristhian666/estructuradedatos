lass Node:
    def __init__(self, key, priority):
        self.key = key
        self.priority = priority
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def insert(self, node, key, priority):
        if not node:
            return Node(key, priority)
        
        if priority < node.priority:
            node.left = self.insert(node.left, key, priority)
        else:
            node.right = self.insert(node.right, key, priority)
        
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)
        
        if balance > 1 and priority < node.left.priority:
            return self.rotate_right(node)
        if balance < -1 and priority > node.right.priority:
            return self.rotate_left(node)
        if balance > 1 and priority > node.left.priority:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance < -1 and priority < node.right.priority:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        
        return node

    def pre_order(self, node):
        if node:
            print(f"{node.key} ({node.priority})", end=" ")
            self.pre_order(node.left)
            self.pre_order(node.right)

# EJEMPLO
tree = AVLTree()
root = None
root = tree.insert(root, "Paciente A", 3)
root = tree.insert(root, "Paciente B", 1)
root = tree.insert(root, "Paciente C", 2)
tree.pre_order(root)