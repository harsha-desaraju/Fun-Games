import os 
import time
import platform

# Needed functions

def clear_screen():
    os_name = platform.system()
    if os_name == "Windows":
        os.system('cls')
    elif os_name == "Linux":
        os.system("clear") 

def animation():
    str1 = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    str2 = ""
    for i in range(60):
        str2 = str2 + " "
        clear_screen()
        print(str1+str2+"Welcome to the game of tic-tac-toe!")
        time.sleep(0.005)

def print_board():
    #row ,col = tup
    for i in range(1,4):
        print("   |   |   ")
        for j in range(1,4):
            if (i,j) in moves_done:
                sym = move_done_by[(i,j)]
            #if i==row and j==col:
                if j==1:
                    print(" "+sym+" ",end="")
                elif j==2:
                    print("| "+sym+" |",end="")
                else:
                    print(" "+sym+" ")
            else:
                if j==1:
                    print("   ",end="")
                elif j==2:
                    print("|   |",end="")
                else:
                    print("   ")
                
        if i!=3:
            print("___|___|___")
        else:
            print("   |   |   ")
            
def game_won(lst):
    for t in win_pos:
        if (t[0] in lst) and (t[1] in lst) and (t[2] in lst):
            return True
    return False

# End of definitions of needed functions.

while 1:

    # Required data structures
    
    valid_moves = [1,2,3,4,5,6,7,8,9]

    pos = {1:(1,1),
           2:(1,2),
           3:(1,3),
           4:(2,1),
           5:(2,2),
           6:(2,3),
           7:(3,1),
           8:(3,2),
           9:(3,3)}

    moves_done = []
    move_done_by = {}

    win_pos = [(1,2,3),(4,5,6),(7,8,9),
               (1,4,7),(2,5,8),(3,6,9),
               (1,5,9),(3,5,7)]

    X_moves = []
    O_moves = []

    # Execution starts here...

    clear_screen()
    animation()
    clear_screen()
    print("\t\t\t\t\t\t\t\t Welcome to the of game Tic tac toe! \t\t\t\t")
    clear_screen()
    #print("Enter the name of player 1")
    player1 = input("Enter the name of player 1\n")
    player2 = input("Enter the name of player 2\n")

    fst_chance = input("Who's playing first?\n")
    while 1:
        if fst_chance==player1 or fst_chance==player2:
            if fst_chance==player1:
                sec_chance=player2
            else:
                sec_chance=player1
            break
        else:
            print("Enter a valid name. Name of 1st or 2nd player")
            fst_chance = input("Who's playing first?\n")
            
    print("Which symbol would you like to choose ",fst_chance,"?\n")
    symbol = input("Enter X or O\n")
    while 1:
        if symbol=="X" or symbol=="O":
            break
        else:
            print("Enter a valid string. X/O")
            symbol = input("Enter X or O\n")
    clear_screen()
    print("We are good to go.Let's start....\n")
    
    
    # ..............Start.............
    
    if symbol == "X":
        i=0
        Max=8
    elif symbol == "O":
        i=1
        Max=9
    won=0 # vairable to tell if game is won by any.
    while i<=Max:
        if i%2==0:
            num = int(input("It's X's chance.Enter the position of box. -1 to undo\n"))
        else:
            num = int(input("It's O's chance.Enter the position of box. -1 to undo\n"))
        if num==-1:
            if len(moves_done) > 0:
                temp = moves_done[-1]
                moves_done.pop(-1)
                del move_done_by[temp]
                print("Okay.Your previous moved will be cancelled.Enter again\n")
                i=i-1
            else:
                print("You did not make any move yet...")
        elif num in valid_moves:
            if pos[num] in moves_done:
                print("This position is already occupied")
            else:
                i+=1
                moves_done.append(pos[num])
                clear_screen()
                if i%2==0:
                    move_done_by[pos[num]]="O"
                    O_moves.append(num)
                    print_board()
                    if game_won(O_moves):
                        won=1
                        if symbol=="O":
                            print("The game is won by ",fst_chance,"!\n")
                        else:
                            print("The game is won by ",sec_chance,"!\n")
                        break
                else:
                    move_done_by[pos[num]]="X"
                    X_moves.append(num)
                    print_board()
                    if game_won(X_moves):
                        won=1
                        if symbol=="X":
                            print("The game is won by ",fst_chance,"!\n")
                        else:
                            print("The game is won by ",sec_chance,"!\n")
                        break
                    
        else:
            print("Enter a valid position number\n")
               
    
    if won==0:
        print("The game is a draw!\n")
        
    print("Would you like to play again?")
    string = input('Enter yes or no\n')
    while 1:
        if string == "yes" or string == "no":
            break
        else:
            print("Enter valid string-yes/no")
            string = input('Enter yes or no\n')

    if string == "no":
        break
        

    
