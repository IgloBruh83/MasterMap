import json
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from Config import Config as cfg

class Unit (QGraphicsPixmapItem):
    def __init__(self, unit_id, database):
        super().__init__()

        # VALIDATION
        try:
            with open(database+".json", "r") as f:
                data = json.load(f)[unit_id]
        except FileNotFoundError:
            print("ERROR: Given database does not exist"); return
        except KeyError:
            print("ERROR: Given unit id was not found in this database"); return
        except json.decoder.JSONDecodeError:
            print("ERROR: JSON parsing failed"); return

        # DATA
        self.name = data["name"]
        self.fraction = data["fraction"]
        self.maxhp = data["maxhp"]
        self.initbonus = data["initBonus"]
        self.armorClass = data["armorClass"]

        # GRAPHICS
        self.setPixmap(QPixmap(f"UnitGraphics/{unit_id}.png"))

        # FLAGS
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable, True)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable, True)


