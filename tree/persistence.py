import json
from tree.binary_tree import Tree
from tree.node import *

def save_tree(tree: Tree, filename: str):
    data = {
        "name": tree.name,
        "type": "BST",
        "insert_order": tree.insert_order
    }
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def load_tree(filename: str) -> Tree:
    try:
        with open(filename, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"[Error] {filename} not found.")
        return Tree()

    tree_name = data.get("name", "Untitled Tree")
    tree = Tree(name=tree_name)

    for value in data.get("insert_order", []):
        tree.insert(value)

    return tree

def display_upright(node, prefix="", is_left=True, is_root=True):
    if node is None:
        return

    if node.right:
        new_prefix = prefix + ("│   " if not is_root and is_left else "    ")
        display_upright(node.right, new_prefix, False, False)

    if is_root:
        print(prefix + str(node.value))
    else:
        connector = "└── " if is_left else "┌── "
        print(prefix + connector + str(node.value))

    if node.left:
        new_prefix = prefix + ("    " if is_left else "│   ")
        display_upright(node.left, new_prefix, True, False)




