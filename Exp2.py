def find_min_max():
    n = int(input("Enter number of elements: "))
    arr = []
    for i in range(n):
        num = int(input("Enter element: "))
        arr.append(num)
    minimum = arr[0]
    maximum = arr[0]
    for x in arr:
        if x < minimum:
            minimum = x
        if x > maximum:
            maximum = x
    print("Minimum =", minimum)
    print("Maximum =", maximum)
find_min_max()
