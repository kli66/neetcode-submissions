from collections import deque

class MinStack:

    def __init__(self):
        self._data = list()
        self._curr_min: list[int] = list()

    def push(self, val: int) -> None:
        self._data.append(val)
        self._curr_min.append(min(val, self._curr_min[-1]) if self._curr_min else val)

    def pop(self) -> None:
        # need to update _curr_min
        value = self._data.pop()
        self._curr_min.pop()

    def top(self) -> int:
        if not self._data:
            raise ValueError
        else:
            return self._data[-1]

    def getMin(self) -> int:
        if not self._curr_min:
            raise ValueError
        else:
            return self._curr_min[-1]
