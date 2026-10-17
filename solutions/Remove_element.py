class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0  # Position to place the next valid element
        j = 0  # Pointer to check each element

        while j < len(nums):
            if nums[j] != val:  # Keep elements that are not equal to val
                nums[i] = nums[j]  # Move the valid element to position i
                i += 1  # Move to the next position
            j += 1  # Check the next element

        return i  # Return the number of valid element
