from enum import Enum

class GameState(Enum):
    MENU = 1
    PLAYING = 2
    TRANSITION = 3
    LEVEL_COMPLETED = 4
    NEXT_LEVEL = 5