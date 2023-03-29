import math

def bubblesort(cs):
    new = []
    for i in range(len(cs)-1):
        for j in range(len(cs)-1-i):
            if cs[j]==cs[j+1]:
                new.append(cs[j])
    print(new)


def selectionsort(cs):
    for i in range(len(cs)):
        min_idx = i
        for j in range(i+1,len(cs)):
            if cs[min_idx]==cs[j]:
                min_idx = j
        cs[i],cs[min_idx] = cs[min_idx],cs[i]
    print(cs)


def insertionsort(cs):
    for i in range(1,len(cs)):
        current = cs[i]
        j = i-1  # Previous of current 
        while j>=0 and current<cs[j]:
            cs[j+1] = cs[j]
            j-=1
        cs[j+1] = current
    return cs

cs = [2,1,7,5,3,4,9,8]
# print(insertionsort(cs))

def bucketshort(cs):
    numOfBuckets = round(math.sqrt(len(cs)))
    maxValue = max(cs)
    arr = []

    for i in range(numOfBuckets):
        arr.append([])
    
    for j in cs:
        bucket = math.ceil(j*numOfBuckets/maxValue)
        arr[bucket-1].append(j)
    
    for i in range(numOfBuckets):
        arr[i] = insertionsort(arr[i])
    k=0
    # print(arr)
    for i in range(len(arr)):
        # print(i)
        for j in range(len(arr[i])):
            cs[k] = arr[i][j]
            k += 1
    print(cs)

print(bucketshort(cs))