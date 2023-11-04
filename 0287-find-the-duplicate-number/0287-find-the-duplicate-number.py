class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        track=dict()

        for i in nums:
            if i in track:
                return i
            else:
                track[i]=1
            
        