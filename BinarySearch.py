def binarySearch(sequence, item):
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

sequence_A = [-100000, -10000, -1000, -100, -10, 0, 10, 100, 1000, 10000, 100000, 1000000, 100000000000, 100000000000000]
item_A = 0

print(binarySearch(sequence_A, item_A))