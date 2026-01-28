from tree.persistence import save_tree, load_tree

def run_cli(tree):
    terminated = False

    while not terminated:
        print("""
Welcome to the tree learning widget
1. Create / Load tree
2. View Tree
3. Insert/Delete Node
5. Delete Tree
7. Exit Program
""")

        try:
            option = int(input("Type a number (1-7): "))
        except ValueError:
            print("Invalid input.")
            continue

        if option == 1:
            filename = input("Filename (without .json): ") + ".json"
            save_tree(tree, filename)
            print("Tree saved.")

        elif option == 5:
            tree.reset()
            print("Tree deleted.")

        elif option == 7:
            print("Thank you for using this tool!")
            terminated = True
