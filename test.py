map = [[0,1],[1,0], [-1,0],[0,-1]]
def isNear(twoPoints):
    for i in map:
        if (twoPoints[0][0] + i[0] == twoPoints[1][0]) and (twoPoints[0][1] + i[1] == twoPoints[1][1]):
            return True
    return False

def isConnected(listOfPoints):
    selected = [True, False, False, False, False]
    for _ in range(5):
        for i in range(5):
            if selected[i]:
                for point in range(5):
                    if point != i:
                        if isNear([listOfPoints[point], listOfPoints[i]]):
                            selected[point] = True
    if selected == [True, True, True, True, True]:
        return True
    return False

