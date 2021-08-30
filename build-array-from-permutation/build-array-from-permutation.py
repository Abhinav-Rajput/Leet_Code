class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(0,len(nums)):
            t=nums[nums[i]]
            ans.append(t)
        return ans
        