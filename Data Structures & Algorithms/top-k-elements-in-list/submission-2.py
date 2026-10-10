class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        frq=[[]for i in range(len(nums)+1)]#List[List]
        for n in nums:
            count[n]=1+count.get(n,0)#n:freq
        for e,f in count.items():
            frq[f].append(e)#freq->element
        res=[]
        for i in range(len(frq)-1,0,-1):
            for n in frq[i]:
                res.append(n)
                if len(res)==k:
                    return res
        