# import sys
# def binary_search(stops,z):
#     left=0
#     right=len(stops)-1
#     while stops[left]<= stops[right]:
#         c=int((right+left)/2)
#         if z == stops[c]:
#             return c
#             break
#         elif stops[left] == stops[right]:
#             if z != stops[c]:
#                 return -1
#                 break
#         elif stops[c]<z:
#             left=c+1
#         else:
#             right=c-1 
 
# if __name__ == '__main__':
#     stops=[]
#     stops1=[]
#     i1=input()
#     stops=i1.split(" ")
#     k=stops[0]
#     del stops[0]
#     i2=input()
#     stops1=i2.split(" ")
#     k12=stops1[0]
#     del stops1[0]
#     for i in range(len(stops1)):
#         z=stops1[i]
#         print(binary_search(stops,z),end=" ")
seq = [int(i) for i in input().split()]
search_seq = [int(i) for i in input().split()]
n = seq[0]
seq = seq[1:]

def binary_search(seq, elt, r):
    l = 0
    while l<=r: 
        m = (l+r)//2
        if elt > seq[m]:
            l = m + 1
        elif elt < seq[m]:
            r = m - 1
        else:
            return m
    return -1

soln1 = list()
for i in search_seq[1:]:
    ans = binary_search(seq, i, n-1)
    soln1.append(ans)
print(' '.join([str(i) for i in soln1]))

