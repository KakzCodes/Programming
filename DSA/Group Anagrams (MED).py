'''
Group Anagrams:
- Given an array of strings, group anagrams together.
- Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: 
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
'''

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Map sorted word -> list of original words
        anagram_map = defaultdict(list)
    
        for s in strs:
            # Sort string to create unique key: "eat" -> ("a", "e", "t")
            sorted_key = tuple(sorted(s))
            
            # Group original string under its sorted signature
            anagram_map[sorted_key].append(s)
            
        # Return grouped lists
        return list(anagram_map.values())