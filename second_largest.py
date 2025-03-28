arr = list(map(int, input("Enter array: ").split()))

non_zeros = []
zero_count = 0
for num in arr:
    if num == 0:
        zero_count += 1
    else:
        non_zeros.append(num)
arr[:] = non_zeros + [0] * zero_count
print(arr)
