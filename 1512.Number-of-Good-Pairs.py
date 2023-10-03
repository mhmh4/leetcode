class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {}
        result = 0
        for n in nums:
            if n in count:
                result += count[n]
                count[n] += 1
            else:
                count[n] = 1
        return result
