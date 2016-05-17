def fibonacci(x):
    a = 0
    b = 1
    for i in range(0, x):
        temp = a
        a = b
        b = temp + b
    return a
