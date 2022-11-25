def quick_sort(char_list, start, end):
    if start < end:
        pivot = partition(char_list, start, end)

        quick_sort(char_list, start, pivot - 1)
        quick_sort(char_list, pivot + 1, end)


def partition(char_list, start, end):
    pivot = char_list[end]
    delimiter = start - 1

    for index in range(start, end):
        if char_list[index] <= pivot:
            delimiter = delimiter + 1
            char_list[index], char_list[delimiter] = (
                char_list[delimiter],
                char_list[index],
            )

    char_list[delimiter + 1], char_list[end] = (
        char_list[end],
        char_list[delimiter + 1],
    )
    return delimiter + 1


def is_anagram(first_string, second_string):
    if first_string == "" and second_string == "":
        return (first_string, second_string, False)

    first_string_list = list(first_string.lower())
    second_string_list = list(second_string.lower())

    quick_sort(first_string_list, 0, len(first_string_list) - 1)
    quick_sort(second_string_list, 0, len(second_string_list) - 1)

    sorted_first_string = "".join(first_string_list)
    sorted_second_string = "".join(second_string_list)

    return (
        sorted_first_string,
        sorted_second_string,
        sorted_first_string == sorted_second_string,
    )
