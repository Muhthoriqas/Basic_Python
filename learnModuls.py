import math
def dollar_to_rupiah(money):
    return math.floor(money*15000)

def rupiah_to_dollar(money):
    return math.floor(money/15000)

def find_max(numbers):
    max = numbers[0]

    for i in numbers:
        if i > max:
            max =i
    
    return max