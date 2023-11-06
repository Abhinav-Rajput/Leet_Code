class Solution:
    def reverseOnlyLetters(self, s: str) -> str:

        s_list=list(s)
        l, r = 0 , len(s)-1

        while l<r:
            if s_list[l].isalpha() and s_list[r].isalpha():
                s_list[l], s_list[r] = s_list[r],s_list[l]
                l+=1
                r-=1
            
            if  s_list[l].isalpha() and s_list[r].isalpha() is False:
                r-=1

            if  s_list[l].isalpha() is False and s_list[r].isalpha() is False:
                l+=1
                r-=1

            if  s_list[l].isalpha() is False and s_list[r].isalpha() :
                l+=1
        

        return "".join(s_list)
        