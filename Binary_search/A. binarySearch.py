# Реализуйте алгоритм бинарного поиска.

# Входные данные
# В первой строке входных данных содержатся натуральные числа N
#  и K(0<N,K≤100000). Во второй строке задаются N
#  элементов первого массива, отсортированного по возрастанию, а в третьей строке – K
#  элементов второго массива. Элементы обоих массивов - целые числа, каждое из которых по модулю не превосходит 109

# Выходные данные
# Требуется для каждого из K чисел вывести в отдельную строку "YES", если это число встречается в первом массиве, и "NO" в противном случае.
def bin_search(arr, x):
    left = -1
    right = len(arr)
    while right - left > 1:
        m = (left + right ) // 2
        if x == arr[m]:
            return "YES"
        elif arr[m] < x:
            left = m
        else:
            right = m
    return "NO"



n, k = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

for i in range(k):
    res = bin_search(arr1 , arr2[i])
    print(res)
