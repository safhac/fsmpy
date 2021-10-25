from enum import Enum, auto


class Msg(Enum):
    Listen = auto()
    Process = auto()
    Send = auto()
    Failure = auto()



