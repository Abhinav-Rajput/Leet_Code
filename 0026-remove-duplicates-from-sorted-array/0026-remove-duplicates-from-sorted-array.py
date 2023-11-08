class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j
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
        