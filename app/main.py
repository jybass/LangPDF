import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QSplitter, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton)

from components.pdf_viewer import PdfViewer

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
        
        #Splitter config
        self.splitter = QSplitter(Qt.Horizontal)
        self.splitter.setHandleWidth(0.2)


        self.pdf_panel = PdfViewer("0661217151.pdf")
        self.canvas_panel = Whiteboard()

        toolbar_layout = QHBoxLayout()
        toolbar_layout.setContentsMargins(10, 10, 10, 10)

        btn_fit = QPushButton("Ajustar à Tela")
        btn_zoom_out = QPushButton("Zoom -")
        btn_zoom_in = QPushButton("Zoom +")

        button_style = "padding: 5px; font-weight: bold; background-color:#444; color: white; border-radius: 4px;"
        btn_fit.setStyleSheet(button_style)
        btn_zoom_out.setStyleSheet(button_style)
        btn_zoom_in.setStyleSheet(button_style)

        btn_fit.clicked.connect(self.pdf_panel.reset_zoom)
        btn_zoom_out.clicked.connect(self.pdf_panel.zoom_out)
        btn_zoom_in.clicked.connect(self.pdf_panel.zoom_in)

        toolbar_layout.addWidget(btn_fit)
        toolbar_layout.addWidget(btn_zoom_out)
        toolbar_layout.addWidget(btn_zoom_in)
        toolbar_layout.addStretch()

        left_panel = QWidget()
        left_panel.setStyleSheet("background-color: #2d2d2d;")
        left_layout = QVBoxLayout(left_panel)
        left_layout.setContentsMargins(0,0,0,0)
        left_layout.addLayout(toolbar_layout)
        left_layout.addWidget(self.pdf_panel)


        self.splitter.addWidget(left_panel)
        self.splitter.addWidget(self.canvas_panel)

        self.splitter.setSizes([500,700])


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
        

