# import sys
# import random as rd
# def get_majority_element(a, left, right):
#     for ij in a:
#         k=a.count(ij)
#         if k>int(n/2):
#             return 1
#         else:
#             return -1
# if __name__ == '__main__':
#     a=[]
#     # n=int(input())
#     # ni=input()
#     # a=ni.split(" ")
#     n=rd.randrange(100,200)
#     print(n)
#     for z in range(n):
#         ni=rd.randrange(1,1000000)
#         print(ni)
#         a.append(ni)
#     print(a)
#     if get_majority_element(a, 0, n) != -1:
#         print(1)
#     else:
#         print(0)

def findMajority(arr, size): 
    ma = {} 
    for i in range(size): 
        if arr[i] in ma: 
            ma[arr[i]] += 1
        else: 
            ma[arr[i]] = 1
    count = 0
    for key in ma: 
        if ma[key] > size / 2: 
            count = 1
            return 1
            break
    if(count == 0): 
        return 0
  
a=[]
n=int(input())
ni=input()
a=ni.split(" ")
print(findMajority(a, n))
