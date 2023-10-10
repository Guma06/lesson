# Т: Декораторы

# def my_decorator(func):
#     def wrapper():
#         print('то что выходит до функ')
#         func()
#         print("то что выходит после функ")
#     return wrapper
# @my_decorator
# def hello():
#     print('hello world')
# hello()


# def my_decorator(func):
#     def wrapper():
#         print('то что выходит до функ')
#         print(func())
#         b = func()
#         print(b + 10)
#     return wrapper
# @my_decorator
# def hello():
#     n = 5+5
#     return n
# hello()

# def repeat(num):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(num):
#                 func(*args , **kwargs)
#         return wrapper
#     return decorator

# @repeat(3)
# def say_hello():
#     print('hello')
# say_hello()

def auth_decor(fube ):
    def wrapper(username , passwors , *arg, **kwargo):
        if username == 'admin' and passwors == 'secret':
            result = func(*args , **kwargs)
        else:
            result = 'error'
        return result
    return wrapper
@auth_decor
def my_func():
    return 'Доступ разрешен'
print(my_func('admin' , 'secret'))









