import random
# Define list of options for computer to choose from
playlist = ["R", "P", "S"]
# initialise userplay and computerplay to get while loop rolling
userplay = "x"
computerplay = userplay.upper()
while userplay.upper() == computerplay:  # Tie condition ensures the loop only continues if it's a tie
    userplay = input("Please pick your play: R, P, or S ")
    # compensate for upper or lowercase
    if userplay.upper() != "R" and userplay.upper() != "P" and userplay.upper() != "S":
        print("Invalid entry, please try again")
    else:
        computerplay = random.choice(playlist)
        # print players' play as required
        print(f"Player ({userplay}), CPU({computerplay})")
        # set winning criteria
    if (userplay.upper() == "R" and computerplay == "S") or (userplay.upper() == "P" and computerplay == "R") or (userplay.upper() == "S" and computerplay == "P"):
        print("YOU WIN!!!")
        # set tie criteria
    elif userplay.upper() == computerplay:
        print("It's a tie")
        # set losing criteria
    elif (userplay.upper() == "S" and computerplay == "R") or (userplay.upper() == "R" and computerplay == "P") or (userplay.upper() == "P" and computerplay == "S"):
        print("COMPUTER WINS!!!")
        # catch all other lose ends in a try again bucket
    else:
        print("Try again")
