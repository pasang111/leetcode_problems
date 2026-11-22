class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:

        # Create an empty list to store the running sums
        result = []

        # Start the total sum from 0
        total = 0

        # Go through each number in the nums list
        for num in nums:

            # Add the current number to the total
            total += num

            # Add the updated total to the result list
            result.append(total)

        # Return the final list of running sums
        return result
