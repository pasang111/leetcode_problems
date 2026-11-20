class Solution:
    def lengthofLastWord(self, s:str)->int:
        words = s.split()
        return len(words[-1])