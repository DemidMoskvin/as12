#Task 3
#сортировка выбором, подберу минимальное из тех, что есть, после этого выставлю по порядку
def my_sort(numbers):
    comparisons = 0
    n = len(numbers)
# после определения минимума, выставим остальное    
    for i in range(n):
        smallest = i
        for j in range(i + 1, n):
            comparisons += 1
            if numbers[j] < numbers[smallest]:
                smallest = j
        numbers[i], numbers[smallest] = numbers[smallest], numbers[i]
    
    return numbers, comparisons
# списки для проверки метода
short_l = [5, 2, 9, 1]
long_l = [23, 1, 45, 12, 8, 34, 2, 19, 7, 15]

sorted_short, comp_short = my_sort(short_l)
print(sorted_short, comp_short)
sorted_long, comp_long = my_sort(long_l)
print(sorted_long, comp_long)