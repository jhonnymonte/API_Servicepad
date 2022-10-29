
import fizbuzz


def test_multiples_of_three():
    n = 3
    assert "fizz" == fizbuzz(n)


def test_multiples_of_five():
    n = 5
    assert "buzz" == fizbuzz(n)


def test_multiples_of_three_and_five():
    n = 15
    assert "fizz buzz" == fizbuzz(n)
