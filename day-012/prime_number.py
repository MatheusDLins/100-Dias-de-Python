
def is_prime(num):
    primos = [2, 3, 5, 7]
    if num == 1:
        return False
    elif (num not in primos):
        if (num % 2) == 0:
            return False
        elif (num % 3) == 0:
            return False
        elif (num % 5) == 0:
            return False
        elif (num % 7) == 0:
            return False
        else:
            return True
    else:
        return True


print(is_prime(1))
