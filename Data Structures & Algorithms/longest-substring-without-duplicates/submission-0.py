class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        window = set()
        longest = 0

        # to move right pointer
        for right in range(len(s)):
            char = s[right]

            while char in window:
                window.remove(s[left])
                left += 1

            window.add(char)
            longest = max(longest, right - left + 1)
        
        return longest