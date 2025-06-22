
# ----- DEV IMPORTS -----
import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

# ----- MODULES IMPORTS -----
from Config import Config as cfg
from Overrides.Viewport import MainViewport
from Overrides.World import WorldScene
from Models.Unit import Unit


# ----- CONFIG -----
app = QApplication(sys.argv)
cfg.dpi = QGuiApplication.primaryScreen().devicePixelRatio()


# ----- MAIN WINDOW -----
window = QMainWindow()
window.setWindowTitle("Master Map -- DnD")
(window.setWindowFlags
(Qt.WindowType.FramelessWindowHint & ~Qt.WindowType.WindowStaysOnTopHint))
window.setStyleSheet(""" QMainWindow {
        border-image: url(bg.png) repeat;
    } """)
window.showFullScreen()


# ----- WORLD SCENE -----
world = WorldScene()
world.changebg("Map.png", [300, 200])

# ----- MAIN VIEWPORT -----
view = MainViewport(world)
view.resetTransform()
view.scale(4.16, 4.16)


# ----- MAINLOOP -----
window.setCentralWidget(view)
sys.exit(app.exec())