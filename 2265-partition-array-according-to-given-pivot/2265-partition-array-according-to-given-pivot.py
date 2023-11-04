class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        """
        1. Every element less than pivot appears before every element greater
        than pivot
        2.Every element equals to pivot appears in between the elements less than and greater than pivot
        3. The relative order of the elements less than pivot and the elements greater than pivot is maintained
        4

        nums = [9,12,5,10,14,3,10], pivot =10

        Key things to notice before approaching the problem:
        1.The problem asks us to rearrange an array such that every element less than the pivot appears before every element greater than the pivot, and every element equal to the pivot appears in between.
        2.The problem also asks us to maintain the relative order of the elements less than and greater than the pivot.


        How to approach pivot questions using two-pointers:

        How to get the "two-pointers" intuition for the above problem:

        The intuition behind the two-pointer approach for this problem is to use the two pointers to partition the array into three parts:
            1.Elements less than the pivot
            2.Elements equal to the pivot
            3.Elements greater than the pivot




        """
        less_than_pivot = []
        equal_to_pivot = []
        greater_than_pivot = []

        for num in nums:
            if num < pivot:
                less_than_pivot.append(num)
            elif num > pivot:
                greater_than_pivot.append(num)
            else:
                equal_to_pivot.append(num)

        return less_than_pivot + equal_to_pivot + greater_than_pivot

        # l =0
        # r=len(nums)-1
        # i=0
        # while i<=r:
        #     if nums[i]<pivot:
        #         nums[i],nums[l]=nums[l],nums[i]
        #         l+=1
        #         i+=1
        #     elif nums[i]>pivot:
        #         nums[i],nums[r] = nums[r],nums[i]
        #         r-=1

        #     else:
        #         i=i+1

        # return nums


        
        