# Use a hashtable to filter out duplicate items

# define a set of items with duplicates
items = ["apple", "pear", "orange", "banana", "apple", "orange", "apple", "pear", "banana", "orange", "kiwi"]

# TODO: create a hashtable to perform a filter
filter = dict()

# TODO: loop over each item and add to the hashtable
for key in items:
    filter[key] = 0

# TODO: create a set from the resulting keys in the hashtable
result = set(filter.keys())
print(result)
