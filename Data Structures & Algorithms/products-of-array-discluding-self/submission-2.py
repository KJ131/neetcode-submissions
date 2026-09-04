class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        newl = []
        newr = []
        flist = []
        for i in range(len(nums)):
            if i == 0:
                newl.append(1)
                continue
            newl.append(newl[i-1] * nums[i-1])

        for i in range(len(nums),0,-1):

            if i == len(nums):
                newr.append(1)
                continue
            newr.append(newr[-1] * nums[i])
        newr.reverse()

        for i in range(len(nums)):
            flist.append(newr[i] * newl[i])
        return flist

           



        