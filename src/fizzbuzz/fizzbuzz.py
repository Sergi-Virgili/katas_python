# Hacer una funcion que devuelva una lista de numeros de 1 al 100
# Que si el numero es divisible por 3 -> Fizz
# Que si el numero es divisible por 5 -> Buzz
# Que si el numero es divisible por 3 y 5 -> FizzBuzz
# Que si no devuelve el numero [1,2,Fizz,4,Buzz,..]
# Si no es un numero devuelve un Error

# USE TDD + Piensa en dividir el problema

def modify_fizzbuzz_number(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz" 
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return number

def fizzbuzz():
    result = []
    for number in range(1,101):
        result.append(modify_fizzbuzz_number(number))
    return result