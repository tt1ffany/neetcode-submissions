class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Matrix using lengths of each word + 1
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        # Bottom-up: start at end (bottom-right of matrix) and move backwards
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) -1, -1, -1):
                if text1[i] == text2[j]:
                    # If the letters in each at this position match, add 1 to the diagonal position
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    # If no match, find the max of moving down or right
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        # Result is at top-left of matrix since solution was bottom-up
        return dp[0][0]