tic_tac = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

dict_player1 = {}
dict_player2 = {}

print ("Welcome to the tic tac toe game! Quick rules: each player choose if he wants to play as 'X' or 'O'. The one who get three symbols in a row is a winner. Good luck!")

def display_board():
        print (tic_tac[0])
        print (tic_tac[1])
        print (tic_tac [2])
display_board()

def player_input ():
        dict_player1 ["position"] = {"row" : ' ', "column" : ' '}
        dict_player1 ["position"]["row"] = [int(input("Choose a position of your symbol (write the number of row for 0 to 2): " ))]
        dict_player1 ["position"]["column"] = [int(input("Choose a position of your symbol (write the number of column for 0 to 2): " ))]
        
        != ' ', 

     
        #for value in dict_player1["position"].values():
               #if 1 <= value <=3:
player_input ()