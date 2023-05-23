def nearlySimilarRectangles(sides):
    # Write your code here
    count = 0
    for i in range(0,len(sides)):
        a = float(sides [i][0])/float(sides [i][1])  
        for j in range(i+1, len(sides)):
            if a == float(sides [j][0])/float(sides[j][1]):
                count = count +1
    return count    
