import arrays
import time

def binary_search(array, target):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    



def binary_search_timer(array, target):
    start = time.perf_counter()
    binary_search(array, target)
    end = time.perf_counter()
    return end - start

def main():
    my_array = arrays.Array(101)
    for i in range(len(my_array)):
        my_array[i] = i
    print(binary_search_timer(my_array, 1))
    print(binary_search_timer(my_array, 50))
    print(binary_search_timer(my_array, 101))



if __name__ == "__main__":
    main()


