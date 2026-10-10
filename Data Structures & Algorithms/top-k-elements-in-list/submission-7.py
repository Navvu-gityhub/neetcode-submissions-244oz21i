class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap={}
        l=[[] for i in range(len(nums)+1)]
        for n in nums:
            hmap[n]=1+hmap.get(n,0)
        for c,f in hmap.items():
            l[f].append(c)
        res=[]
        for j in range(len(l)-1,0,-1):
            for u in l[j]:
                res.append(u)
                if len(res)==k:
                    return res