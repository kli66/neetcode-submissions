"""
state of another 3 minutes
consulted 
"""

OPEN_SYM = {'(', '[', '{'}
CLOSE_SYM = {')', ']', '}'}
MAPPING = {'(': ')', '[': "]", '{':'}'}

from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        comp = deque()

        for curr in s:
            print(curr)
            if curr in OPEN_SYM:
                comp.append(MAPPING[curr])
            else:
                if not comp:
                    return False
                if curr != comp.pop():
                    return False
                else:
                    continue
        return len(comp) == 0
