class Solution:
    # Create a function that takes a Roman numeral
    def romanToInt(self, s: str) -> int:

        # Store each Roman symbol and its value
        values = {
            "I": 1,      # I = 1
            "V": 5,      # V = 5
            "X": 10,     # X = 10
            "L": 50,     # L = 50
            "C": 100,    # C = 100
            "D": 500,    # D = 500
            "M": 1000    # M = 1000
        }

        # Start the answer at 0
        total = 0

        # Loop through all characters except the last one
        for i in range(len(s) - 1):

            # Check if the current value is smaller than the next value
            if values[s[i]] < values[s[i + 1]]:

                # If smaller, subtract the current value
                total = total - values[s[i]]

            # Otherwise, the current value should be added
            else:
                total = total + values[s[i]]

        # Add the last character's value
        total = total + values[s[-1]]

        # Return the final answer
        return total