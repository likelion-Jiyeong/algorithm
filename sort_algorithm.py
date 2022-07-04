# bubble sort => the worst case it takes O(n^2)
def bubbleSort(x):
    for i in range(len(x)-1):
        for j in range(len(x)-i):
            if x[j] > x[j+1]:
                x[j],x[j+1] = x[j+1],x[j] #swap
                
    return x

# 파이썬의 장점을 살린 퀵 정렬
def quick_sort(array):
    # 리스트가 하나 이하의 원소를 가지면 종료
    if len(array) <= 1: return array
    
    pivot, tail = array[0], array[1:]
    
    leftSide = [x for x in tail if x <= pivot]
    rightSide = [x for x in tail if x > pivot]
    
    return quick_sort(leftSide) + [pivot] + quick_sort(rightSide)

def max_search(list):
    n = len(list)
    maxValue = list[0]
    
    for i in range(1,n):
        if list[i] > maxValue:
            maxValue = list[i]
    return maxValue

def min_search(list):
    n = len(list)
    minValue = list[0]

    for i in range(1,n):
        if list[i] < minValue:
            minValue = list[i]
    return minValue
    
