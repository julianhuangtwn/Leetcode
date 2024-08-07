'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1
'''

def reverse(x):
        """
        :type x: int
        :rtype: int
        """
        min, max = -1 * 2 ** 31, 2 ** 31 - 1
        sign = 1 if x >= 0 else -1
        x *= sign
        
        numStr = str(x)[::-1]
        x = int(numStr) * sign
        if x < min or x > max:
            return 0
        
        return x

print(reverse(123))
print(reverse(-123))
print(reverse(120))


'''
By converting the int to string, we can use reversal from beginning to end with -1
then manually check if the reversed number exceeds 32 bit bounds or not
'''