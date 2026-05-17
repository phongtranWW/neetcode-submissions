class Solution:
    def validPalindrome(self, s: str) -> bool:
        def rangePalindrome(left: int, right: int):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return rangePalindrome(left + 1, right) or rangePalindrome(left, right - 1)
            left += 1
            right -= 1

        return True
