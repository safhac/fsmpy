from dataclasses import dataclass
from enum import Enum, auto


class Msg(Enum):
    Listen = auto()
    Process = auto()
    Send = auto()
    Failure = auto()


@dataclass(frozen=True)
class Model:
    state: str
    data: str
