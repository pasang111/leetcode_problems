class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) < len(nums)

    # A list can contain duplicate values, so every element is counted,
    # even if the same number appears multiple times.
    # For example, [1, 2, 3, 4, 5, 1, 1] has 7 elements.
    #
    # A set only keeps unique values, so duplicate numbers are counted once.
    # The same list becomes {1, 2, 3, 4, 5}, which has 5 elements.
    #
    # If the set has fewer elements than the list, it means
    # the list contains duplicates.