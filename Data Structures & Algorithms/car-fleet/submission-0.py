class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed),reverse = True)
        maxTime = 0
        fleet = 0
        for p,s in pairs:
            time = (target - p)/s   
            if time > maxTime:
                fleet += 1
                maxTime = time
        return fleet



        