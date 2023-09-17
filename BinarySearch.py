
sequence_A = [-100000, -10000, -1000, -100, -10, 0, 10, 100, 1000, 10000, 100000, 1000000, 100000000000, 100000000000000]
item_A = 0
item_B = 100000

def iterativeBinarySearch(sequence, item):
    startPoint = 0
    endPoint = len(sequence) - 1

    while startPoint <= endPoint:
        midPoint = startPoint  + (endPoint - startPoint) // 2
        midpointValue = sequence[midPoint]

        if midpointValue == item:
            return midPoint

        elif item < midpointValue:
            endPoint = midPoint - 1

        else:
            startPoint = midPoint + 1
            
    return None


def recursiveBinarySearch(sequence, startpoint, endpoint, item):

    if startpoint <= endpoint:
        midpoint = (startpoint + endpoint) // 2

        if sequence[midpoint] == item:
            return midpoint
        elif item < sequence[midpoint]:
            return recursiveBinarySearch(sequence, startpoint, midpoint-1, item)
        else:
            return recursiveBinarySearch(sequence, midpoint+1, endpoint, item)
    return None


print(iterativeBinarySearch(sequence_A, item_A))
print(recursiveBinarySearch(sequence_A, 0, len(sequence_A) -1, item_B))