from PySide6.QtWidgets import QGraphicsView, QGraphicsScene
from PySide6.QtGui import QPen, QBrush
from PySide6.QtCore import Qt

class TreeCanvas(QGraphicsView):
    def __init__(self):
        super().__init__()

        self.scene = QGraphicsScene()
        self.setScene(self.scene)

    def draw_tree(self, root):
        self.scene.clear()

        if root is None:
            return

        self._draw_node(root, x=450, y=60, spacing=200)

    def _draw_node(self, node, x, y, spacing):
        radius = 20

        # Draw node circle
        circle = self.scene.addEllipse(
            x - radius,
            y - radius,
            radius * 2,
            radius * 2,
            QPen(Qt.black),
            QBrush(Qt.white)
        )

        # Draw node value
        text = self.scene.addText(str(node.value))
        text.setDefaultTextColor(Qt.black)
        text.setPos(x - text.boundingRect().width() / 2,
            y - text.boundingRect().height() / 2)

        # Draw left subtree
        if node.left:
            new_x = x - spacing
            new_y = y + 100
            self.scene.addLine(x, y, new_x, new_y)
            self._draw_node(node.left, new_x, new_y, spacing / 2)

        # Draw right subtree
        if node.right:
            new_x = x + spacing
            new_y = y + 100
            self.scene.addLine(x, y, new_x, new_y)
            self._draw_node(node.right, new_x, new_y, spacing / 2)
