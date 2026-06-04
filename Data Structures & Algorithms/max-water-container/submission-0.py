class Solution:
    def maxArea(self, ht: List[int]) -> int:
        res=0
        l,r=0,len(ht)-1
        while l<r:
            ar=(r-l)*min(ht[l],ht[r])
            res=max(res,ar)
            if ht[l]<ht[r]:
                l+=1
            else:
                r-=1
        return res