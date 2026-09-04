class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for i in range(len(nums)):
            map[nums[i]] = map.get(nums[i], 0) + 1
            value = map.get(nums[i])
            if value > 1:
                return True
        return False
        