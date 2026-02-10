n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
        arr.append(int(input("Enter element: ")))
largest = arr[0]
for x in arr:
        if x > largest:
            largest = x
print("Largest element =", largest)
