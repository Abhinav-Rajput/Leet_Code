class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        result =[]

        def helper(s,i, slate ):
            if i == len(s):
                result.append(slate)
            else:
                if s[i].isdigit():
                    helper(s,i+1,slate+s[i])
                else:
                    helper(s,i+1,slate+s[i].upper())
                    helper(s,i+1,slate+s[i].lower())
        
        helper(s,0,"")

        return result
        