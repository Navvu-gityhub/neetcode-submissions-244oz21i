class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer =[1]*(len(nums))
        i=0
        prefix=1
        postfix=1
        while i <len(nums):
            answer[i]*=prefix
            prefix *= nums[i]
            i +=1
        i = len(nums)-1
        while i >=0:
            answer[i]*=postfix
            postfix *= nums[i]
            i -=1
        return answer

