class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice=prices[0]
        maxprof=0
        for p in prices:
            minprice=min(minprice,p)
            profit=p-minprice
            maxprof=max(maxprof,profit)
        return maxprof