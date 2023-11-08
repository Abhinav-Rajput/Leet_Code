class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []

        def helper(slate,A):
            if len(A)==0:
                return result.append(slate)
            else:
                for i in range(len(A)):
                    helper(slate+[A[i]],A[:i]+A[i+1:])
            # pass
        

        helper([],nums)

        return result



"""
        result = []

        def helper(A,i):
            #base case no sub-problem to solve
            if i==len(A):
                result.append(A[:])
            
            else:
                for pick in range(i,len(A)):
                    A[i],A[pick] = A[pick],A[i]
                    helper(A,i+1)
                    A[i],A[pick] = A[pick],A[i]
        helper(nums,0)

        return result

"""        

        