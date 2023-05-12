def elfentry(nc):
    totalcalories = int(nc)
    lastone = False
    while lastone == False:
        newcalorie = input()
        if newcalorie != "":
            totalcalories = totalcalories + int(newcalorie)
        else:
            lastone = True
    return totalcalories




def main():
    elflist = []
    print("Advent day 1 - Calories count by Elf")
    print("Enter the list of calories of an Elf, enter nothing to pass")
    theend = False
    while theend == False:
        nc = ""
        nc = input()
        if nc != "":
            elflist.append(elfentry(nc))
        else:
            theend = True
    
    print(elflist)

    max = 0
    pos = 0

    for p in (range(len(elflist))):
        if elflist[p] > max:
            max = elflist[p]
            pos = p

    print("The elf with the most calories is number "+str(pos+1)+" with "+str(max)+" total calories")

    print("End of the program")

if __name__ == "__main__":
    main()
