my_hash_set = [
    [None],
    ['Jones'],
    [None],
    ['Lisa', 'Stuart'],
    [None],
    ['Bob'],
    [None],
    ['Siri'],
    ['Pete'],
    [None]
]

# trying to store 'Stuart' in the Hash Set, but it collides with 'Lisa' at index 3
# to solve this, we can use a list to store multiple values at the same index (chaining)

# this is a simple hash function that sums the ASCII values of the characters in the 
# string and takes the modulus with 10 to get an index between 0 and 9.
def hash_function(value):
    return sum(ord(char) for char in value) % 10

# this function checks if a value is in the Hash Set by looking
# up the index using the hash function
def add(value):
    index = hash_function(value)
    bucket = my_hash_set[index]
    if value not in bucket:
        bucket.append(value)

# this function checks if a value is in the Hash Set by looking
# up the index using the hash function and checking if the value is in the bucket
def contains(value):
    index = hash_function(value)
    bucket = my_hash_set[index]
    return value in bucket

add('Stuart')

print(my_hash_set)
print('Contains Stuart:',contains('Stuart'))