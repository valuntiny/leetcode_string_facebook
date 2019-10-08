"""
Question:
    Given a string, find the length of the longest substring without repeating characters.

    Example 1:
    Input: "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

    Example 2:
    Input: "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

    Example 3:
    Input: "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
                 Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

Solution:
    - hashmap? (key, value) = (char, index)
    - consider "" and " " and no repetition
    - use a starter to tract the starting point
    - so hard ... damn
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        hashtable = {}
        res = starter = 0

        for i in range(len(s)):
            if s[i] in hashtable.keys() and starter <= hashtable[s[i]]:
                starter = hashtable[s[i]] + 1
            else:
                res = max(res, i - starter + 1)

            hashtable[s[i]] = i

        return res


test = Solution()
s = " "
print(test.lengthOfLongestSubstring(s))