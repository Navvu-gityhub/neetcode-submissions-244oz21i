class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0,len(numbers)-1
        while l<r:
            sumy=numbers[l]+numbers[r]
            if sumy<target:
                l+=1
            elif sumy>target:
                r-=1
            else:
                return [l+1,r+1] 