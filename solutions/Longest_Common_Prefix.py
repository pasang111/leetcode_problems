class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # If the list is empty, return an empty string
        if not strs:
            return ""

        prefix = ""

        # Check each character of the first string
        for i in range(len(strs[0])):
            # Compare with all other strings
            for s in strs[1:]:
                # Stop if the string is too short or characters don't match
                if i >= len(s) or strs[0][i] != s[i]:
                    return prefix

            # Add the matching character to the prefix
            prefix += strs[0][i]

        # Return the longest common prefix
        return prefix
