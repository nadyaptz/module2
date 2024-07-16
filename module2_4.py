numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in numbers:
    is_prime = True
    if i == 1:  # проверяем, не 1 ли (1 не простое и не сложное число)
        is_prime = False
    for j in range(2, i - 1):   # перебираем делители от 2 до самого числа -1
        if i % j == 0:          # если делится без остатка, то число не простое
            is_prime = False
            not_primes.append(i)
            break
    if is_prime == True:
        primes.append(i)

print('Primes:', primes)
print('Not primes:', not_primes)
