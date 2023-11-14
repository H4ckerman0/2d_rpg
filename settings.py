import os, sys

if getattr(sys, 'frozen', False):
    GAME_PATH = os.path.dirname(sys.executable)
elif __file__:
    GAME_PATH = os.path.dirname(__file__)

WIDTH = 1280
HEIGHT = 720
FPS = 60
TILESIZE = 64

HEALTH_BAR_WIDTH = 300
STAMINA_BAR_WIDTH = 300
BAR_HEIGHT = 20
WEAPON_BOX_SIZE = 70
UI_FONT = GAME_PATH + r"\font\slkscr.ttf"
UI_FONT_SIZE = 50

HEALTH_BAR_COLOR = "red"
STAMINA_BAR_COLOR = "darkgreen"
BG_BAR_COLOR = "#333333"
EXP_TEXT_COLOR = "#00929d"
BORDER_COLOR = "black"
BORDER_COLOR_ACTIVE = "darkgrey"



weapon_data = {

    "spear": {"graphic": GAME_PATH + r"\graphics\weapon\spear\up.png"},
    "axe": {"graphic": GAME_PATH + r"\graphics\weapon\axe\up.png"},
    "sickle": {"graphic": GAME_PATH + r"\graphics\weapon\sickle\up.png"}

}

magic_data = {

    "heal": {"impact": 20, "cost": 30, "graphic": GAME_PATH + r"\graphics\particles\heal\heal.png"},
    "flame": {"impact": 40, "cost": 60,"graphic": GAME_PATH + r"\graphics\particles\flame\flame.png"}

}