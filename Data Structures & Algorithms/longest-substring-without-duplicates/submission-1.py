from itertools import permutations

class Solution:

    
    def lengthOfLongestSubstring(self, s: str) -> int:
        # brute force


        result = 0 
        for l in range(len(s)):
            r = l + 1
            curr_result = 1
            while r <= len(s) - 1:
                curr_substr = s[l:r+1]
                if len(set(curr_substr)) < len(curr_substr):
                    break
                else:
                    curr_result += 1
                    r += 1
            result = max(curr_result, result)

        return result

