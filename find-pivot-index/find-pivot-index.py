class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if nums == None:
            return -1
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return -1
        leftSum,rightSum=0,0
        for i in range(0,len(nums)):
            leftSum = sum(nums[0:i])
            rightSum = sum(nums[i+1:])
            if leftSum==rightSum:
                return i
        return -1
            
            