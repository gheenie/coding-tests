import math


def gcdi(x,y):
    # your code
    return math.gcd(x, y)


def lcmu(a, b):
    # your code
    return math.lcm(abs(a), abs(b))


def som(a, b):
    # your code
    return a + b


def maxi(a, b):
    # your code
    return max(a, b)


def mini(a, b):
    # your code
    return min(a, b)


def oper_array(fct, arr, init): 
    # your code
    reduced = []
    last_step = init
    
    for element in arr:
        current_step = fct(last_step, element)
        reduced.append(current_step)
        last_step = current_step
    
    return reduced


# Should return [2, 6, 12, 20, 30, 50]
print(oper_array(som, [2, 4, 6, 8, 10, 20], 0))
