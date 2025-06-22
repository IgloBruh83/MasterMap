from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from Config import Config as cfg

class MainViewport (QGraphicsView):
    def __init__(self, scene):
        super().__init__(scene)
        self.setRenderHints(self.renderHints())
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setStyleSheet("QGraphicsView { border: none; }")
        self.setFixedSize(int(cfg.viewportDims[0]/cfg.dpi), int(cfg.viewportDims[1]/cfg.dpi))
        self.setViewportUpdateMode(QGraphicsView.ViewportUpdateMode.FullViewportUpdate)