
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        result = []

        total = 0
        for num in nums:
            total += num
            result.append(total)

        return result


# Example usage
solution = Solution()

nums = [1, 2, 3, 4]
print(solution.runningSum(nums))  # [1, 3, 6, 10]
