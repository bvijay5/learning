def greet(fn):
    def wrapper(*args):
        print("Hello")
        fn(*args)
        print("Thanks for using this function")
    return wrapper

@greet
def summ(a,b):
    print(a+b)

summ(5,6)


# def greet(fn):
#     def wrapper(*args):
#         print("Hello")
#         result = fn(*args)
#         print(result)
#         print("Thanks for using this function")
#         return result
#     return wrapper

# @greet
# def summ(a,b):
#     return a+b

# summ(5,6)
