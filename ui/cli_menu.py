from tree.persistence import save_tree, load_tree, display_upright
from tree.binary_tree import Tree
from tree.traversals import *
def run_cli():
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
                print('''📌 How to Read the Tree Display\n
                      ⚠️ This tree is shown using a text (ASCII) diagram.\n
                      Please read it like this:\n
                      1. The root is the node where the tree splits into left and right branches.\n
                      2. Lines going down-left represent LEFT children.\n
                      3. Lines going down-right represent RIGHT children.\n
                      4. The tree may not be perfectly centered — this is normal.\n
                      5. Focus on connections, not alignment.\n
                👉 This matches how trees are drawn in exams.''')
                display_upright(tree.root)
        elif option == 3:
            print("Insert/Delete Node")

            if tree is None or tree.root is None:
                print("Hey, it seems there's no tree yet.")
                print("Try to load one or create one if you didn't have any!")
            else:
                while True:
                    print("\nAlright, what do you want to do?")
                    print("1. Add node")
                    print("2. Delete node (proceed with caution!)")
                    print("3. Return")

                    try:
                        choice = int(input("Choose a number: "))
                    except ValueError:
                        print("Only numbers are accepted.")
                        continue

                    if choice == 1:
                        print("Here's your tree:")
                        display_upright(tree.root)

                        try:
                            value = int(input("Enter a number of the node: "))
                        except ValueError:
                            print("Only numbers are accepted.")
                            continue

                        success = tree.insert(value)
                        if not success:
                            print("No duplicates allowed.")
                        else:
                            save_tree(tree, current_file)

                    elif choice == 2:
                        print("Here's your tree:")
                        display_upright(tree.root)
                        print("Note: \nDeleting a node updates the current tree structure.\nThe original insertion order is kept for learning purposes.")

                        try:
                            value = int(input("Enter a number of the node: "))
                        except ValueError:
                            print("Only numbers are accepted.")
                            continue

                        success = tree.delete(value)
                        if not success:
                            print("The node doesn't exist inside the tree.")
                        else:
                            save_tree(tree, current_file)

                    elif choice == 3:
                        print("Returning to main menu...")
                        break

                    else:
                        print("Invalid selection. Please choose 1–3.")

        elif option == 4:
            if tree is None or tree.root is None:
                print("\nHey, it looks like you don’t have a tree yet.")
                print("Create one, add a few nodes, and then we can start learning together, okay?\n")
            else:
                while True:
                    print("\nAlright, this is where the learning begins!")
                    print("What are you curious about?\n")
                    print("1. Traversals (how the tree is explored)")
                    print("2. Search Operations (how values are found) [COMING SOON]")
                    print("3. Return to main menu")

                    try:
                        choice = int(input("Pick a choice: "))
                    except ValueError:
                        print("Only numbers are accepted.")
                        continue

                    if choice == 1:
                        print("Welcome to traversals. Which one would you like to explore?")
                        print("1. Preorder Traversal  (Root-Left-Right)")
                        print("2. Inorder Traversal   (Left-Root-Right)")
                        print("3. Postorder Traversal (Left-Right-Root)")
                        selection = int(input("Please let me know which one you want to learn first: "))
                        print("\nBefore we begin:")
                        print("1️⃣ Draw the entire tree on paper.")
                        print("2️⃣ Use arrows to trace how we move between nodes.")
                        print("3️⃣ ONLY write down nodes when they are VISITED.\n")
                        print("Here's the tree for your reference: ")
                        display_upright(tree.root)
                        input("Press Enter when you're ready to begin...")
                        save_tree(tree,current_file)
                        if selection == 1:
                            result = []
                            for step in preorder_step(tree.root):
                                if isinstance(step, tuple):
                                    step_type, message = step
                                    if step_type == "move":
                                        print("➡️", message)
                                    elif step_type == "visit":
                                        print("✍️ VISIT:", message, "→ mark this node")
                                    elif step_type == "return":
                                        print("↩️", message)

                                elif isinstance(step, int):
                                    result.append(step)
                                    print("Current traversal result:", result)

                                input("Press Enter to continue...")
                        if selection == 2:
                            result = []
                            for step in inorder_step(tree.root):
                                if isinstance(step, tuple):
                                    step_type, message = step
                                    if step_type == "move":
                                        print("➡️", message)
                                    elif step_type == "visit":
                                        print("✍️ VISIT:", message, "→ mark this node")
                                    elif step_type == "return":
                                        print("↩️", message)

                                elif isinstance(step, int):
                                    result.append(step)
                                    print("Current traversal result:", result)

                                input("Press Enter to continue...")
                        if selection == 3: 
                            result = []
                            for step in postorder_step(tree.root):
                                if isinstance(step, tuple):
                                    step_type, message = step
                                    if step_type == "move":
                                        print("➡️", message)
                                    elif step_type == "visit":
                                        print("✍️ VISIT:", message, "→ mark this node")
                                    elif step_type == "return":
                                        print("↩️", message)

                                elif isinstance(step, int):
                                    result.append(step)
                                    print("Current traversal result:", result)

                                input("Press Enter to continue...")
                    elif choice == 2:
                        print("This feature will be added soon!")
                        print("You will learn how Breadth-First Search, Depth First Search, etc. work!")

                    elif choice == 3:
                        print("Returning to main menu...")
                        break

                    else:
                        print("Invalid selection. Please choose 1–3.")

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
