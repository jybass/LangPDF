import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QSplitter, QWidget, QVBoxLayout, QLabel)

from pdf_viewer import PdfViewer

class Whiteboard(QWidget):
    def __init__(self):
            super().__init__()
    
            layout = QVBoxLayout()

            label = QLabel("Whiteboard")
            label.setAlignment(Qt.AlignCenter)

            self.setStyleSheet("background-color: #1e1e1e; color: a0a0a0; font-size: 18px;")
            layout.addWidget(label)
            self.setLayout(layout)

            
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("LangPDF")
        self.resize(1200,800)

        self.splitter = QSplitter(Qt.Horizontal)

        self.pdf_panel = PdfViewer("sample.pdf")
        self.canvas_panel = Whiteboard()

        self.splitter.addWidget(self.pdf_panel)
        self.splitter.addWidget(self.canvas_panel)

        self.splitter.setStretchFactor(0,1)
        self.splitter.setStretchFactor(1,2)

        self.splitter.setStyleSheet("""
            QSplitter:: handle {
                background-color: #3f3f3f;
                width: 4px;
            }
            QSplitter:: handle:houver {
                background-color: #0078D7;    
            }
        """)

        self.setCentralWidget(self.splitter)

if __name__ == "__main__":

    app = QApplication(sys.argv)

    w = MainWindow()
    w.show()

    sys.exit(app.exec())    
        

