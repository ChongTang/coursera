'''
Usage: python count_inversion.py test_data.txt
'''
import sys


def count_inversion(A):
    '''
    This function count inversions in the given input array.
    '''
    length = len(A)
    if length <= 1:
        return(A, 0)

    n = length // 2
    C = A[:n]
    D = A[n:]
    # count inversion in the left half
    C, c = count_inversion(A[:n])
    # count inversion in the right half
    D, d = count_inversion(A[n:])
    # count the inversion in merge
    B, b = merge_and_count(C, D)
    return(B, b+c+d)


def merge_and_count(C, D):
    '''
    This function merge and count inverison
    '''
    count = 0
    M = []
    while C and D:
        if C[0] <= D[0]:
            M.append(C.pop(0))
        else:
            count += len(C)
            M.append(D.pop(0))
    M += C + D
    return(M, count)


# read test data
test_data = sys.argv[1]
test_arr = []
with open(test_data, 'r') as fp:
    for line in fp:
        test_arr.append(int(line.strip()))

# call count_inversion function
print(count_inversion(test_arr))
