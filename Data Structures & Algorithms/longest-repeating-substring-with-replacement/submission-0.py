class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxCount = 0 
        hashmap = {}
        l = 0
        length = 0 
        for r in range(len(s)):
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1
            maxCount = max(maxCount, hashmap[s[r]])
            while r - l + 1 - maxCount >k:
                hashmap[s[l]] = hashmap.get(s[l]) - 1
                l += 1
            length = max(length, r - l + 1)
        return length
            




