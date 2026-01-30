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

def display_tree(node,level = 0):
    if node is None:
        return 
    
    display_tree(node.right,level+1)
    print("   " * level + str(node.value))
    display_tree(node.left,level+1)



