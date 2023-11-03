class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l=0
        for r in range(len(nums)):
            if nums[r]!=0:
                nums[l],nums[r]=nums[r],nums[l]
                l=l+1
        
        # following pseudo-code is wrong
        # psuedo-code
        # we can have 2 pointers, l starting from left-end
        # and r starting from right end

        # whenever we l encounters 0, switch it with non-zero
        #  right pointer elemnt

        #  if the current element at right pointer does not have non-zero

        #  elemt decrement it by 1 and swap it with element at l

        # r=len(nums)-1
        # l=0
        # while l<len(nums) :
        #     if l<len(nums) and nums[l]==0:
        #         while r>=l and nums[r]!=0:
        #             r=r-1
        #         nums[l],nums[r]=nums[r],nums[l]
        #     l=l+1
        



        