# A dictionary in python is a hash map
# a hash is a function that takes *anything* as input, and outputs a "unique" value
# hashes try to avoid "collisions", i.e. when two inputs produce the same output.

# dictionaries don't have numbered indices, they are a collection of *key-value* pairs.
# that is each "entry" in a dictionary is two things: the key and the value

my_dictionary = {'name':'Nathaniel', 'age': 41, 5132: ['in BRR'] }

# instead of indexing with a numbered index, dictionaries are indexed by their keys
print(my_dictionary['name'])
print(my_dictionary[5132]) # 5132 is the name of a key, not an index

# dictionaries are mutable
my_dictionary['name'] = 'Hobbs'
print(my_dictionary['name'])
