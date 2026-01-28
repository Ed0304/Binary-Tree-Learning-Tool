import json

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
        self.insert_order = []
    
    def save_tree(self, filename):
        data = {
            "type": "BST",
            "insert_order": self.insert_order
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    #Functions for nodes
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        self.insert_recursive(self.root, value)
        
    def insert_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
                self.insert_order.append(current.left)
            else:
                self.insert_recursive(current.left, value)
        
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
                self.insert_order.append(current.right)
            else:
                self.insert_recursive(current.right, value)
        else:
            return  # duplicate

    def delete(self, value):
        self.root = self.delete_recursive(self.root, value)

    def delete_recursive(self, current, value):
        if current is None:
            return None
        elif value < current.value:
            current.left = self.delete_recursive(current.left, value)
        elif value > current.value:
            current.right = self.delete_recursive(current.right, value)
        else:
            if current.left is None:
                return current.right
            if current.right is None:
                return current.left

            successor = self.min_value_node(current.right)
            current.value = successor.value
            current.right = self.delete_recursive(current.right, successor.value)

        return current
    
    def min_value_node(self, node):
        while node.left is not None:
            node = node.left
        return node

    def reset(self):
        self.root = None

def load_tree(filename):
    with open(filename, "r") as f:
        data = json.load(f)

    tree = Tree()
    for value in data["insert_order"]:
        tree.insert(value)

    print("Tree loaded successfully")
    return tree

# class AVLTree(Tree):
# class BSTTree(Tree):  

if __name__ == "__main__":
    tree = Tree()
    terminated = False

    while not terminated:
        print("""
Welcome to the tree learning widget
1. Create / Load tree
2. View Tree
3. Insert/Delete Node
4. Demonstrate Algorithm
5. Delete Tree
6. Convert Tree (Coming Soon)
7. Exit Program
""")

        try:
            option = int(input("Type a number (1-7): "))
        except ValueError:
            print("Invalid input.")
            continue

        if option == 1:
            choice = None
            while choice is not int :
                try:
                    print("Please select an option")
                    print("1. Create tree")
                    print("2. Load tree")
                    print("3. Back")
                    choice = int(input("Please type a number: "))
                except ValueError:
                    print("Invalid option. Please enter a number.")
                    continue

                if choice == 1:
                    print("Creating new tree...")
                    tree.reset()
                    tree.insert_order = []
                    filename = input("Type filename (stored as JSON)")
                    filename += ".json"
                    tree.save_tree(filename)
                    print("Tree saved.")

                elif choice == 2:
                    print("Loading tree...")
                    # load_tree logic here

                elif choice == 3:
                    break #Return to main menu

                else:
                    print("Choose another number.")

        elif option == 2:
            print("View tree")
        elif option == 3:
            pass
        elif option == 5:
            tree.reset()
            print("Tree deleted.")
        elif option == 7:
            print("Thank you for using this tool!")
            terminated = True
        else:
            print("Please choose another number.")
