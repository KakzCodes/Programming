"""
set is made
code loops through each element (n) and checks if it is already in the set
if it is this means the number has appeared before and the function returns True
if it is not in the set, it is added to the set and the loop continues
if the loop completes without finding any duplicates, the function returns False

why a hashset is more efficient: 
    -checking if an item exists is O(1) on average
    - nested loop would compare each element with every other element, which is O(n^2) WORST CASE

Time and Space complexity is O(1) because size of hashset is limited to the number of unique elements in the input list
which would be 'n' in the worst case, so space complexity is O(n) and time complexity is O(n) as well

"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
    
nums = [1, 2, 3, 3]
solution = Solution()
print(solution.hasDuplicate(nums))  # Output: True