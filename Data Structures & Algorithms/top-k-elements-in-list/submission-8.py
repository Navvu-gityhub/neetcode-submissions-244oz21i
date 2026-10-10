class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap={}
        l=[[] for i in range(len(nums)+1)]
        for n in nums:
            hmap[n]=1+hmap.get(n,0)
        for r,s in hmap.items():
            l[s].append(r)
        res=[]
        for u in range(len(l)-1,0,-1):
            for y in  l[u]:
                res.append(y)
                if len(res)==k:
                    return res
                    
