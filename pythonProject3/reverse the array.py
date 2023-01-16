def reverseArray(arr, m):
    n = len(arr)

    # Declare and initialize ArrayList named 'brr'.
    brr = []

    for i in range(len(arr)):
        brr.append(0)

    # Declare a varibale p.
    p = 0

    # First fill the brr in the same order as the original array upto Mth postion.
    for i in range(m + 1):
        brr[p] = arr[i]
        p += 1

    # Now fill the brr in the reverse order till (m+1)th postion.
    for j in range(n - 1, m, -1):
        brr[p] = arr[j]
        p += 1

    # Now copy back the array brr into array arr.
    for i in range(n):
        arr[i] = brr[i]

    return arr


#
a=(10,20,30,40)
b,*c=a
print(a)
print(b)
print(c)

