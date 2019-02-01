# defining_functions.py
def greet(name='anonymous', age=0, location='nowhere'):
    """
    prints out a greeting with the name, age, and location parameters
    :age: int, default=0
    :location: string, default='nowhere'
    :name: string, default='anonymous'
    """
    print(f"Hi! My name is {name}. I am {age} years old and from {location}.")


def sum(*args):
    """
    takes a variable number of arguments and returns their sum
    """
    print(type(args), args)
    running_sum = 0
    for num in args:
        running_sum += num
    return running_sum


def make_contact(**kwargs):
    """
    returns a contact dict with all the keyword arguments (kwargs) joined with the defaults dict
    :kwargs: variable number of keyword arguments
    """
    defaults = {'name': 'anonymous', 'phone': 'N/A', 'email': 'N/A'}
    print(type(kwargs), kwargs)
    defaults.update(kwargs)
    return defaults


def no_joe(name):
    """
    exclusive club for those whose names do not start with 'joe'
    """
    print('Hello! You are in function no_joe.')
    if name.strip().lower().startswith('joe'):
        return 'Not allowed in this club. Joe knows why.'
    print('Welcome to Club No Joe')
    print("You're an executive.")


def plus_one(num):
    """
    returns num + 1
    :num: int
    """
    return num + 1


def separate_keys_and_values(dictionary):
    """
    returns tuple of dictionary's keys and values
    """
    return list(dictionary.keys()), list(dictionary.values())

# example with positional and keyword args
greet('larry', 45, 'bird')
greet(age=99, name='ethel', location='FLA')
greet(56, 'hell, michigan')
greet()

# example with variable number of arguments, or *args
print(sum(1,1,1,1,1))
print(sum())
print(sum(1,-2,3,4,5))

# example with variable number of keyword arguments, or **kwargs
print(make_contact(name='ethel', age=99, location='FLA'))

# example with return statement
print('Not allowed in this club. Joe knows why.')
print(no_joe('jose'))

# example of how you can chain function calls
# function calls 'boil down' into whatever the function returns
print(plus_one(1)) # prints 2
print(plus_one(plus_one(1))) # prints plus_one(2) or 3
print(plus_one(plus_one(plus_one(1)))) # prints plus_one(3) or 4

# example of returning multiple values as tuple
print(separate_keys_and_values({'a': 'apples', 'b': 'buffet'}))

# example of tuple unpacking
keys, values = separate_keys_and_values({'name': 'ethel', 'age': 99, 'location': 'FLA'})
print(keys, values)