class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max1=0
        for i in range(0, len(accounts)):
            sum1=0
            for j in range(0,len(accounts[i])):
                sum1=sum1+accounts[i][j]
            if max1<sum1:
                max1=sum1
        return max1
                
                
        