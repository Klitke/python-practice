# Noobie Intuitive Approach

input_li = list(range(1, 11))
output_li = []

def func(x):
    return x**x

for x in input_li:
    output_li.append(func(x))

# With map()

print(list(map(func, input_li)))

# With list comprehension
print([func(x) for x in input_li])