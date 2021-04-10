"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
Хотя в примерах к уроку уже есть вариант реализации слияния,
попробуйте предложить другой (придумать или найти)
И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...
Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

import random

# def sort_merge(lst):
#     if len(lst) > 1:
#         center = len(lst) // 2
#         left = lst[:center]
#         right = lst[center:]
#
#         sort_merge(left)
#         sort_merge(right)
#
#     if len(lst)


# def merge_sort(lst_obj):
#     if len(lst_obj) > 1:
#         center = len(lst_obj) // 2
#         left = lst_obj[:center]
#         right = lst_obj[center:]
#
#         merge_sort(left)
#         merge_sort(right)
#
#         # перестали делить
#         # выполняем слияние
#         i, j, k = 0, 0, 0
#
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 lst_obj[k] = left[i]
#                 i += 1
#             else:
#                 lst_obj[k] = right[j]
#                 j += 1
#             k += 1
#
#         while i < len(left):
#             lst_obj[k] = left[i]
#             i += 1
#             k += 1
#
#         while j < len(right):
#             lst_obj[k] = right[j]
#             j += 1
#             k += 1
#         return lst_obj


def merge_sort_optimized(lst_obj):
    if len(lst_obj) > 1:
        center = len(lst_obj) // 2
        left = lst_obj[:center]
        right = lst_obj[center:]

        merge_sort_optimized(left)
        merge_sort_optimized(right)

        

        return lst_obj


n = 10
prime_lst = [(random.random() * 50) for _ in range(0, n)]
prime_lst = [random.randint(0,1000) for _ in range(0, n)]
print(prime_lst)
print(merge_sort_optimized(prime_lst[:]))