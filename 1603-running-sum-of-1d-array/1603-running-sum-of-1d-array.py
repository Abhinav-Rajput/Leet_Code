class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        sum1=0
        for i in range(len(nums)):
            sum1+=nums[i]
            res.append(sum1)
        return res