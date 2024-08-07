'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
'''

def isPalindrome(s: str) -> bool:
    s = ''.join(char for char in s if char.isalnum()).lower()
    
    startPtr = 0
    endPtr = len(s) - 1
    while startPtr < endPtr:
        if s[startPtr] != s[endPtr]:
            return False
        startPtr += 1
        endPtr -= 1
    return True


print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome(" "))

'''
By using the built in isalnum() and lower() to convert the original string into only 
numbers and letters and all lower case, use two pointer approach to compare the letters each step of the way until
both pointers cross each other
'''