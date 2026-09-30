from PySide6.QtWidgets import QGraphicsView, QGraphicsScene
from PySide6.QtGui import QPainterPath, QPen, QPainter
from PySide6.QtCore import Qt

class Whiteboard(QGraphicsView):
    def __init__(self):
        super().__init__()

        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        self.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.setStyleSheet("background-color: #f5f5f5; border: none;")

        self.scene.setSceneRect(0,0,5000,5000)

        self.drawing = False
        self.current_path = None
        self.current_path_item = None

        self.pen = QPen(Qt.GlobalColor.black, 3, Qt.PenStyle.SolidLine,
                        Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing = True 
            self.current_path = QPainterPath()

            scene_pos = self.mapToScene(event.position().toPoint())
            self.current_path.moveTo(scene_pos)

            self.current_path_item = self.scene.addPath(self.current_path, self.pen)

        super().mousePressEvent(event)

    def mouseMoveEvent(self,event):
        if self.drawing and self.current_path_item:
            scene_pos = self.mapToScene(event.position().toPoint())

            self.current_path.lineTo(scene_pos)

            self.current_path_item.setPath(self.current_path)

        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing = False
            self.current_path = None
            self.current_path_item = None
        
        super().mouseReleaseEvent(event)

