import pymupdf as fitz
from PySide6.QtWidgets import QScrollArea, QWidget, QVBoxLayout, QLabel
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt, QRect

class PdfViewer(QScrollArea):
    def __init__(self, pdf_path):
        super().__init__()
        self.setWidgetResizable(True)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet("background-color: #2d2d2d;")

        self.doc = fitz.open(pdf_path)
        self.zoom = 1.5
        self.page_labels = []
        self.rendered_pages = set()

        self.container = QWidget()
        self.container.setStyleSheet("background-color: transparent;")

        self.layout = QVBoxLayout(self.container)
        self.layout.setSpacing(15)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self._setup_pages()
        self.setWidget(self.container)

        self.verticalScrollBar().valueChanged.connect(self.check_visible_pages)

    def _setup_pages(self):
        for i in range(len(self.doc)):
            page = self.doc[i]

            rect = page.rect
            width = int(rect.width * self.zoom)
            height = int(rect.height * self.zoom)

            label = QLabel()
            label.setFixedSize(width, height)
            label.setStyleSheet("background-color: white;")

            self.layout.addWidget(label)
            self.page_labels.append(label)

    def check_visible_pages(self):
        visible_rect = self.widget().visibleRegion().boundingRect()

        margin = 1500
        render_zone = QRect(0, visible_rect.top() - margin, self.width(), visible_rect.height()+ (margin * 2))

        for i, label in enumerate(self.page_labels):
            if render_zone.intersects(label.geometry()):
                if i not in self.rendered_pages:
                    self._render_page(i)
            else:
                if i in self.rendered_pages:
                    self._unload_page(i)

    def _render_page(self, page_index):
        page = self.doc[page_index]
        mat = fitz.Matrix(self.zoom, self.zoom)
        pix = page.get_pixmap(matrix=mat)

        img = QImage(pix.samples,pix.width, pix.height, pix.stride, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(img)

        self.page_labels[page_index].setPixmap(pixmap)
        self.rendered_pages.add(page_index)

    def _unload_page(self, page_index):
        self.page_labels[page_index].clear()
        self.rendered_pages.remove(page_index)

    def showEvent(self, event):
        super().showEvent(event)
        self.check_visible_pages()
       

