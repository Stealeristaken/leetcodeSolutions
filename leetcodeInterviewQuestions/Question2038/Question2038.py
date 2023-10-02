class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        totalA = 0  # Initialize a variable to store the total points of player A.
        totalB = 0  # Initialize a variable to store the total points of player B.
        currA = 0   # Initialize a variable to count the current consecutive colors of A.
        currB = 0   # Initialize a variable to count the current consecutive colors of B.

        # Iterate through the characters in the 'colors' string.
        for char in colors:
            if char == 'A':    # If the current character is 'A':
                currA += 1     # Increment the count of consecutive 'A' colors.
                if currB > 2:  # If there were more than 2 consecutive 'B' colors before this 'A':
                    totalB += currB - 2  # Add the excess consecutive 'B' colors to totalB.
                currB = 0       # Reset the consecutive 'B' count since there's an 'A'.
            else:              # If the current character is 'B':
                currB += 1     # Increment the count of consecutive 'B' colors.
                if currA > 2:  # If there were more than 2 consecutive 'A' colors before this 'B':
                    totalA += currA - 2  # Add the excess consecutive 'A' colors to totalA.
                currA = 0       # Reset the consecutive 'A' count since there's a 'B'.

        # After the loop, add any remaining consecutive 'A' and 'B' colors to their respective totals.
        if currA > 2:
            totalA += currA - 2
        if currB > 2:
            totalB += currB - 2

        # Compare the total points for 'A' and 'B' to determine the winner.
        return totalA > totalB  # If 'A' has more points, return True (A wins); otherwise, return False (B wins or it's a tie).