import json
from tree.binary_tree import Tree

def save_tree(tree: Tree, filename: str):
    data = {
        "type": "BST",
        "insert_order": tree.insert_order
    }
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def load_tree(filename: str) -> Tree:
    with open(filename, "r") as f:
        data = json.load(f)

    tree = Tree()
    for value in data.get("insert_order", []):
        tree.insert(value)

    return tree
