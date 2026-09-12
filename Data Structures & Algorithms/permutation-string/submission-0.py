class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        maps1 = {}
        maps2 = {}
        l = 0
        window_max = len(s1)
        for i in range(len(s1)):
            maps1[s1[i]] = maps1.get(s1[i],0) + 1
        for right in range(len(s2)):
            maps2[s2[right]] = maps2.get(s2[right],0) + 1
            if right - l + 1 == window_max:
                if maps1 == maps2:
                    return True
                else:
                    maps2[s2[l]] = maps2.get(s2[l]) - 1
                    if maps2.get(s2[l]) == 0:
                        maps2.pop(s2[l])
                    l += 1
        return False
                    
