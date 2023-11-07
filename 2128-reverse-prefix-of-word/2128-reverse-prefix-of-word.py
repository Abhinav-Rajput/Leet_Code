class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        res = list(word)
        l =0

        for i in range(len(word)):
            if res[i]==ch:
                while l <=i:
                    res[i],res[l]=res[l],res[i]
                    l+=1
                    i-=1
                return "".join(res)
        return word
        