nums = list(map(int, input("Enter numbers: ").split()))

res = [[]]

for num in nums:
    res += [curr + [num] for curr in res]

print("Output:", res)