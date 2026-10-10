class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[1]*len(nums)
        pr=1
        po=1
        i=0
        while i<len(nums):
            ans[i]*=pr
            pr*=nums[i]
            i+=1
        i=len(nums)-1
        while i>=0:
            ans[i]*=po
            po*=nums[i]
            i-=1
        return ans