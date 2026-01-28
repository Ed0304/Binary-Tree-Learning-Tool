from tree.persistence import save_tree, load_tree
from tree.binary_tree import Tree

def run_cli(tree):
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
                    tree = Tree()
                    print("Creating new tree...")
                    tree.insert_order = []
                    filename = input("Type filename (stored as JSON): ")
                    filename += ".json"
                    save_tree(tree,filename)
                    print("Tree saved.")
                    tree.reset()

                elif choice == 2:
                    print("Loading tree...")
                    filename = input("Enter the filename:") + ".json"

                    loaded_tree = load_tree(filename)
                    tree.root = loaded_tree.root
                    tree.insert_order = loaded_tree.insert_order

                    print("Tree loaded")

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
