def diagonalDifference(arr):
    left = 0
    right = 0
    for i in range(0, len(arr)):
        left += arr[i][i]
        right += arr[i][len(arr)-i-1]
    return abs(left-right)

if __name__ == '__main__':
    arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    print(diagonalDifference(arr))
