c = list(map(int, input("Enter candidates: ").split()))
t = int(input("Enter target: "))

c.sort()
res = []

def dfs(start, total, path):
    if total == t:
        res.append(path)
        return
    if total > t:
        return

    for i in range(start, len(c)):
        if i > start and c[i] == c[i-1]:
            continue
        dfs(i + 1, total + c[i], path + [c[i]])

dfs(0, 0, [])

if res:
    print("Output:", res)
else:
    print("Target not found")