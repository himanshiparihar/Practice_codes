def maxprod(l1):
    maxi=l1[0]*l1[1]
    return maxi
input1=int(input())
l1=[int(x) for x in input().split()]
l1.sort(reverse=True)
print(maxprod(l1))
 


    