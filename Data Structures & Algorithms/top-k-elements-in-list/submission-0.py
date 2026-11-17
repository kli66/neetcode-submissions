from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        # struggled wondered if there is alt methods for better format

        return [tmp[0] for tmp in cnt.most_common(k)]