def uppercase_decorator(function):
    def wrapper():
        func = function()
        return func.upper()
    return wrapper

@uppercase_decorator
def say_hi():
    return 'hello there'

say_hi_uppercase = uppercase_decorator(say_hi)

result = say_hi_uppercase()

print(result)