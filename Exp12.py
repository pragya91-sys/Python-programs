c = list(map(int, input("Enter candidates: ").split()))
t = int(input("Enter target: "))

res = []

def dfs(i, s, path):
    if s == t:
        res.append(path)
        return
    if s > t or i == len(c):
        return

    dfs(i, s + c[i], path + [c[i]])   # take
    dfs(i + 1, s, path)               # skip

dfs(0, 0, [])
print("Output:", res)