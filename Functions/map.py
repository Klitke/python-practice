# Noobie Intuitive Approach
input_li = list(range(1, 11))
output_li = []


def func(x):
    return x**x

# Long approach
for x in input_li:
    output_li.append(func(x))

# With map()
print(list(map(func, input_li)))

# With list comprehension
print([func(x) for x in input_li])


# Map with dict
# Map returns tuple of key-value pair
some_dict = {"key1": "value1", "key2": "value2"}

def return_dict(pair):
    new_key = str(pair[0]) + "_KeyModified"
    new_value = str(pair[1]) + "_ValueModified"
    
    pair = (new_key, new_value)
    return pair 

print(dict(map(return_dict, some_dict.items())))