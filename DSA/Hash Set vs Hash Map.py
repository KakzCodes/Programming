"""

Uniqueness and storage:
    - Hash Set: Every element is a unique key
    - Hash Map: Every entry is a key-value pair with a unique key and a value connected to it.

Use Case:
    - Hash Set: checking if an element is in the set, like checking if a name is in a list of names.
    - Hash Map: finding information based on a key, like looking up a phone number by name.

Is it fast to search, add and delete elements:
    - Hash Set: Yes, average O(1) time complexity for search
    - Hash Map: Yes, average O(1) time complexity for search

"""

# Hash Tables Summarised #
'''
Every Hash Table element has a part that is unique that is called the key.

A hash function takes the key of an element to generate a hash code.

The hash code says what bucket the element belongs to, so now we can go directly
to that Hash Table element: to modify it, or to delete it, or just to check if it exists.
Specific hash functions are explained in detail on the next two pages.

A collision happens when two Hash Table elements have the same hash code,
because that means they belong to the same bucket. A collision can be solved in two ways.

Chaining is the way collisions are solved in this tutorial,
by using arrays or linked lists to allow more than one element in the same bucket.

Open Addressing is another way to solve collisions. With open addressing,
if we want to store an element but there is already an element in that bucket,
the element is stored in the next available bucket. This can be done in many
different ways, but we will not explain open addressing any further here.
'''