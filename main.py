class TicTacToe:
    # 0 is nobody, 1 is X, 2 is O
    state = []
    def __init__(self):
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

    def getInput(self):
        while True:
            user_input = input("Enter your move: ")
            if (user_input in str(range(0,10))):
                return int(user_input)
            else:
                print("Invalid input.")
    
    def step(self):
        move = -1
        while move == -1:
            move = self.move(self.getInput())
        self.printBoard()
        if self.winCheck() == 1:
            print("X wins!")
            self.state[2] = 1
        elif self.winCheck() == 2:
            print("O wins!")
            self.state[2] = 2

    def winCheck(self):
        wins = [
            [0,1,2],  # horizontal
            [3,4,5],
            [6,7,8],
            [0,3,6],  # vertical
            [1,4,7],
            [2,5,8],
            [0,4,8],  # diagonal
            [6,4,2],
        ]

        x_indices = [i for i, x in enumerate(self.state[0]) if x == 1]
        o_indices = [i for i, x in enumerate(self.state[0]) if x == 1]

        for combo in wins:
            if all(pos in x_indices for pos in combo):
                return 1
            
        for combo in wins:
            if all(pos in o_indices for pos in combo):
                return 2

    def printBoard(self):
        print("\n-------")
        for j in range(0,3):
            print("|", end="")
            for i in range(0, 3):
                if self.state[0][i+(j*3)] == 1:
                    square = "X"
                elif self.state[0][i+(j*3)] == 2:
                    square = "O"
                else:
                    square = " "
                print(f"{square}|", end="")
            print("\n-------")
        print()

Game = TicTacToe()
while Game.state[2] == 0:
    Game.step()