from PySide6.QtCore import QPointF
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from Config import Config as cfg
from Models.Grid import Grid

class WorldScene (QGraphicsScene):

    def __init__(self):
        super().__init__()
        self.setSceneRect(0, 0, 300, 200)
        self.setBackgroundBrush(QColor("#D0D0D0"))

        self.bg = QGraphicsPixmapItem()
        self.bg.setZValue(cfg.zBackground)
        self.addItem(self.bg)

        self.grid = Grid()
        self.addItem(self.grid)

        self.rulerLine = None
        self.rulerText = None
        self.rulerStart = None

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.RightButton:
            self.rulerStart = event.scenePos()
            self.rulerLine = QGraphicsLineItem()
            self.rulerLine.setPen(QPen(QColor("darkgrey"), 0.6))
            self.addItem(self.rulerLine)
            self.rulerText = QGraphicsSimpleTextItem()
            self.rulerText.setBrush(QColor("red"))
            font = QFont("Arial", 20)
            font.setBold(True)
            self.rulerText.setFont(font)
            self.rulerText.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIgnoresTransformations)
            self.addItem(self.rulerText)
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.rulerLine and self.rulerStart:
            end_pos = event.scenePos()
            self.rulerLine.setLine(self.rulerStart.x(), self.rulerStart.y(),
                                    end_pos.x(), end_pos.y())

            # Відстань у метрах
            delta = self.rulerStart - end_pos
            distance = ((delta.x() ** 2 + delta.y() ** 2) ** 0.5)/10
            self.rulerText.setText(f"{distance:.1f} / 18 m")
            self.rulerText.setPos(end_pos + QPointF(2, 2))

        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.RightButton:
            if self.rulerLine:
                self.removeItem(self.rulerLine)
                self.rulerLine = None
            if self.rulerText:
                self.removeItem(self.rulerText)
                self.rulerText = None
            self.rulerStart = None
        else:
            super().mouseReleaseEvent(event)


    def changebg(self, path, dims):
        _pixmap = QPixmap(path)
        self.bg.setPixmap(_pixmap)
        self.setSceneRect(0, 0, dims[0], dims[1])
        scale_x = dims[0] / _pixmap.width()
        scale_y = dims[1] / _pixmap.height()
        self.bg.setScale(min(scale_x, scale_y))
