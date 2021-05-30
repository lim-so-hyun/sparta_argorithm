
def solution(L, x):
    for i in range(len(L)):
        if L[i] < x:
            continue
        else:
            L.insert(i,x)
            return L


print (solution([20, 37, 58, 72, 91], 65))

