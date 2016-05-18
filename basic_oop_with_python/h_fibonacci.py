def fibonacci(x):
'''
Decided not to do it recursively.
'''
    a = 0
    b = 1
    for i in range(0, x):
        temp = a
        a = b
        b = temp + b
    return a
