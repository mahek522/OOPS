lst = list(map(int, input("Enter the numbers to be sorted: \n").split()))
for i in range(0, len(lst)-1):
    for j in range(i+1, len(lst)):
        if lst[j] < lst[i]:
            lst[i], lst[j] = lst[j], lst[i]
print("Sorted list is:", lst)