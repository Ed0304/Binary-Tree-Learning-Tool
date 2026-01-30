from tree.node import Node

class Tree:
    def __init__(self, name = "Untitled Tree"):
        self.name = name
        self.root = None
        self.insert_order = []

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            self.insert_order.append(value)
            return
        self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
                self.insert_order.append(value)
            else:
                self._insert_recursive(current.left, value)

        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
                self.insert_order.append(value)
            else:
                self._insert_recursive(current.right, value)

    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, current, value):
        if current is None:
            return None

        if value < current.value:
            current.left = self._delete_recursive(current.left, value)
        elif value > current.value:
            current.right = self._delete_recursive(current.right, value)
        else:
            if current.left is None:
                return current.right
            if current.right is None:
                return current.left

            successor = self._min_value_node(current.right)
            current.value = successor.value
            current.right = self._delete_recursive(current.right, successor.value)

        return current

    def _min_value_node(self, node):
        while node.left is not None:
            node = node.left
        return node

    def reset(self):
        self.root = None
        self.insert_order.clear()
