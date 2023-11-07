class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        # result =[]

        # def helper(s,i, slate ):
        #     if i == len(s):
        #         result.append(slate)
        #     else:
        #         if s[i].isdigit():
        #             helper(s,i+1,slate+s[i])
        #         else:
        #             helper(s,i+1,slate+s[i].upper())
        #             helper(s,i+1,slate+s[i].lower())
        
        # helper(s,0,"")

        # return result

        # above solution is  with immutable parameter

        # following solution with mutable parameter

        result=[]

        def mutableHelper(s,i,slate):
            if i== len(s):
                result.append("".join(slate))
                return
            else:
                if s[i].isdigit():
                    slate.append(s[i])
                    mutableHelper(s,i+1, slate)
                    slate.pop()
                else:
                    slate.append(s[i].lower())
                    mutableHelper(s,i+1,slate)
                    slate.pop()

                    slate.append(s[i].upper())
                    mutableHelper(s,i+1,slate)
                    slate.pop()

        mutableHelper(s,0,[])

        return result