class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ans = 0
        minSoFar = prices[0]
        for i in range(1, n):
            ans = max(ans, prices[i] - minSoFar)
            minSoFar = min(minSoFar, prices[i])
        return ans
    
    
#         flag=0
#         for i in range(len(prices)-1):
#             if prices[i]<prices[i+1]:
#                 flag=1
#                 break
#         if flag==0:
#             return 0
        
#         buy = prices[0]
#         sell = prices[1]
#         if sell>buy:
#             profit = sell-buy
#         else:
#             profit=0
#         for i in range(len(prices)):            
#             for j in range(i+1,len(prices)):
#                 if prices[j]-prices[i]>profit:
#                     profit= prices[j]-prices[i]
#         return profit
        