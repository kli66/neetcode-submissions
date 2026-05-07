class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        obs_window = set()
        l = 0

        result = 0
        for r in range(len(s)):
            while s[r] in obs_window:
                obs_window.remove(s[l])
                l += 1
            
            obs_window.add(s[r])
            result = max(result, r - l +1)
        return result