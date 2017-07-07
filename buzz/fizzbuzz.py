
def generate(start, stop):
    result = {}
    for number in range(start, stop+1):
        item = ''
        if number % 3 == 0:
            item += 'Fizz'
        if number % 5 == 0:
            item += 'Buzz'
        result[number] = item if item else number
    return result
