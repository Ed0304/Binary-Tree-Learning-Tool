from PySide6.QtWidgets import QGraphicsView, QGraphicsScene
from PySide6.QtGui import QPen, QBrush
from PySide6.QtCore import Qt

class TreeCanvas(QGraphicsView):
    def __init__(self):
        super().__init__()

        self.scene = QGraphicsScene()
        self.setScene(self.scene)

    def draw_tree(self, root, highlight=None, visited=None):
        self.scene.clear()

        if root is None:
            return

        self._draw_node(root, 450, 60, 200, highlight, visited)

    def _draw_node(self, node, x, y, spacing, highlight=None, visited=None):
        radius = 20

        color = Qt.white

        if highlight == node.value:
            color = Qt.red
        elif visited and node.value in visited:
            color = Qt.green

        # Draw node circle
        self.scene.addEllipse(
            x - radius,
            y - radius,
            radius * 2,
            radius * 2,
            QPen(Qt.black),
            QBrush(color)
        )

        # Draw node value
        text = self.scene.addText(str(node.value))
        text.setDefaultTextColor(Qt.black)
        text.setPos(
            x - text.boundingRect().width() / 2,
            y - text.boundingRect().height() / 2
        )

        # LEFT
        if node.left:
            new_x = x - spacing
            new_y = y + 100

            self.scene.addLine(
                x, y + radius,
                new_x, new_y - radius
            )

            self._draw_node(
                node.left,
                new_x,
                new_y,
                spacing / 2,
                highlight,
                visited
            )

        # RIGHT
        if node.right:
            new_x = x + spacing
            new_y = y + 100

            self.scene.addLine(
                x, y + radius,
                new_x, new_y - radius
            )

            self._draw_node(
                node.right,
                new_x,
                new_y,
                spacing / 2,
                highlight,
                visited
            )
