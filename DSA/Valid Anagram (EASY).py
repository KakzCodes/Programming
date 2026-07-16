"""
Input: s = "racecar", t = "carrace"
return: True

Input: s = "jar", t = "jam"
return: False

end up checking if there are the same number of characters again in both strings which becomes
a problem of counting the number of characters in each string and comparing them.

efficient method would be to use a hashset like in the 'Contains Duplicate' problem because
we can check if the characters in one string are in the other string and if they are not, we can return False
but you cant store duplicate items in a hashset so this cannot work

could check how many characters there of each type in each string and compare them but that would be inefficient

can use a hashmap though to store the number of characters in each string and then compare the two hashmaps to see if they are equal

for example:
    - {r: 2, a: 2, c: 2, e: 2}
    - {c: 2, a: 2, r: 2, e: 2}
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # anagram must have same number of characters so if the lengths are not equal, return False
        if len(s) != len(t):
            return False

        # initialising 2 empty dictionaries to store character counts for each string
        map_s = {}
        map_t = {}

        # loops through every character in s
        for char in s:

            # counts how many times each character appears in s and stores it in map_s
            map_s[char] = map_s.get(char, 0) + 1

        for char in t:
            map_t[char] = map_t.get(char, 0) + 1

        for key in map_s:
            if map_s[key] != map_t.get(key, 0):
                return False
        return True