class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_map = {}
        for i in range(len(s)):
            my_map[s[i]] = my_map.get(s[i], 0) + 1

        for i in range(len(t)):
            my_map[t[i]] = my_map.get(t[i], 0) - 1
        
        for count in my_map.values():
            if count !=0:
                return False
        return True


            
        