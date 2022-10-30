def fibonacci_series(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

def main():
    print (fibonacci_series(100))

if __name__ == '__main__' : main()