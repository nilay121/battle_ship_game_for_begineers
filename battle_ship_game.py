###############################################################################################################
###############################################################################################################
###############################################################################################################
#BATTLESHIP GAME DEVELOPED BY NILAY


from random import randint
print("LET'S PLAY BATTLESHIP BOOY!!")
name = input("Enter your name :- ")
guts_input = input(f"{name} , DO U HAVE THE GUTS :- \nTYPE YES OR NO\n")
if guts_input == "yes" or guts_input == "YES":
    print(f"WELCOME {name}  \nYOU HAVE FOUR CHANCES TO SINK THE SHIP ")
    for i in range(0, 5):
        print(5 * " 0 ")


    def ship_sinking_details():
        ship_row = randint(0,5)
        ship_column = randint(0,5)
        return ship_row,ship_column

    def ship_user_input():
        user_ship_row = input("Guess Row :- ")
        user_ship_column = input("Guess Row :- ")
        return user_ship_row , user_ship_column


    def user_data():
        obtained = ship_sinking_details()
        ship_row_initial = obtained[0]
        ship_column_initial = obtained[1]
        for i in range(4, 1,-1):
            user_obtained = ship_user_input()
            user_ship_row = user_obtained[0]
            user_ship_column = user_obtained[1]
            if int(user_ship_column) == ship_column_initial and int(user_ship_row) == ship_row_initial:
                print("YAYYYYY!!!! CONGOOO , U SANK THE SHIP ")
                break
            else:
                print("Wrong Guess")
                print(f"You have {i} chances left ")
                continue
    user_data()
else:
    print(f"{name} you may leave!!")




