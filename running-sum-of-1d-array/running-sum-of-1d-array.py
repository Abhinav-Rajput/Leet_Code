class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum1=0
        ans=[]
        for i in range(0,len(nums)):
            sum1=sum1+nums[i]
            ans.append(sum1)
        return ans
        