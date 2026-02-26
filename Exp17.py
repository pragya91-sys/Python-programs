m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

matrix = []
print("Enter matrix:")
for _ in range(m):
    matrix.append(list(map(int, input().split())))

rows = set()
cols = set()

for i in range(m):
    for j in range(n):
        if matrix[i][j] == 0:
            rows.add(i)
            cols.add(j)

for i in range(m):
    for j in range(n):
        if i in rows or j in cols:
            matrix[i][j] = 0

print("Output:")
for row in matrix:
    print(row)