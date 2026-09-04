class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        list = []
        count = 1
        nums.sort()
        if len(nums)==0:
            return 0
        
        for i in range(len(nums)):
            if i == 0:
                previousn = nums[i]
                continue
            if nums[i]==previousn:
                continue
            if (previousn +1) == nums[i]:
                count += 1
                previousn=nums[i]
            else:
                list.append(count)
                count = 1
                previousn = nums[i]
        list.append(count)

        return max(list)
    