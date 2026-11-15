class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        specials = {
            "+": lambda: record.append(record[-1] + record[-2]),
            "D": lambda: record.append(2*record[-1]), 
            "C": lambda: record.pop()
        }

        for opr in operations: 
            if opr in specials:
                specials[opr]()
            else:
                record.append(int(opr))
        return sum(record)