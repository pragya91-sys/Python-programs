m = int(input("Enter rows: "))
n = int(input("Enter columns: "))

matrix = []
print("Enter matrix:")
for _ in range(m):
    matrix.append(list(map(int, input().split())))

target = int(input("Enter target: "))

l = 0
r = m * n - 1

found = False

while l <= r:
    mid = (l + r) // 2
    row = mid // n
    col = mid % n

    if matrix[row][col] == target:
        found = True
        break
    elif matrix[row][col] < target:
        l = mid + 1
    else:
        r = mid - 1

print("Output:", found)