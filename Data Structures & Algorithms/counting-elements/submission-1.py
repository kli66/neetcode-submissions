

class Solution:
    def countElements(self, arr: List[int]) -> int:
        deduped = set(arr)
        plus_1 = list(map(lambda x: x+1, arr))
        
        # res = 0
        # for _ in plus_1:
        #     if _ in deduped:
        #         res += 1
        
        # return res
        
        return sum(list(map(lambda x: int(x in deduped), plus_1)))