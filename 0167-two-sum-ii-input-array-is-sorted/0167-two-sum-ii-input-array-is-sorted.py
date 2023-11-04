class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        """
        1. Given input array is sorted
        2. we have to return the indices of elements whose sum is equal to target
        3. we can use 2-pointer approach , since array is sorted.
        4. we'll have 2 pointer left, and right starting from opposite ends of the array
        
        """

        l,r=0,len(numbers)-1

        while l<r:
            if numbers[l]+numbers[r]<target:
                l=l+1
            elif numbers[l]+numbers[r]>target:
                r=r-1
            else:
                return [l+1,r+1]
        
        