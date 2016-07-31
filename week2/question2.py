import sys


def partition(A, left, right):
    # switch the last element and the first one
    A[left], A[right] = A[right], A[left]
    p = A[left]
    i = left + 1  # i is the first element of second half
    for j in range(left+1, right+1):
        if A[j] < p:
            A[j], A[i] = A[i], A[j]
            i += 1

    A[left], A[i-1] = A[i-1], A[left]
    return(i-1)   # return pivot index


def quicksort(A, left, right):
    if left >= right:
        return(0)
    cnt = right - left  # number of comparison
    p = partition(A, left, right)
    cnt += quicksort(A, left, p-1)
    cnt += quicksort(A, p+1, right)
    return(cnt)

data_file = sys.argv[1]
test_arr = []
# read test data
with open(data_file, 'rb') as fp:
    for line in fp:
        test_arr.append(int(line.strip()))

cnt = quicksort(test_arr, 0, len(test_arr)-1)
print(cnt)
