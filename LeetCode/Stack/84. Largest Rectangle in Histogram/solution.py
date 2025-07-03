class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i in range(len(heights)):
            index = i
            while stack and stack[-1][1] > heights[i]:
                start, h = stack.pop()
                res = max(res, (i - start) * h)
                index = start
            stack.append([index, heights[i]])
        
        for i, h in stack:
            res = max(res, (len(heights) - i) * h)
        
        return res
