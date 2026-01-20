def deco(func):
    def inner():
        str1 = func()
        return str1.upper()
    return inner

# @deco
def print_str():
    return "vijay"

a = deco(print_str)
print(a())