n=2
for i in range(1 << n):
        # Convert the current number to a binary string of length n
        binary_str = format(i, '0' + str(n) + 'b')
        print(binary_str)


