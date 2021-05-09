def isOdd(x):
    return x%2 != 0

def add100(x):
    return x + 100

raw_list = [1,2,3,4,5,6,7,8,9,10]
filtered_list = list(filter(isOdd, raw_list))
print(filtered_list)

processed_list = list(map(add100, filter(isOdd, raw_list)))
print(processed_list)
