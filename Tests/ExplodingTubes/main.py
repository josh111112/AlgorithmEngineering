def main():
    line1 = input().split()
    numtubes = int(line1[0])
    numexplodingtubes = int(line1[1])
    explodingtubes = input().split()
    explodingtubes = [int(x) for x in explodingtubes]
    

    '''
    sort exploding tubes
    loop through exploding tubes and find the largest difference between two tubes
    print the center of the largest difference
    '''
    explodingtubes.sort()
    maxInternalGap: int = 0
    for i in range(numexplodingtubes - 1):
        diff = explodingtubes[i + 1] - explodingtubes[i]
        if diff > maxInternalGap:
            maxInternalGap = diff
    
    startDist: int = explodingtubes[0]
    endDist: int = (numtubes - explodingtubes[-1]) - 1
    
    internalDist: int = int(maxInternalGap) // 2
    
    finalResult: int = max(startDist, endDist, internalDist)
    print(finalResult)
    
if __name__ == '__main__':
    main()