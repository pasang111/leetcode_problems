#input: nums = [2,7,11,15] target = 9
#output : [0,1]


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        # Check every number
        for i in range(len(nums)):

            # Check numbers after i
            for j in range(i + 1, len(nums)):

                # If the two numbers add up to target
                if nums[i] + nums[j] == target:
                    return [i, j]  # Return their indexes
