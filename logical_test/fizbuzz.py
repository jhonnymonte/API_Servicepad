
def fizbuzz (list_numbers):
    for i in range(list_numbers):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")            
        elif i % 5 == 0:
            print("buzz")            
        print(i)


if __name__ == '__main__':
    n = 100
    print(fizbuzz(n))
