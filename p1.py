import p1_random as p1

rng = p1.P1Random()
card = 0
x = 0
tie = 0
DWin = 0
PWin = 0
dealertotal = 0


def calcCard(num):
    if num >= 2 and num <= 10:
        return num
    elif num == 1:
        return "ACE"
    elif num == 11:
        return "JACK"
    elif num == 12:
        return "QUEEN"
    elif num == 13:
        return "KING"


def checkTotal(added):
    global total
    if added >= 10:
        added = 10
    total += added
    return total


def showStats():
    print(f"Number of Player wins: {PWin}")
    print(f"Number of Dealer wins: {DWin}")
    print(f"Number of tie games: {tie}")
    print(f"Total # of games played is: {numGame}")
    print(f"Percentage of Player wins: {round(((PWin / numGame) * 100), 1)}%")


numGame = 0

while x != 1:
    print(f'START GAME #{numGame + 1}')
    total = 0
    randy = (rng.next_int(13) + 1)
    print(f"Your card is a {calcCard(randy)}!")
    print(f"Your hand is: {checkTotal(randy)}\n")

    while True:
        print("1. Get another card")
        print("2. Hold hand")
        print("3. Print statistics")
        print("4. Exit\n")
        response = int(input(f"Choose an option: \n"))
        if response == 1:
            randy = (rng.next_int(13) + 1)
            print(f"Your card is a {calcCard(randy)}!")
            print(f"Your hand is: {checkTotal(randy)}")
            if total == 21:
                print("BLACKJACK! You win!\n")
                numGame = numGame + 1
                PWin += 1
                break
            elif total > 21:
                print("You exceeded 21! You lose.\n")
                numGame = numGame + 1
                DWin += 1
                break
            else:
                continue
        elif response == 2:
            dealertotal = (rng.next_int(11) + 16)
            print(f"Dealer's hand: {dealertotal}")
            print(f"Your hand is: {total}")
            if (dealertotal > total and dealertotal <= 21):
                print("Dealer wins!\n")
                numGame = numGame + 1
                DWin += 1
                break
            elif dealertotal > 21:
                print("You win!")
                numGame = numGame + 1
                PWin += 1
                break
            elif dealertotal == total:
                print("It's a tie! No one wins!")
                numGame = numGame + 1
                tie += 1
                break
            elif total > dealertotal and total <= 21:
                print("You win!")
                numGame = numGame + 1
                PWin += 1
                break
        elif response == 3:
            showStats()
            continue
        elif response == 4:
            x = 1
            break
        else:
            print("Invalid input!")
            print("Please enter an integer value between 1 and 4.")
            continue