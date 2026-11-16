class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True # Set valid starting point

        for i in range(1, len(dp)):
            for j in range(i):
                # If valid prev segment and current substring is in wordDict
                if dp[j] and s[j : i] in wordDict:
                    dp[i] = True
                    break

        return dp[len(s)]

