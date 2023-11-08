class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<2:
            return len(nums)
        l=0
        for i in range(len(nums)):
            if nums[i]==nums[l]:
                i+=1
            else:
                nums[l+1]=nums[i]
                l+=1
                i+=1
        return l+1
        