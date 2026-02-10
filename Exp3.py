def kth_smallest():
    n = int(input("Enter number of elements: "))
    arr = []
    for i in range(n):
        arr.append(int(input("Enter element: ")))
    k = int(input("Enter k: "))
    arr.sort()
    print(f"{k}th smallest element =", arr[k-1])
kth_smallest()
