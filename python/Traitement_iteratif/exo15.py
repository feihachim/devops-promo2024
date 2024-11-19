def isPrimeNumber(number: int) -> bool:
    if number == 2:
        return True

    limit = number**0.5
    i = 2
    while i <= limit and number % i != 0:
        i += 1

    if number % i == 0:
        return False
    else:
        return True


counter = 0
currentNumber = 2

while counter < 500:
    if isPrimeNumber(currentNumber):
        print(currentNumber)
        counter += 1
    currentNumber += 1
