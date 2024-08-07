'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
'''

def isAnagram1(self, s: str, t: str) -> bool:
    from collections import Counter
    
    return Counter(s) == Counter(t)

def isAnagram2(s: str, t: str) -> bool:
    charCount = {}
    
    if len(s) != len(t):
        return False
    
    for char in s:
        if char in charCount:
            charCount[char] += 1
        else:
            charCount[char] = 1
    
    for char in t:
        if char in charCount:
            charCount[char] -= 1
            if charCount[char] == 0:
                del charCount[char]
        else:
            return False
    
    return True if not charCount else False

print(isAnagram2("anagram", "nagaram"))
print(isAnagram2("rat", "car"))


'''
Using a hashmap, we can keep a count of all the characters, then go through the second string
If we find the same letter present we subtract, delete the ones that got to 0
If at anytime we find a non-existent letter, return False
The end dictionary should be empty or else return false

We can also make it a little faster to check the length before any operation

The first answer involves using a Counter from collections that is already implemented
'''