class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashy= set()
        for i in nums:
            if i in hashy:
                return True
            hashy.add(i)
        return False 