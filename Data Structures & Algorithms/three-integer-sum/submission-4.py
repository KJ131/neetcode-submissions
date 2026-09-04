class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        list =[]
        for i in range(len(nums)):
            right = len(nums)-1
            left = i + 1
            while left<right:
                if i>=1 and nums[i] == nums[i-1]:
                    break
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    list.append([nums[i],nums[left],nums[right]])
                    left +=1
                    right -= 1
                    while left < right and nums[left-1] == nums[left]:
                        left += 1
                    while left < right and nums[right+1] == nums[right]:
                        right -= 1
                elif total > 0:
                    right-=1
                elif total < 0:
                    left+=1
                
        return list