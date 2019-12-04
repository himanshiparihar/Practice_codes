def maxproduct(numb):
    n = len(numb)
    max_prod = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_prod = max(max_prod,
                numb[first] * numb[second])

    return max_prod


if __name__ == '__main__':
    input_n = int(input())
    input_numb = [int(x) for x in input().split()]
    print(maxproduct(input_numb))
