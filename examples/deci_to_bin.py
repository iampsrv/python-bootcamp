def decimal_to_binary(n):
    n = int(n)
    if n == 0:
        return "0"
    
    binary = ''
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    
    return binary

number = 12
binary = decimal_to_binary(number)
print(f"The binary representation of {number} is {binary}")
