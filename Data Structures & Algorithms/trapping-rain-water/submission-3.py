class Solution:
    def trap(self, ht: List[int]) -> int:
        if not ht: return 0
        l,r=0,len(ht)-1
        res=0
        lmax,hmax=ht[l],ht[r]
        while l<r:
            if lmax<hmax:
                l+=1
                lmax=max(lmax,ht[l])
                res+= lmax-ht[l]
            else:
                r-=1
                hmax=max(hmax,ht[r])
                res+= hmax-ht[r]
        return res