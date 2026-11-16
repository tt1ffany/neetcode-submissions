class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        # i is the starting position of the substring
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if (i + len(word)) <= len(s) and s[i : i + len(word)] == word:
                    dp[i] = dp[i + len(word)] # Also checks if the remaining substring is successfully segmented

                # String successfully segmented, don't need to check other words
                if dp[i]:
                    break
                
        return dp[0]