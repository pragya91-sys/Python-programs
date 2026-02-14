def two_sum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return i, j
n = int(input("Enter number of elements: "))
nums = []
for i in range(n):
    nums.append(int(input(f"Enter element {i+1}: ")))
target = int(input("Enter target: "))
result = two_sum(nums, target)
print("Indices:", result)
