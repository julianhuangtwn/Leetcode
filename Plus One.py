'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
 

Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.
'''

def plusOne(digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits) - 1
        digits[i] += 1
        while digits[i] > 9 and i > 0:
            digits[i] = 0
            digits[i - 1] += 1
            i -= 1
            
        if digits[0] == 10:
            digits[0] = 0
            digits.insert(0, 1)
        
        return digits


print(plusOne([1,2,3]))
print(plusOne([4,3,2,1]))
print(plusOne([9]))

'''
The only tricky thing about this is to consider for the case where there are 9s in the array. 
We need to make sure that all the elements will be single digit when 1 is added, 
which can be done by a simple while loop to add one to the next spot

In the case where all digits are 9 in the array, we need to insert a 1 into the first position
'''