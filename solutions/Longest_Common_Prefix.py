class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        prefix = ""

        for i in range(len(strs[0])):
            for s in strs[1:]:
                if i >= len(s) or strs[0][i] != s[i]:
                    return prefix

            prefix += strs[0][i]

        return prefix