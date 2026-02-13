from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout,
    QPushButton, QHBoxLayout
)
from PySide6.QtWidgets import (
    QLineEdit, QLabel
)

from ui.tree_canvas import TreeCanvas
from ui.tree_controller import TreeController

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Binary Tree Visualizer v1.0")
        self.resize(900, 600)
        self.controller = TreeController()

        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout()
        central.setLayout(layout)

        # Button row
        button_layout = QHBoxLayout()
        self.preorder_btn = QPushButton("Preorder")
        self.inorder_btn = QPushButton("Inorder")
        self.postorder_btn = QPushButton("Postorder")

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

        self.insert_btn = QPushButton("Insert")
        self.delete_btn = QPushButton("Delete")
        self.create_btn = QPushButton("Create Tree")
        self.reset_btn = QPushButton("Reset")

        self.insert_btn.clicked.connect(self.insert_node)
        self.delete_btn.clicked.connect(self.delete_node)
        self.create_btn.clicked.connect(self.create_tree)
        self.reset_btn.clicked.connect(self.reset_tree)

        tree_controls.addWidget(self.value_input)
        tree_controls.addWidget(self.insert_btn)
        tree_controls.addWidget(self.delete_btn)
        tree_controls.addWidget(self.create_btn)
        tree_controls.addWidget(self.reset_btn)

        layout.addLayout(tree_controls)
    
    def create_tree(self):
        text = self.value_input.text()
        if not text:
            return

        try:
            value = int(text)
            self.controller.create_tree(value, "GUI Tree")
            self.canvas.draw_tree(self.controller.tree.root)
        except ValueError:
            pass
    
    def insert_node(self):
        text = self.value_input.text()
        if not text:
            return

        try:
            value = int(text)
            success = self.controller.insert(value)
            if success:
                self.canvas.draw_tree(self.controller.tree.root)
        except ValueError:
            pass
    
    def delete_node(self):
        text = self.value_input.text()
        if not text:
            return

        try:
            value = int(text)
            success = self.controller.delete(value)
            if success:
                self.canvas.draw_tree(self.controller.tree.root)
        except ValueError:
            pass

    def reset_tree(self):
        self.controller.tree = None
        self.canvas.scene.clear()





