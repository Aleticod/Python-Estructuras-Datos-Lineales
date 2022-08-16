

from __future__ import annotations
from typing import Any

class Node():
    def __init__(self, data: Any, next: Node = None) -> None:
        self.data = data
        self.next = next


class TwoWayNode(Node):
    def __init__(self, data: Any, previous: Node =None, next: Node = None) -> None:
        super().__init__(data, next)
        self.previous = previous