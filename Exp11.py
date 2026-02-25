nums = list(map(int, input("Enter sorted numbers: ").split()))
target = int(input("Enter target: "))

l = 0
r = len(nums)

while l < r:
    m = (l + r) // 2
    if nums[m] < target:
        l = m + 1
    else:
        r = m

print("Output:", l)
