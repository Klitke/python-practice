# Use case #1: Within a function

def func(x):
    func2 = lambda x: x+5
    return func2(x) + 5

print(func(2))

# Use case #2: with map/filter

some_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(list)

x = list(map(lambda x: x+100, some_list))

print(x)
