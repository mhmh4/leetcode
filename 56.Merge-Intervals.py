class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stack = []
        for current in intervals:
            if stack and current[0] <= stack[-1][1]:
                stack[-1][1] = max(current[1], stack[-1][1])
            else:
                stack.append(current)
        return stack
