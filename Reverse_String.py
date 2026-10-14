class Solution:
    def reverseString(self, s: list[str]) -> None:
        i = 0  # Start pointer
        j = len(s) - 1  # End pointer

        while i < j:  # Continue until pointers meet
            s[i], s[j] = s[j], s[i]  # Swap characters

            i += 1  # Move start pointer forward
            j -= 1  # Move end pointer backward
