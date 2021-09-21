class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dicts= dict()
        for i in nums:
            if i in dicts:
                if dicts[i]>1:
                    return True
                else:
                    dicts[i]=2 
                    return True
            else:
                dicts[i]=1
        return False
        