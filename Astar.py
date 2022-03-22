def AstarAlgo(startNode , stopNode):
    openSet=set(startNode)
    closedSet=set()
    parent={}
    g={}
    parent[startNode]=startNode
    g[startNode]=0
    
    while len(openSet) > 0:
        n=None
        
        for v in openSet:
            if n==None or g[v]+heur(v) < g[n]+heur(n):
                n=v
        
        if n==stopNode or graphNodes[n]==None:
            pass
        else:
            for (m,weights) in getNeighbors(n):
                if m not in openSet and m not in closedSet:
                    openSet.add(m)
                    parent[m]=n
                    g[m]=g[n]+weight
                else:
                    if  g[m] > g[n]+weight  :
                        g[m]=g[n]+weight
                        
                        if m in closedSet:
                            closedSet.remove(m)
                            openSet.add(m)
                        
    
        if n==None:
            print("Path does not exist")
            return None
    
        if n==stopNode:
            path=[]
            while parent[n]!=n:
                path.append(n)
                n=parent[n]
            path.append(startNode)
            path.reverse()
            print('Path found: {}'.format(path))
            return path
        
        openSet.remove(n)
        closedSet.add(n)

    print('Path does not exist!')
    return None

def getNeighbors(v):
    if v in graphNodes:
        return graphNodes[v]
    else:
        return None
    
def heur(n):
    hValue={
        'A': 10,
        'B': 8,
        'C': 5,
        'D': 7,
        'E': 3,
        'F': 6,
        'G': 5,
        'H': 3,
        'I': 1,
        'J': 0
    }
    return hValue[n]

graphNodes={
    
    'A':[('B',6),('F',3)],
    'B': [('C', 3), ('D', 2)],
    'C': [('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 8)],
    'E': [('I', 5), ('J', 5)],
    'F': [('G', 1),('H', 7)] ,
    'G': [('I', 3)],
    'H': [('I', 2)],
    'I': [('E', 5), ('J', 3)],
}

AstarAlgo('A','J')
