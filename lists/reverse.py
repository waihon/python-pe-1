def reverse(lst):
    length = len(lst)
    for i in range(length // 2):
        lst[i], lst[length - i - 1] = lst[length - i - 1], lst[i]

if __name__ == "__main__":
    lst = [10, 1, 8, 3, 5]
    print("Original:", lst)
    reverse(lst)
    print("Reversed:", lst)
