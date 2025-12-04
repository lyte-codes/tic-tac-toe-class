import engine

class TerminalUI(engine.UI):
    def displayBoard(self, boardState):
        print("\n-------")
        for j in range(0,3):
            print("|", end="")
            for i in range(0, 3):
                if boardState[0][i+(j*3)] == 1:
                    square = "X"
                elif boardState[0][i+(j*3)] == 2:
                    square = "O"
                else:
                    square = " "
                print(f"{square}|", end="")
            print("\n-------")
        print()

    def displayDraw(self):
        print("Draw.")

    def displayWinX(self):
        print("X wins!")

    def displayWinO(self):
        print("O wins!")

    def getInput(self):
        while True:
            user_input = input("Enter your move: ")
            if (user_input in [str(item) for item in range(0, 10)]):
                return int(user_input)
            else:
                print("Invalid input.")

Game = engine.TicTacToe(ui=TerminalUI())
while Game.state[2] == 0:
    Game.step()