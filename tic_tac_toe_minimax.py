# Initializing empty board 
board = [
            ["-","-","-"], 
            ["-","-","-"],
            ["-","-","-"]
        ] 

ai_sign = None
player_sign = None
value_dict = {}

def choice_input():
    """ This method gives a choice to player1 to select sing whether "X" or "O" """
    while True:
        choice = input("Enter your choice 'X' or 'O': ")
        choice = choice.strip()
        if choice == "X" or choice == "O":
            global player_sign
            global ai_sign
            player_sign = choice
            if player_sign == "X":
                ai_sign = "O"
            else:
                ai_sign = "X"
            global value_dict
            value_dict = {
                player_sign: -1,
                ai_sign: 1,
                "tie": 0
            }
            break
        else:
            print("Please enter valied choice x or o")

def print_board_state(board):
    """
        prints the current snapshot of the board to the console 
        
        Parameter:
            board - a nested list which is the current board
    """
    for row in board:
        print(row[0],row[1],row[2])


def winner(board):
    """
        Determines the winner of the current board or if it is Still not  clear who will win

        Parameter:
            board - a nested list which is the current board

        Return:
            sing of winner from board index if any winner otherwise
            return "continue" if board is empty otherwise
            return "tie" if there is no winner and board is filled
    """
    # Check for horizontal win
    for i in range(len(board)):
        if board[i][0] != "-" and board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]

    # Check for vertical 
    for i in range(len(board[0])):
        if board[0][i] != "-" and board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]

    # Check for diagonal 
    if board[0][0] != "-" and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]

    if board[2][0] != "-" and board[2][0] == board[1][1] == board[0][2]:
        return board[2][0]

    # Check for empty cells for continue game
    for row in board:
        for cell in row:
            if cell == "-":
                return "continue"

    return "tie"


def minimax(board, is_this_AIs_turn):
    """
        Implementation of the minimax algorithm.

        parameters:
            board: a nested list which is the current board
            is_this_AIs_turn: a boolean which is true if AI is the current Player

        return:
            the value of the current score
    """
    winner_player = winner(board)

    #if we reached the end of the tree
    if winner_player != "continue":
        return value_dict[winner_player]
    
    #this is AIs turn 
    if is_this_AIs_turn:
        score = - 2    # anything smaller than min score
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "-":
                    board[i][j] = ai_sign
                    curr_score = minimax(board, False) 
                    board[i][j] = "-"
                    score = max(score, curr_score) # assign maximum score b/w current score and new score
        return score
    else:
        # user turn 
        score = 2 
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "-":
                    board[i][j] = player_sign
                    curr_score = minimax(board, True)
                    board[i][j] = "-"
                    score = min(score, curr_score)
        return score

                

def ais_move(board):
    """
        Check for the next move of the AI
        parameter:
             board:  a nested list which is the current board

        Return:
            array with 2 items representing the coordinates of the indexs

    """
    score = - 2               
    x = -1                   
    y = -1                    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "-":
                board[i][j] = ai_sign
                curr_score = minimax(board,False)
                board[i][j] = "-"
                if curr_score > score:
                    score = curr_score
                    x = i 
                    y = j
    return [x, y]

def game(board):
    """
        the main function of the program which run the game.

        Parameter:
             board:  a nested list which is the current board
    """
    print("Welcome to tic tac toe")
    choice_input()
    print_board_state(board)

    while winner(board) == "continue":
        location = input("Enter space seperated row[0-2] and column[0-2] no (0-indexed) of the cell you want to choose: ")
        location = location.strip()
        while True:
            try:
                space_pos = location.find(" ")
                x = int(location[ : space_pos])
                y = int(location[space_pos + 1 : ])
        
                #if player makes an illegal move
                if board[x][y] != "-" or space_pos == -1:
                    location = input("Please enter valid input for example '1 2'. The entered cell should be empty: ")
                    continue

                board[x][y] = player_sign
                break

            except ValueError as e:
                location = input("Please enter valid input only digit for example '1 2'. : ")
                location = location.strip()
            
            #if the player enters wrong or out of bounds index location
            except:
                location = input("Please enter valid input for example '1 2'. Also, the entered cell should be empty: ")
                location = location.strip()

        print("")
        print("After your Move-")
        print_board_state(board)

        #checking if the game has ended after the player's move
        if winner(board) == player_sign: 
            print("Congratulations! you win the game")
            break

        elif winner(board) == ai_sign: 
            print("Computer win the game !")
            break

        elif winner(board) == "tie": 
            print("Game has tie !")
            break

        # AI playing it's move
        AIs_turn = ais_move(board)
        x = AIs_turn[0]
        y = AIs_turn[1]
        board[x][y] = ai_sign

        print("After Computer Move-")
        print_board_state(board)

        if winner(board) == player_sign: 
            print("Congratulations! you win the game")
            break

        elif winner(board) == ai_sign: 
            print("Computer win the game !")
            break

        elif winner(board) == "tie": 
            print("Game has tie !")
            break
            
if __name__ == '__main__':
    game(board)

