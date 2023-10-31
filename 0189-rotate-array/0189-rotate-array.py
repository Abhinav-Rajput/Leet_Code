class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        1. no return , In-place modifications
        2. rotate to right by k steps, k is NON-negative
        3. 
        """
        # nums=nums[::-1]
        k=k%len(nums)
        l=0
        r = len(nums)-1

        def rev(arr,l,r):
            while l<r:
                arr[l],arr[r] =arr[r],arr[l]
                l=l+1
                r=r-1
            return arr
        l=0
        r = len(nums)-1
        nums=rev(nums,l,r)

        l=0
        r=k-1
        nums=rev(nums,l,r)

        l=k
        r=len(nums)-1
        nums=rev(nums,l,r)

    

        

        

        
        # nums1=nums
        # for i in range(k):
        #     k=nums1.pop()
        #     print(k)
        #     print(nums1)
        #     nums1=[k]+nums1
        # nums=nums1


        
        