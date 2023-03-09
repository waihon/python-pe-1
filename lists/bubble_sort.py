def bubble_sort(lst, reverse=False):
    swapped = True # It's a little fake, we need it to enter the while loop

    while swapped:
        swapped = False # no swaps so far
        for i in range(len(lst) - 1):
            if (lst[i] > lst[i + 1]) == (not reverse):
                swapped = True
                lst[i], lst[i + 1] = lst[i + 1], lst[i]

if __name__ == "__main__":
    my_list = [8, 10, 6, 2, 4]
    print("Original:", my_list)
    bubble_sort(my_list)
    print("Increasing order:", my_list)

    my_list = [8, 10, 6, 2, 4]
    print("Original:", my_list)
    bubble_sort(my_list, reverse=True)
    print("Decreasing order:", my_list)
