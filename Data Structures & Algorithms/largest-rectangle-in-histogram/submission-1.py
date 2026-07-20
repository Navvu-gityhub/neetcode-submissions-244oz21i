class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ma=0
        stack=[]
        for i,h in enumerate(heights):
            start=i
            while stack and stack[-1][1]>h:
                index,ht=stack.pop()
                ma=max(ma,ht*(i-index))
                start=index
            stack.append([start,h])
        for i,h in stack:
            ma=max(ma,h*(len(heights)-i))
        return ma