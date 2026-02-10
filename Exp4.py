n1 = int(input("Enter size of first array: "))
a = []
for i in range(n1):
        a.append(int(input("Enter element: ")))
n2 = int(input("Enter size of second array: "))
b = []
for i in range(n2):
        b.append(int(input("Enter element: ")))
union = list(set(a + b))
print("Union of arrays:", union)