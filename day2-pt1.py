playslist = []

def played(p):
    
    playslist.append(calcpoints(p))

    lastone = False
    while lastone == False:
        p = input()
        #print(p)
        if p != "":
            playslist.append(calcpoints(p))
        else:
            lastone = True

    return True

def calcpoints(versus):
    vs = []
    vs = versus.split()
    player1 = ""
    player2 = ""
    points = 0

    match vs[0]:
        case "A":
            player1 = "R"
        case "B":
            player1 = "P"
        case "C":
            player1 = "S"

    match vs[1]:
        case "X":
            player2 = "R"
            points = points + 1
        case "Y":
            player2 = "P"
            points = points + 2
        case "Z":
            player2 = "S"
            points = points + 3

    #print(vs)
    #print(player1+" "+player2)

    if (player1 == player2):
        points = points + 3
    elif (player2 == "R" and player1 == "S"):
        points = points + 6
    elif (player2 == "S" and player1 == "P"):
        points = points + 6
    elif (player2 == "P" and player1 == "R"):
        points = points + 6



    return points

def totalscore():
    return sum(playslist)

def main():
    
    print("Advent day 2")
    print("Enter the list of games, enter nothing to pass")

    play = ""
    score = 0
    play = input()
    #print(play)
    if play != "":
        played(play)
    
    score = totalscore()

    print(score)


    print("The total score is "+str(score))

    print("End of the program")

if __name__ == "__main__":
    main()
