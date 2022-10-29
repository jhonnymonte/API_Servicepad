
def fizbuzz (list_numbers):
    for i in range(list_numbers):
        if i % 3 == 0 and i % 5 == 0:
            print ('FizzBuzz')
        elif i % 3 == 0:
            print ('Fizz')
        elif i % 5 == 0:
            print ('Buzz')
        else:
            print (str(i))

list_numbers= 100
