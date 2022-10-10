# insertion sort
def insertion_sort(list):
    for i in range(1, len(list)):
        j = i - 1
        nxt_element = list[i]
        # Compare the current element with next one
        while (list[j] > nxt_element) and (j >= 0):
            list[j + 1] = list[j]
            j = j - 1
        list[j + 1] = nxt_element

def random_list():
    import random
    list = []
    for i in range(10):
        list.append(random.randint(1, 100))
    return list


def main():
    list = random_list()
    print(f'\nrandom list : {list}')
    insertion_sort(list)
    print(f'sorted list : {list}\n')

if __name__ == "__main__":
    main()