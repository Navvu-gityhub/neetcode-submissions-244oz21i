class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap={}
        f=[[] for i in range(len(nums)+1)]
        for n in nums:
            hmap[n]=1+hmap.get(n,0)
        '''
            | element -> freq|
        '''
        for j,k1 in hmap.items():
            f[k1].append(j)
        res=[]
        for i  in range(len(f)-1,0,-1):
            for j in f[i]:
                res.append(j)
                if len(res)==k:
                    return res
            