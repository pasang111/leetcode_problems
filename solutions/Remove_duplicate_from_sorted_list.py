class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0  # CMT: Points to the last unique element
        j = 1  # CMT: Checks the next element

        while j < len(nums):  # CMT: Loop through the array
            if nums[i] != nums[j]:  # CMT: Check if the element is unique
                i += 1  # CMT: Move to the next position
                nums[i] = nums[j]  # CMT: Store the unique element
            j += 1  # CMT: Move to the next element

        return i + 1  # CMT: return the count of unique element

#solutions
