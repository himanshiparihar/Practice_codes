import sys
import random


def partition3(a, left, right):
    pivot_value = a[left]
    p_l = i1 = left
    p_e = right
    while i1 <= p_e:
        if a[i1] < pivot_value:
            a[i1], a[p_l] = a[p_l], a[i1]
            p_l += 1
            i1 += 1
        elif a[i1] == pivot_value:
            i1 += 1
        else:
            a[i1], a[p_e] = a[p_e], a[i1]
            p_e -= 1
        pIndexes = [p_l, p_e]
    return pIndexes


def partition2(a, left, right):
    pivot = random.randint(left, right)
    a[right], a[pivot] = a[pivot], a[right]
    pivot_value = a[right]
    pIndex = left
    for i1 in range(left, right):
        if a[i1] <= pivot_value:
            a[i1], a[pIndex] = a[pIndex], a[i1]
            pIndex += 1
    a[right], a[pIndex] = a[pIndex], a[right]
    return pIndex


def randomized_quick_sort(a, left, right):
    if left >= right:
        return

    pivot = random.randint(left, right)
    a[left], a[pivot] = a[pivot], a[left]
    pIndex = partition3(a, left, right)
    randomized_quick_sort(a, left, pIndex[0] - 1)
    randomized_quick_sort(a, pIndex[1] + 1, right)


if __name__ == '__main__':
    # input = sys.stdin.read()
    # n1, *a = list(map(int, input.split()))
    # randomized_quick_sort(a, 0, n1 - 1)
    # for x1 in a:
    #     print(x1, end=' ')
    k=int(input())
    a = list(map(int,input(" ").strip().split()))[:k]  
    randomized_quick_sort(a, 0, len(a) - 1) 
    listToStr = ' '.join([str(elem) for elem in a])
    print(listToStr)