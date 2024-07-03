import numpy as np
import math

if __name__ == '__main__':
    # Создайте одномерный массив чисел от 0 до 9.
    array = np.arange(10)
    print(array)

    # Создайте логический массив размером 3 × 3 из всех True.
    bool_array = np.full((3, 3), True)
    print(bool_array)

    # Извлеките все нечетные числа из arr.
    arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    arr_odd = arr[arr % 2 != 0]
    print(arr_odd)

    # Замените все нечетные числа на -1.
    arr[arr % 2 != 0] = -1
    print(arr)

    # Преобразование одномерного массива в двухмерный массив с двумя строками.
    arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    arr_2D = np.array(arr).reshape(2, math.floor(len(arr) / 2))
    print(arr_2D)

    # Выполните стыковку массивов a и b по вертикали.
    a = np.arange(10).reshape(2, -1)
    b = np.repeat(1, 10).reshape(2, -1)

    arr_a_b = np.concatenate((a, b), axis=0)
    print(arr_a_b)

    # Выполните стыковку массивов a и b по горизонтали.
    arr_a_b = np.concatenate((a, b), axis=1)
    print(arr_a_b)

    # Получите общие элементы между массивами a и b.
    a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
    b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
    a_b = np.intersect1d(a, b)
    print(a_b)

    # Удалите из массива a все элементы, присутствующие в массиве b.
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([5, 6, 7, 8, 9])

    a_not_b = np.setdiff1d(a, b)
    print(a_not_b)

    # Получите позиции, в которых элементы массивов a и b совпадают.
    a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
    b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])

    a_and_b = np.where(a == b)
    print(a_and_b)

    # Получите все элементы от 5 до 10 в массиве a.
    a = np.array([2, 6, 1, 9, 10, 3, 27])
    find = a[(a >= 5) & (a <= 10)]
    print(find)
