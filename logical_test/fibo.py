


def fibonacci(n_index):
    "'' fib[0] = 0; fib[1] = 1 """
    fib = [0, 1]
    if n_index < 2:
        return fib[n_index]
    else:
        for i in range(1, n_index):
            fib[0], fib[1] = fib[1], fib[0]+fib[1]
        return fib[1]