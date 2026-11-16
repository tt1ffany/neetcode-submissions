class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Initializing memo also handles base case of reaching end of string
        memo = {len(s) : True}

        def dfs(startingPos):
            if startingPos in memo:
                return memo[startingPos]

            for word in wordDict:
                if ((startingPos + len(word) <= len(s)) and s[startingPos : startingPos + len(word)] == word):
                    if dfs(startingPos + len(word)):
                        memo[startingPos] = True
                        return True

            memo[startingPos] = False
            return False

        return dfs(0)