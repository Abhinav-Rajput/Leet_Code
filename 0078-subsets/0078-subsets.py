class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result =[]
        def helper(s, i, slate):

            if i==len(s):
                result.append(slate)
                return
            else:
                # slate.append(s[i])
                helper(s,i+1,slate)
                # slate.pop(s[i])
                helper(s,i+1,slate+[s[i]])

        

        helper(nums,0,[])

        return result







































        """
        
        if nums == []:
            return [[]]

        first = nums[0]
        rest = nums[1:]

        subsets_without_first = self.subsets(rest)
        subsets_with_first = []

        for subset in subsets_without_first:
            subset_with_first = subset.copy()
            subset_with_first.append(first)
            subsets_with_first.append(subset_with_first)

        return subsets_without_first + subsets_with_first
        """

        
        