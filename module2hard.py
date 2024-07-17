n = int(input('Please enter a number from 3 to 20: '))

result = []
for num_in_pair1 in range(1, n-1):
    for num_in_pair2 in range(num_in_pair1+1, n - num_in_pair1+1):
        if n % (num_in_pair1 + num_in_pair2) == 0:
            result.append(str(num_in_pair1))
            result.append(str(num_in_pair2))
print('The password is: ', *result)