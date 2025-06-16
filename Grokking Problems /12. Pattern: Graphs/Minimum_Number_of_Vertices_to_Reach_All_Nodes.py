def findSmallestSetOfVertices(n, edges):
    incomingEgdes = [0 for i in range(n)]

    for src,des in edges:
        incomingEgdes[des] += 1
    
    res = []
    for i in range(len(incomingEgdes)):
        if incomingEgdes[i] == 0:
            res.append(i)
    
    return res