class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # tracker = dict()

        # for i in range(len(nums)):
        #     if nums[i] in  tracker and tracker[nums[i]] >= 2:
        #         continue
        #     elif nums[i] in  tracker and tracker[nums[i]]==1:
        #         tracker[nums[i]]+=1
        #     else:
        #         tracker[nums[i]]=1
        # total=0
        # for i in tracker.values():
        #     total+=i
        
        # return total
        i = 1
        while i < len(nums) - 1:
            if nums[i] == nums[i - 1] and nums[i] == nums[i + 1]:
                del nums[i]
            else:
                i += 1
        return len(nums)


        