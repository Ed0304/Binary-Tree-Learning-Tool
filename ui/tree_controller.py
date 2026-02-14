from tree.binary_tree import Tree
from tree.persistence import save_tree, load_tree
from tree.traversals import (
    preorder_step,
    inorder_step,
    postorder_step
)

class TreeController:
    def __init__(self):
        self.tree = None
        self.current_file = None

    def create_tree(self, root_value, name):
        self.tree = Tree()
        self.tree.name = name
        self.tree.insert(root_value)


    def load_tree(self, filename):
        self.tree = load_tree(filename)
        self.current_file = filename
        return self.tree

    def save(self):
        if self.tree and self.current_file:
            save_tree(self.tree, self.current_file)

    def insert(self, value):
        if not self.tree:
            return False
        success = self.tree.insert(value)
        self.save()
        return success

    def delete(self, value):
        if not self.tree:
            return False

        success = self.tree.delete(value)

        if success:
            if value in self.tree.insert_order:
                self.tree.insert_order.remove(value)

        self.save()
        return success


    def get_traversal_generator(self, traversal_type):
        if not self.tree:
            return None

        if traversal_type == "preorder":
            return preorder_step(self.tree.root)
        elif traversal_type == "inorder":
            return inorder_step(self.tree.root)
        elif traversal_type == "postorder":
            return postorder_step(self.tree.root)

        return None
