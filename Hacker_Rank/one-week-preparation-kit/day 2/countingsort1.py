def countingSort(arr):
    arr_container = [0] * 100
    for i in range(0, len(arr)):
        arr_container[arr[i]] += 1
    return arr_container


if __name__ == '__main__':
    # arr = random.sample(range(0, 100), 10)
    arr = [1, 4, 1, 2, 7, 5, 2, 3, 20, 32, 99, 20, 50]
    print(countingSort(arr))