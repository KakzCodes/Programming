"""

A Hash Table is a data structure designed to be fast to work with.

Hash Tables are preferred over arrays or linked lists is because
searching for, adding and deleting data can be done quickly
(in constant time O(1) on average.)

searching an item in a linked list would go from one node to the next
until bob is found, which would take linear time O(n) in the worst case.

searching an item in an array would require a linear search,
which would also take linear time O(n) in the worst case.

but with a Hash Table you can go directly to the index where the item is stored,
which takes constant time O(1) on average.

"""

# 1. Starting with an array.
# 2. Storing names using a hash function.
# 3. Looking up an element using a hash function.
# 4. Handling collisions.
# 5. The basic Hash Set code example and simulation.

my_hash_set = [None,'Jones',None,'Lisa',None,'Bob',None,'Siri','Pete',None]

def hash_function(value):
    sum_of_chars = 0
    for char in value:
        sum_of_chars += ord(char)

    return sum_of_chars % 10
    
def contains(name):
    index = hash_function(name)
    return my_hash_set[index] == name

print("'Pete' is in the Hash Set:",contains('Jack'))