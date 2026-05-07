class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lookup_tbl = dict()
        result = 0

        l = 0

        for r in range(len(s)):
            lookup_tbl[s[r]] = 1 + lookup_tbl.get(s[r], 0)

            if (r-l+1) - max(lookup_tbl.values()) > k: 
                lookup_tbl[s[l]] -= 1
                l += 1
            
            result = max(result, r-l+1)

        return result