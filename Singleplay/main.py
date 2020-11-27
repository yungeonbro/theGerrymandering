import random
#1:democrat 0: republican

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

class Game:
    def __init__(self, n):

        self.turn = 0
        self.demPoint = 0
        self.repPoint = 0

        tmplist = list(range(4*n*n))
        democratsnumbers = random.sample(tmplist, 2*n*n - 2)
        #print(democratsnumbers)
        self.board = [[0 for i in range(2*n)] for j in range(2*n)]

        for i in democratsnumbers:
            self.board[i%(2*n)][int(i/(2*n))] = 1

        #print(self.board)

    def removeVoters(self, listOfVoters):
        if len(listOfVoters)!=5: # if not 5 area, return none 
            return None
        for i in listOfVoters:
            if self.board[i[0]][i[1]] == None:
                return None 
        if not isConnected(listOfVoters): #if the voters are not connected, return None
            return None

        x = [self.board[voter[0]][voter[1]] for voter in listOfVoters] # x is the list of votes that the voters took

        for voter in listOfVoters: # setting all the voters who voted to None
            self.board[voter[0]][voter[1]] = None

        demcnt = 0  # checking who won the election between 5 of voters
        repcnt = 0
        for i in x:
            if i == None:
                return None
            elif i == 0:
                repcnt += 1
            elif i == 1:
                demcnt += 1

        if demcnt + repcnt == 5: # if they don't add up to 5, there is some value such that they or not 0 or 1
            if demcnt > repcnt: # did democrats win??
                self.demPoint += 1
            else: #republicans win
                self.repPoint += 1
        else: #they dont add up to 5
            return None

        return 0 #not returning None



