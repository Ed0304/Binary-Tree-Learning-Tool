from tree.persistence import save_tree, load_tree, display_tree
from tree.binary_tree import Tree

def run_cli(tree):
    tree = None 
    current_file = None
    terminated = False
    while not terminated:
        print("""
Welcome to the tree learning widget
1. Create / Load tree
2. View Tree
3. Insert/Delete Node
4. Demonstrate Algorithm
5. Remove Loaded Tree
6. Convert Tree (Coming Soon)
7. Exit Program
""")

        try:
            if tree is None or tree.root is None:
                print("No tree loaded yet — create or load a tree to start learning!")
            else:
                print(f"Current Tree: {tree.name}")

                if len(tree.insert_order) == 1:
                    print("It looks like there’s only one node so far. Let’s add a few more!")
                elif len(tree.insert_order) == 2:
                    print("Nice! You’ve added one more node — that’s a great starting point.")
                    print("How about adding a few extra nodes?")
                else:
                    print("Great! You’re ready to learn.")
                    print("Select option 4 and let’s explore trees together!")

            
            option = int(input("Type a number (1-7): "))
        except ValueError:
            print("Invalid input.")
            continue

        if option == 1:
            choice = None
            while choice is not int :
                try:
                    print("Please select an option")
                    print("Tip: If you are new here, pick 1, and create a new tree to start learning together!")
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
                    try:
                        root = int(input("Type the starting value of the tree: "))
                        tree.insert_order = [root]
                        filename = input("Type filename (stored as JSON): ")
                        filename += ".json"
                        current_file = filename
                        tree_name = input("Enter tree name: ")
                        tree.name = tree_name
                        save_tree(tree,current_file)
                        print("Tree saved.")
                        tree.reset()
                    except ValueError:
                        print("Invalid value for the root.")

                    

                elif choice == 2:
                    filename = input("Enter the filename: ").strip() + ".json"
                    tree = load_tree(filename)
                    current_file = filename


                    if tree.root is None:
                        print("Loaded file contains an empty tree.")
                    else:
                        print("Tree loaded successfully.")
                        
                    break

                elif choice == 3:
                    break #Return to main menu

                else:
                    print("Choose another number.")

        elif option == 2:
            print("View tree")
            if tree is None or tree.root is None:
                print("Please upload a tree first.")
            else:
                display_tree(tree.root,0)
        elif option == 3:
            print("Insert/Delete Node")
            if tree is None or tree.root is None:
                print("Hey, it seems there's no tree yet.")
                print("Try to load one or create one if you didn't have any!")
            else:
                while choice is not int:
                    print("Alright, what do you want to do?")
                    print("1. Add node")
                    print("2. Delete node (proceed with caution!)")
                    print("3. Return")
                    choice = int(input("Choose a number: "))
                    try:
                        if choice == 1:
                            
                            try:
                                value = int(input("Enter a number of the node: "))
                                tree.insert(value)
                                save_tree(tree,current_file)
                            except ValueError:
                                print("Only numbers are accepted.")
                        
                        elif choice == 2:

                            try:
                                value = int(input("Enter a number of the node: "))
                                if value not in tree.insert_order:
                                    print("The node doesn't exist inside the tree")
                                else:
                                    tree.delete(value)
                                    save_tree(tree,current_file)
                            except ValueError:
                                print("Only numbers are accepted.")
                        elif choice == 3:
                            print("Returning to main menu...")
                            break
                            
                    except ValueError:
                        print("Invalid selection. Please type a number.")
        elif option == 4:
            if tree is None or tree.root is None:
                print("\nHey, it looks like you don’t have a tree yet.")
                print("Create one, add a few nodes, and then we can start learning together, okay?\n")
            else:
                print("\nAlright, this is where the learning begins!")
                print("What are you curious about?\n")
                print("1. Traversals (how the tree is explored)")
                print("2. Search Operations (how values are found)")
                print("3. Return to main menu")
        elif option == 5:
            tree = None
            print("Loaded tree removed.")
        elif option == 6: 
            print("Tree conversion isn’t available yet, but it’s on the roadmap.")
            print("For now, feel free to explore traversals and searches!")
        elif option == 7:
            print("Alright, see you later! If this helped you with exams or interviews, I’m glad it did 🙂")
            terminated = True
        else:
            print("Please choose another number.")
