import the_table
import the_players

#Start of main biz
table = the_table.Board()
player = the_players.Player()
userInput = ""

#Setup Loop
while(userInput != "quit" and player.availableCities != 0):
    table.printBoard()
    userInput = input(f"""
Select where you would like to build a city.
Enter the tile ID (top number) followed by position:
Ex. 4-TL would place a town on tile 4 in the top left.
                      
You have {str(player.availableCities)} left to place.
""")
    if(userInput != "quit"):
        table.gameLogic.buildTown(player, table, userInput)
#Main Game Loop
while(userInput != "quit"):
    table.printBoard()
    player.printPlayer()
    userInput = input("""
What would you like to do?
1. roll - Roll the dice and collect your resources
2. upgrade town - Upgrade a town you currently own to a city
3. quit - Exit the game
""")
    if(userInput == "roll"):
        table.gameLogic.rollDice(table, player)
    elif(userInput == 'upgrade town'):
        userInput = input("What town would you like to upgrade?")
        table.gameLogic.buildCity(player, table, userInput)
    else:
        print(f"Invalid input: {userInput}. Please try again.")

print("Thank you for playing!")

#print(
#f"""   {board.boardMap[0].corner[0]}{board.boardMap[0].side[0]*5}{board.boardMap[0].corner[1]}   
#  {board.boardMap[0].side[5]}{' '*7}{board.boardMap[0].side[1]}  
# {board.boardMap[0].side[5]}{' '*9}{board.boardMap[0].side[1]} 
#{board.boardMap[0].corner[5]}{' '*((11-len(board.boardMap[0].title))//2)}{board.boardMap[0].title}{' '*(((11-len(board.boardMap[0].title))//2)+((11-len(board.boardMap[0].title))%2))}{board.boardMap[0].corner[2]}
# {board.boardMap[0].side[4]}{' '*(4-(board.boardMap[0].id//10))}{board.boardMap[0].id}{' '*4}{board.boardMap[0].side[2]} 
# {board.boardMap[0].side[4]}{' '*7}{board.boardMap[0].side[2]}  
#   {board.boardMap[0].corner[4]}{board.boardMap[0].side[3]*5}{board.boardMap[0].corner[3]}   
#""")
#print(board.boardMap[0].id)
#print(board.boardMap[0].resource)
#print(board.boardMap[6].id)
#print(board.boardMap[6].resource)