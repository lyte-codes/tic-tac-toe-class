class UI:
    def displayBoard(self, boardState):
        pass
    def getInput(self):
        return int(0)
    def displayWinX(self):
        pass
    def displayWinO(self):
        pass
    def displayDraw(self):
        pass

class TicTacToe:
    # 0 is nobody, 1 is X, 2 is O
    state = []
    ui = UI()
    def __init__(self, ui):
        self.UI = ui
        self.state = [[0,0,0, 0,0,0, 0,0,0], 1, 0]
    
    def move(self, move):
        if self.state[0][move] == 0:
            self.state[0][move] = self.state[1]
        else:
            return -1
        if self.state[1] == 1:
            self.state[1] = 2
        else:
            self.state[1] = 1
        return 0
    
    def step(self):
        move = -1
        while move == -1:
            move = self.move(self.UI.getInput())
        self.printBoard()
        winCheck = self.winCheck()
        if winCheck == 1:
            self.UI.displayWinX()
            self.state[2] = 1
        elif winCheck == 2:
            self.UI.displayWinO()
            self.state[2] = 2
        elif winCheck == 3:
            self.UI.displayDraw()
            self.state[2] = 3

    def winCheck(self):
        winPatterns = [
            [0,1,2],  # horizontal
            [3,4,5],
            [6,7,8],
            [0,3,6],  # vertical
            [1,4,7],
            [2,5,8],
            [0,4,8],  # diagonal
            [6,4,2],
        ]
        
        unwinnablePatterns = 0
        for pattern in winPatterns:
            currentPatternStatus = [
                self.state[0][pattern[0]],
                self.state[0][pattern[1]],
                self.state[0][pattern[2]]
            ]

            if (1 in currentPatternStatus) and (2 in currentPatternStatus):
                unwinnablePatterns += 1
        if unwinnablePatterns == len(winPatterns):
            return 3

        x_indices = [i for i, x in enumerate(self.state[0]) if x == 1]
        o_indices = [i for i, x in enumerate(self.state[0]) if x == 1]

        for combo in winPatterns:
            if all(pos in x_indices for pos in combo):
                return 1
            
        for combo in winPatterns:
            if all(pos in o_indices for pos in combo):
                return 2

    def printBoard(self):
        self.UI.displayBoard(self.state)