class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        """
        Returns an array where each element is the
        cumulative sum of all previous elements.
        """
        result = []
        total = 0

        for num in nums:
            total += num
            result.append(total)

        return result
