
# Unacking kwargs
def receive_kwargs(name, age):
    print(name, age)

some_dict = {"name": "Peter", "age": 24}
receive_kwargs(**some_dict)

# Unacking args
def receive_args(first, last):
    print(first, last)

some_list = ["Frank", "Müller"]
receive_args(*some_list)