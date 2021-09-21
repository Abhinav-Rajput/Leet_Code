class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(s)):
            if s[i] in sentence:
                flag= 1
            else:
                flag = 0
                break
        if flag==0:
            return False
        else:
            return True
        
        
        