from collections import deque



class Solution:
    def isValid(self, s: str) -> bool:
        match = {"(":")", "[":"]", "{":"}"}
        expected = deque()
        for c in s:
            if c in match.keys():
                expected.append(match[c])
            else:
                if not expected:
                    return False
                elif expected.pop() != c:
                    return False
        if len(expected) > 0:
            return False

        return True
