class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(letter for letter in s if letter.isalnum()).lower()
        reversed = cleaned[::-1]
 
        return cleaned == reversed