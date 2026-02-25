nums = list(map(int, input("Enter numbers: ").split()))

jumps = 0
curr_end = 0
far = 0

for i in range(len(nums) - 1):
    far = max(far, i + nums[i])

    if i == curr_end:
        jumps += 1
        curr_end = far

print("Output:", jumps)