def add(a, b):
    return float(a) + float(b)
def second_min(number_list):
    sortList = insertion_sort(number_list)
    return sortList[1]
def insertion_sort(number_list):
    x = 1
    while x < len(number_list):
        y = x
        while y > 0 and number_list[y-1] > number_list[y]:
            number_list[y-1], number_list[y] = number_list[y], number_list[y-1]
            y= y - 1
        x = x + 1
    return number_list