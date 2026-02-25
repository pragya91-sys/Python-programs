n = int(input("Enter number of strings: "))
strs = []

for _ in range(n):
    strs.append(input())

d = {}

for s in strs:
    key = ''.join(sorted(s))
    if key in d:
        d[key].append(s)
    else:
        d[key] = [s]

print("Output:", list(d.values()))