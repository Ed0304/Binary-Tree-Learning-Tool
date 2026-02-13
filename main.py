from tree.binary_tree import Tree
from ui.cli_menu import run_cli
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow
import sys
from ui import * 
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()