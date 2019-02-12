# expression vs statement

# expressions evaluate to a value
# we can set expressions as variables

# literals are expressions
7           # int literal
5.0         # float literal
'string'    # string literal
True        # bool literal
[1,2,3]     # list literal
(1,2,3)     # tuple literal
{'k': 'v'}  # dict literal
            # ... etc.

# function calls are expressions, because function calls *evaluate to a value*
# this is why we can set a variable = to a function call
input()     # evaluates to user input
print()     # evaluates to None
            # ... etc.


x = 5               # statement, not an expression 
# conditions are expressions. you can chain them with logical operators.
x == 5              # expression
x != 5              # expression
x < 5               # expression 
x < 5 and x < 10    # also expression 
x < 5 or x > 100    # also expression


# an argument must be an expression
# a return value must be an expression
# a condition must be an expression
# the lefthand side of a comprehension must be an expression


# statements
# statements DO something
# statements do not evaluate to a value

x = 5               # variable assignments are statements

# conditionals are statements
if x <= 5:
    print(x, '<= 5')
else:
    print(x, '> 5')


# loops are statements
for i in range(10):
    pass            # pass is also a statement

while True:
    break           # break is also a statement

# function definitions are statements
def plus_two(x):
    return x + 2    # return statements are also statements
                    # but the value you return is an expression
                    # i.e. x + 2 is an expression
                    # but return x + 2 is an expression

