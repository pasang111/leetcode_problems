# Note before doing this solution
# 1. Get the last digit
# digit = x % 10
# Example: 121 % 10 = 1

# 2. Remove the last digit
# x = x // 10
# Example: 121 // 10 = 12

# 3. Build the reverse number
# reverse = reverse * 10 + digit
# Example:
# reverse = 1, digit = 2
# reverse = 1 * 10 + 2 = 12
# Remember:
# % 10 → GET the last digit
# // 10 → REMOVE the last digit
# * 10 → Make space for the next digit

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False  # Negative numbers are not palindromes

        original = x  # Save the original number
        reverse = 0   # Start the reversed number at 0

        while x > 0:  # Keep running while digits are left
            digit = x % 10  # Get the last digit
            reverse = reverse * 10 + digit  # Add digit to reversed number
            x = x // 10  # Remove the last digit

        if original == reverse:  # Check if original and reverse are same
            return True  # It is a palindrome

        return False  # It is not a palindrome

