
from numpy import number


#%%
def fizbuzz (list_of_numbers):
    for i in range(1, list_of_numbers):
        if i % 3 == 0 and i % 5 == 0:
            print ('FizzBuzz')
        elif i % 3 == 0:
            print ('Fizz')
        elif i % 5 == 0:
            print ('Buzz')
        else:
            print (str(i))




def test_fizbuzz():
    for i in [2]:
        assert fizbuzz(i) == 'Fizz'
# %%
