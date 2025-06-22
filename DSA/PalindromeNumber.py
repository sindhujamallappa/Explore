'''
Given an integer x, return true if x is a palindrome, and false otherwise.

'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        rev = 0
        orig = x
        while x > 0:
            rev = rev * 10 + x % 10
            x //= 10
        return rev == orig
    

solution = Solution()
result = solution.isPalindrome(100)
print(result)

# Time Complexity: O(logn) because you process each digit once, and the number of digits grows logarithmically with the value of n