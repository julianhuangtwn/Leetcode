'''
You are given a 0-indexed string s, a string a, a string b, and an integer k.

An index i is beautiful if:

>>> 0 <= i <= s.length - a.length
>>> s[i..(i + a.length - 1)] == a

There exists an index j such that:
>>> 0 <= j <= s.length - b.length
>>> s[j..(j + b.length - 1)] == b
>>> |j - i| <= k
Return the array that contains beautiful indices in sorted order from smallest to largest.
'''

def beautifulIndices(s, a, b, k):
        """
        :type s: str
        :type a: str
        :type b: str
        :type k: int
        :rtype: List[int]
        """
        beautList = []
        aIndexList = []
        bIndexList = []
        
		# Stores the indexes of the substring a and b of s into lists
        aIndex = s.find(a)
        while aIndex != -1:
            aIndexList.append(aIndex)
            aIndex = s.find(a, aIndex + 1)
        
        bIndex = s.find(b)
        while bIndex != -1:
            bIndexList.append(bIndex)
            bIndex = s.find(b, bIndex + 1)

        # Going through every indexes combination, as long as condition fits, i in aIndexList is a beautiful index
        for i in aIndexList:
            for j in bIndexList:
                if abs(j - i) <= k:
                    beautList.append(i)
                    break
                            
        return sorted(beautList)


print(beautifulIndices("abcd", "a", "a", 4))
'''
Input: s = "abcd", a = "a", b = "a", k = 4
Output: [0]
Explanation: There is 1 beautiful index: [0].
- The index 0 is beautiful as s[0 ... 0] == "a" and there exists an index 0 with s[0 ... 0] == "a" and |0 - 0| <= 4.
'''

print(beautifulIndices("isawsquirrelnearmysquirrelhouseohmy", "my", "squirrel", 15))
'''
There are 2 beautiful indices: [16,33].
- The index 16 is beautiful as s[16 ... 17] == "my" and there exists an index 4 with s[4 ... 11] == "squirrel" and |16 - 4| <= 15.
- The index 33 is beautiful as s[33 ... 34] == "my" and there exists an index 18 with s[18 ... 25] == "squirrel" and |33 - 18| <= 15.
'''


'''
The question seemingly asked for many requirements, but actually, the condition where 0 <= i <= s.length - a.length will always be true, as this is simply saying
you don't need to access substring of s that has a length less than a, because it won't be possible for example for the last character in s: "l" to contain the word "my"
Hence, all we have to care about first is to find all the indexes of the substrings, and store the indexes
Then, go through the indexes, and make sure that last condition fits, where abs(k - i) <- k
'''