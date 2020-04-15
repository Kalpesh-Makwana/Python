def is_prime(n):
    for i in range(2, int(n/2)+1):
        if n%i == 0:
            return False
    else:
        return True

def prime(number):
    n = 2
    x = 1
    while x != number:
        n += 1
        if is_prime(n):
            x += 1
    return n