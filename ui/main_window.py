from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout,
    QPushButton, QHBoxLayout
)
from PySide6.QtWidgets import (
    QLineEdit, QLabel
)
from PySide6.QtWidgets import QFileDialog
from ui.tree_canvas import TreeCanvas
from ui.tree_controller import TreeController
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QInputDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.is_modified = False
        self.statusBar().showMessage("Ready.")
        self.setWindowTitle("Binary Tree Visualizer v1.0")
        self.resize(900, 600)
        self.controller = TreeController()

        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout()
        central.setLayout(layout)

        # Button row
        button_layout = QHBoxLayout()
        self.preorder_btn = QPushButton("Preorder Traversal")
        self.inorder_btn = QPushButton("Inorder Traversal")
        self.postorder_btn = QPushButton("Postorder Traversal")
        self.preorder_btn.clicked.connect(
            lambda: self.select_traversal("preorder")
        )
        self.inorder_btn.clicked.connect(
            lambda: self.select_traversal("inorder")
        )
        self.postorder_btn.clicked.connect(
            lambda: self.select_traversal("postorder")
        )

        button_layout.addWidget(self.preorder_btn)
        button_layout.addWidget(self.inorder_btn)
        button_layout.addWidget(self.postorder_btn)

        layout.addLayout(button_layout)

        # Canvas
        self.canvas = TreeCanvas()
        layout.addWidget(self.canvas)

        # ---- Tree Controls ----
        tree_controls = QHBoxLayout()

        self.value_input = QLineEdit()
        self.value_input.setPlaceholderText("Enter value")

        self.insert_btn = QPushButton("Insert Node")
        self.delete_btn = QPushButton("Delete Node")
        self.create_btn = QPushButton("Create Tree")
        self.rename_btn = QPushButton("Rename Tree")
        self.reset_btn = QPushButton("Reset")
        self.save_btn = QPushButton("Save")
        self.save_as_btn = QPushButton("Save As")
        self.load_btn = QPushButton("Load")
        self.start_btn = QPushButton("Start")
        self.next_btn = QPushButton("Next Step")
        self.reset_traversal_btn = QPushButton("Reset Traversal")
        self.start_btn.setEnabled(False)
        self.next_btn.setEnabled(False)
        self.reset_traversal_btn.setEnabled(False)

        self.insert_btn.clicked.connect(self.insert_node)
        self.delete_btn.clicked.connect(self.delete_node)
        self.create_btn.clicked.connect(self.create_tree)
        self.reset_btn.clicked.connect(self.reset_tree)
        self.save_btn.clicked.connect(self.save_tree)
        self.save_as_btn.clicked.connect(self.save_tree_as)
        self.load_btn.clicked.connect(self.load_tree)
        self.rename_btn.clicked.connect(self.rename_tree)


        tree_controls.addWidget(self.value_input)
        tree_controls.addWidget(self.insert_btn)
        tree_controls.addWidget(self.delete_btn)
        tree_controls.addWidget(self.create_btn)
        tree_controls.addWidget(self.reset_btn)
        tree_controls.addWidget(self.save_btn)
        tree_controls.addWidget(self.save_as_btn)
        tree_controls.addWidget(self.load_btn)
        tree_controls.addWidget(self.rename_btn)
        layout.addLayout(tree_controls)

        # ---- Traversal Controls ----
        traversal_controls = QHBoxLayout()

        traversal_controls.addWidget(self.start_btn)
        traversal_controls.addWidget(self.next_btn)
        traversal_controls.addWidget(self.reset_traversal_btn)
        layout.addLayout(traversal_controls)
        self.explanation_label = QLabel("Select a traversal to begin.")
        self.explanation_label.setWordWrap(True)
        layout.addWidget(self.explanation_label)


        self.start_btn.clicked.connect(self.prepare_traversal)
        self.next_btn.clicked.connect(self.next_step)
        self.reset_traversal_btn.clicked.connect(self.reset_traversal)


    
    def create_tree(self):
        text = self.value_input.text()
        self.controller.current_file = None  # new tree not yet saved
        self.update_window_title()
        

        if not text:
            QMessageBox.warning(self, "Input Required", "Please enter a value for the root.")
            return

        try:
            value = int(text)
            self.controller.create_tree(value, "GUI Tree")
            self.canvas.draw_tree(self.controller.tree.root)
            self.statusBar().showMessage("Tree created successfully.", 3000)
            self.explanation_label.setText("Tree created. Select a traversal.")
            self.is_modified = True
            self.update_window_title()
            
        except ValueError:
            QMessageBox.critical(self, "Invalid Input", "Root value must be an integer.")

    
    def insert_node(self):
        if not self.controller.tree:
            QMessageBox.warning(self, "No Tree", "Create a tree first.")
            return

        text = self.value_input.text()

        try:
            value = int(text)
            success = self.controller.insert(value)

            if success:
                self.canvas.draw_tree(self.controller.tree.root)
                self.statusBar().showMessage(f"Inserted {value}.", 3000)
                self.is_modified = True
                self.update_window_title()
            else:
                QMessageBox.warning(self, "Duplicate Value", "No duplicates allowed.")

        except ValueError:
            QMessageBox.critical(self, "Invalid Input", "Please enter a valid integer.")

    
    def delete_node(self):
        if not self.controller.tree:
            QMessageBox.warning(self, "No Tree", "Create a tree first.")
            return

        text = self.value_input.text()

        try:
            value = int(text)
            success = self.controller.delete(value)

            if success:
                self.canvas.draw_tree(self.controller.tree.root)
                self.statusBar().showMessage(f"Deleted {value}.", 3000)
                self.is_modified = True
                self.update_window_title()
            else:
                QMessageBox.warning(self, "Not Found", "Node not found in tree.")

        except ValueError:
            QMessageBox.critical(self, "Invalid Input", "Please enter a valid integer.")


    def reset_tree(self):
        if self.is_modified:
            reply = QMessageBox.question(
                self,
                "Unsaved Changes",
                "You have unsaved changes. Continue without saving?",
                QMessageBox.Yes | QMessageBox.No
            )

            if reply == QMessageBox.No:
                return
        self.controller.tree = None
        self.controller.current_file = None
        self.update_window_title()
        self.start_btn.setEnabled(False)
        self.next_btn.setEnabled(False)
        self.reset_traversal_btn.setEnabled(False)
        self.canvas.scene.clear()

    def save_tree(self):
        if not self.controller.tree:
            QMessageBox.warning(self, "No Tree", "Nothing to save.")
            return

        if not self.controller.current_file:
            self.save_tree_as()
            return

        self.controller.save()
        self.statusBar().showMessage("Tree saved.", 3000)
        self.is_modified = False
        self.update_window_title()

    
    def save_tree_as(self):
        if not self.controller.tree:
            QMessageBox.warning(self, "No Tree", "Nothing to save.")
            return

        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Tree As",
            "",
            "JSON Files (*.json)"
        )
        self.update_window_title()

        if file_path:
            self.controller.current_file = file_path
            self.controller.save()
            self.statusBar().showMessage("Tree saved as new file.", 3000)
            self.is_modified = False
            self.update_window_title()



    
    def load_tree(self):

        if self.is_modified:
            reply = QMessageBox.question(
                self,
                "Unsaved Changes",
                "You have unsaved changes. Continue without saving?",
                QMessageBox.Yes | QMessageBox.No
            )

            if reply == QMessageBox.No:
                return
            
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Load Tree",
            "",
            "JSON Files (*.json)"
        )
        self.update_window_title()

        


        if file_path:
            tree = self.controller.load_tree(file_path)
            self.is_modified = False
            self.update_window_title()


            if tree and tree.root:
                self.canvas.draw_tree(tree.root)
                self.statusBar().showMessage("Tree loaded successfully.", 3000)
            else:
                QMessageBox.warning(self, "Empty Tree", "Loaded file contains no nodes.")
    
    def select_traversal(self, traversal_type):
        if not self.controller.tree:
            QMessageBox.warning(self, "No Tree", "Create a tree first.")
            return

        self.selected_traversal = traversal_type

        self.start_btn.setEnabled(True)
        self.next_btn.setEnabled(False)
        self.reset_traversal_btn.setEnabled(False)

        self.statusBar().showMessage(
            f"{traversal_type.capitalize()} selected. Click Start.",
            3000
        )
    def prepare_traversal(self):
        if not hasattr(self, "selected_traversal"):
            return

        self.traversal_generator = self.controller.get_traversal_generator(
            self.selected_traversal
        )

        self.current_highlight = None
        self.visited_nodes = set()

        self.start_btn.setEnabled(False)
        self.next_btn.setEnabled(True)
        self.reset_traversal_btn.setEnabled(True)

        self.statusBar().showMessage("Click Next Step to proceed.", 3000)

    def next_step(self):
        if not self.traversal_generator:
            QMessageBox.information(self, "Info", "Click Start first.")
            return

        try:
            step = next(self.traversal_generator)
            print("RAW STEP:", step)

            if isinstance(step, tuple):
                step_type, value = step

                if step_type == "move":
                    self.current_highlight = value
                    self.explanation_label.setText(
                        f"Moving to node {value}."
                    )

                elif step_type == "visit":
                    self.current_highlight = value
                    self.visited_nodes.add(value)
                    self.explanation_label.setText(
                        f"Visiting node {value}. Added to traversal result."
                    )

                elif step_type == "return":
                    self.current_highlight = value
                    self.explanation_label.setText(
                        f"Returning from node {value}."
                    )


            elif isinstance(step, int):
                self.current_highlight = step
                self.visited_nodes.add(step)

            self.canvas.draw_tree(
                self.controller.tree.root,
                highlight=self.current_highlight,
                visited=self.visited_nodes
            )

        except StopIteration:
            QMessageBox.information(self, "Done", "Traversal completed.")
            self.traversal_generator = None


    
    def reset_traversal(self):
        self.traversal_generator = None
        self.current_highlight = None
        self.visited_nodes = set()

        if self.controller.tree:
            self.canvas.draw_tree(self.controller.tree.root)

        # Disable traversal control buttons
        self.start_btn.setEnabled(True)
        self.next_btn.setEnabled(False)
        self.reset_traversal_btn.setEnabled(False)
        self.explanation_label.setText("Traversal reset.")
        self.statusBar().showMessage("Traversal reset.", 3000)
    def update_window_title(self):
        base_title = "Binary Tree Visualizer v1.0"

        tree_name = ""
        file_name = ""

        if self.controller.tree and hasattr(self.controller.tree, "name"):
            tree_name = self.controller.tree.name

        if self.controller.current_file:
            import os
            file_name = os.path.basename(self.controller.current_file)

        title = base_title

        if tree_name:
            title += f" - {tree_name}"

        if file_name:
            title += f" [{file_name}]"

        if self.is_modified:
            title += " *"

        self.setWindowTitle(title)

    
    def rename_tree(self):
        if not self.controller.tree:
            QMessageBox.warning(self, "No Tree", "Create or load a tree first.")
            return

        new_name, ok = QInputDialog.getText(
            self,
            "Rename Tree",
            "Enter new tree name:"
        )

        if ok and new_name.strip():
            self.controller.tree.name = new_name.strip()
            self.is_modified = True
            self.update_window_title()
            self.statusBar().showMessage("Tree renamed.", 3000)
    def closeEvent(self, event):
        if self.is_modified:
            reply = QMessageBox.question(
                self,
                "Unsaved Changes",
                "You have unsaved changes. Exit anyway?",
                QMessageBox.Yes | QMessageBox.No
            )

            if reply == QMessageBox.No:
                event.ignore()
                return

        event.accept()


    





