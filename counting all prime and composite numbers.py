def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_prime_and_composite(start, end):
    prime_count = 0
    composite_count = 0
    for num in range(start, end + 1):
        if is_prime(num): 
            prime_count += 1
        else:
            composite_count += 1
    return prime_count, composite_count

# Example usage:
start = 1
end = 20
prime_count, composite_count = count_prime_and_composite(start, end)
print("Number of prime numbers between", start, "and", end, ":", prime_count)
print("Number of composite numbers between", start, "and", end, ":", composite_count)
