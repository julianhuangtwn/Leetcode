'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
 

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
'''

def firstUniqChar(s: str) -> int:
    charCounts = {}
    for i in range(len(s)):
        if s[i] not in charCounts:
            charCounts[s[i]] = i
        else:
            charCounts[s[i]] = -1

    for char in charCounts:
        if charCounts[char] > -1:
            return charCounts[char]
    return -1


print(firstUniqChar("leetcode"))
print(firstUniqChar("loveleetcode"))
print(firstUniqChar("aabb"))


'''
We can use hashmap to remember the positions of all the letters
If we see a repeated letter we set the stored index to -1
Then iterate through the entire dictionary to find which letters are not repeated
'''