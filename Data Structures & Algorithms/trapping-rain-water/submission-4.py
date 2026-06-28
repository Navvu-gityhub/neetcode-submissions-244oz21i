class Solution:
    def trap(self, ht: List[int]) -> int:
        if not ht: return 0
        l,r=0,len(ht)-1
        ltmax,htmax=ht[l],ht[r]
        res=0
        while l<r:
            if ltmax<htmax:
                l+=1
                ltmax=max(ltmax,ht[l])
                res+=ltmax-ht[l]
            else:
                r-=1
                htmax=max(htmax,ht[r])
                res+=htmax-ht[r]
        return res