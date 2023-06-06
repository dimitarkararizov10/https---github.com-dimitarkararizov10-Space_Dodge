from enum import Enum

class GameState(Enum):
    MENU = 1
    PLAYING = 2
    TRANSITION = 3
    LEVEL_COMPLETED = 4
    LEVEL_STATE = 5
    DEAD = 6
    LOCKER = 7