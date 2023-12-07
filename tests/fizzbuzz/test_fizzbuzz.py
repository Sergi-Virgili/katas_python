from fizzbuzz.fizzbuzz import modify_fizzbuzz_number, fizzbuzz

def test_retuns_Fizz_if_3_multipy():
    result = modify_fizzbuzz_number(9)
    assert result == "Fizz"

def test_retuns_Buzz_if_5_multipy():
    result = modify_fizzbuzz_number(10)
    assert result == "Buzz"

def test_retuns_FizzBuzz_if_3_and_5_multipy():
    result = modify_fizzbuzz_number(15)
    assert result == "FizzBuzz"

def test_retuns_number_if_not():
    result = modify_fizzbuzz_number(13)
    assert result == 13

def test_retuns_list_of_fizzbuzz_numbers():
    result =fizzbuzz()
    assert len(result) == 100
    assert result[0] == 1
    assert result[99] == "Buzz"
    assert result[2] == "Fizz"
    assert result[14] == "FizzBuzz"