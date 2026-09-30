import sys
import os
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QSplitter, 
                               QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
                               QGraphicsDropShadowEffect)
from PySide6.QtGui import QFont, QColor

from components.pdf_viewer import PdfViewer
from components.whiteboard import Whiteboard

            
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LangPDF")
        self.resize(1300, 850)

        app_font = QFont("Segoe UI", 10) 
        QApplication.setFont(app_font)

                
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(20, 20, 20, 20) 

        splitter = QSplitter(Qt.Orientation.Horizontal)

                
        left_panel = QWidget()
        left_panel.setObjectName("CardWidget") 
        self.apply_shadow(left_panel) 

        left_layout = QVBoxLayout(left_panel)
        left_layout.setContentsMargins(10, 10, 10, 10)

                
        toolbar_layout = QHBoxLayout()
        btn_fit = QPushButton("Ajustar")
        btn_zoom_out = QPushButton("Zoom -")
        btn_zoom_in = QPushButton("Zoom +")

        self.pdf_viewer = PdfViewer("0661217151.pdf") 

        btn_fit.clicked.connect(self.pdf_viewer.reset_zoom)
        btn_zoom_out.clicked.connect(self.pdf_viewer.zoom_out)
        btn_zoom_in.clicked.connect(self.pdf_viewer.zoom_in)

        toolbar_layout.addWidget(btn_fit)
        toolbar_layout.addWidget(btn_zoom_out)
        toolbar_layout.addWidget(btn_zoom_in)
        toolbar_layout.addStretch()

        left_layout.addLayout(toolbar_layout)
        left_layout.addWidget(self.pdf_viewer)

        right_panel = QWidget()
        right_panel.setObjectName("CardWidget") 
        self.apply_shadow(right_panel) 

        right_layout = QVBoxLayout(right_panel)
        right_layout.setContentsMargins(10, 10, 10, 10)
                
        self.whiteboard = Whiteboard()
        self.whiteboard.setStyleSheet("background: transparent; border: none;")
                
        right_layout.addWidget(self.whiteboard)

        
        splitter.addWidget(left_panel)
        splitter.addWidget(right_panel)
        splitter.setSizes([500, 750])

        main_layout.addWidget(splitter)

    def apply_shadow(self, widget):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(20) 
        shadow.setColor(QColor(0, 0, 0, 15)) 
        shadow.setOffset(0, 4) 
        widget.setGraphicsEffect(shadow)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)

    pasta_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_qss = os.path.join(pasta_atual, "style.qss")

    try:
        with open(caminho_qss, "r", encoding="utf-8") as f:
            app.setStyleSheet(f.read())
    except FileNotFoundError:
        print("No QSS File")
    
    w = MainWindow()
    w.show()
    sys.exit(app.exec())    
        

