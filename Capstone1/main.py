from random import choice
from time import sleep


# A black game that rolls dice and uses those values to add to the player or the houses
# total score, whichever reaches 21 or closest to it without busting wins
# Functions needed - Menu function, Roll function, Game status function , Main function
# and the rules function

# Intro Art function, opening for their game. It just displays a welcoming with ASCII Art

# This is a new test comment, I will commit this and attempt to push it to my repository

# Wow that actually wokred, this is a reply from github editing
# ill make a few intentional mistakes with typos helo haw aree yoi
def intro():
    print("\nWelcome to BlackJack!\n")
    print("                            _____           ")
    print("                    _____  |10 & |          ")
    print("            _____  |Q  ww| | o {)|          ")
    print("     _____ |J  ww| | o {(| |o o%%| _____    ")
    print("    |10 & || o {)| |o o%%| | |%%%||A _  |   ")
    print("    |& & &||o o% | | |%%%| |_%%%>|| ( ) |   ")
    print("    |& & &|| | % | |_%%%O|        |(_'_)|   ")
    print("    |& & &||__%%[|                |  |  |   ")
    print("    |___0I|                       |____V|   ")
    print()


def display_rules():
    print("===============================================")
    print("               Blackjack Rules                 ")
    print("===============================================")
    print("1. The goal of Blackjack is to beat the dealer's hand without going over 21.")
    print("2. Face cards are worth 10. Aces are worth 1 or 11, whichever makes a better hand.")
    print("3. Each player starts with two cards, and one of the dealer's cards is hidden until the end.")
    print("4. To 'Hit' is to ask for another card. To 'Stand' is to hold your total and end your turn.")
    print("5. If you go over 21 you bust, and the dealer wins regardless of the dealer's hand.")
    print("6. If you are dealt 21 from the start (Ace & 10), you got a Blackjack.")
    print("7. Dealer will hit until their cards total 17 or higher.")
    print("8. You can 'Double Down' on your hand, doubling your bet and receiving one more card.")
    print("9. You can 'Split' pairs into two separate hands, and play them independently.")
    print(
        "10. Insurance: If the dealer's up card is an Ace, you can take insurance, which pays 2:1 if the dealer has a "
        "Blackjack.")
    print("11. Surrender: Some casinos offer the option to surrender, forfeiting half of your bet.")
    print("===============================================")


def menu_choice():
    menuChoice = 0
    while menuChoice < 1 or menuChoice > 3:
        try:
            print("Choose from the following: ")
            menuChoice = int(input("1. - Play \n2. - See Rules.\n3. - Quit\n----> "))
            if menuChoice < 1 or menuChoice > 3:
                print("Please input a number, 1, 2, or 3.\n")
        except:
            print("Please input a number!\n")
    return menuChoice


def draw_card(hand):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    cardDrawn = choice(cards)
    hand.append(cardDrawn)
    return hand


def hit_or_pass(score, houseScore):
    choice = 0
    while choice != 1 and choice != 2:
        try:
            choice = int(input(
                f"=================\nYour Score: {score}\nHouse Score: {houseScore}\n=================\nWould you "
                f"like to hit again or stand?\n1] Hit\n2] stand\nHit again or stand: "))
            if choice != 1 and choice != 2:
                print("Please enter 1 or 2.\n")
        except:
            print("\nPlease pick a number!\n")

    return choice


def game_status(score, houseScore, playerHold, houseHold):
    gameStatus = False
    # instead of returning a bunch of parameters and complicating the code
    # I'll assign each possibility a number, when returned to main.py
    # the number will be used to reference the reason for the game ending

    # if player busts = 1, house busts = 2, player lose = 3, house lose = 4
    # So, 1 and 3 initiate the player losing events
    # And, 2 and 4 initiate the house losing events
    # returns 5 for a tie

    condition = 0
    if score > 21:
        condition = 1
    elif houseScore > 21:
        condition = 2
    elif playerHold and houseHold:
        if score < houseScore:
            condition = 3
        elif score > houseScore:
            condition = 4
        else:
            condition = 5
    else:
        gameStatus = True

    return gameStatus, condition


def can_house_draw(houseScore):
    if houseScore <= 16:
        return True
    else:
        return False


def main():
    programStatus = gameStatus = True
    playerWins = houseWins = 0

    while programStatus:
        # Display Intro
        intro()
        # Prompt user for their menu Choice
        choice = menu_choice()

        # beging the game loop
        if choice == 1:
            # Initialize the player card value and house card value, along with their hands
            playerHold = houseHold = False
            playerScore = houseScore = round = 0
            playerHand = []
            houseHand = []

            while gameStatus:
                if round == 0:
                    # By default, blackJack draws a card for the player and house
                    # Draw initial card for player and house and display it
                    playerHand = draw_card(playerHand)
                    houseHand = draw_card(houseHand)
                    # Gets total score value for each hand
                    playerScore = sum(playerHand)
                    houseScore = sum(houseHand)
                    print("\nInital set:")
                    print(
                        f"Your initial draw is {playerHand[round]}.Hand Value: {playerScore}"
                        f"\nHouse Initial Hand is {houseHand[round]}. Hand Value: {houseScore}.\n")
                else:
                    # Display intro to each round
                    sleep(1)
                    print("===========================================")
                    print(f"               Round {round + 1}             ")
                    print("===========================================\n\n")

                    print("***********************")
                    print(f"Your Hand: {playerHand}\nHouse Hand: {houseHand}")
                    print("***********************")

                    # gets the players choice
                    if not playerHold:
                        playerChoice = hit_or_pass(playerScore, houseScore)
                        if playerChoice == 1:
                            print("\nYou draw!")
                            playerHand = draw_card(playerHand)
                            print(f"Card Drew: {playerHand[-1]}")
                        else:
                            print("\nYou hold!")
                            playerHold = True

                    # checking if the house can draw (under card value condition)
                    if not houseHold:
                        HhouseMustDraw = can_house_draw(houseScore)
                        if HhouseMustDraw:
                            print("The house draws")
                            houseHand = draw_card(houseHand)
                        else:
                            print("The house stands")
                            houseHold = True

                    # Gets total score value for each hand
                    playerScore = sum(playerHand)
                    houseScore = sum(houseHand)

                    # Determine if either the player or house gets blackjack
                    # Doubles the wins of the winner, ends the game instantly upon blackjack
                    if playerScore == 21:
                        print("BLACKJACK!!!")
                        playerWins += 2
                        gameStatus = False
                        continue
                    elif houseScore == 21:
                        print("The house gets Blackjack\nYou lose!")
                        houseWins += 2
                        gameStatus = False
                        continue

                    gameStatus, condition = game_status(playerScore, houseScore, playerHold, houseHold)

                    # checks for Potential aces as 1's
                    for playerCard, houseCard in zip(playerHand, houseHand):
                        if condition == 1:
                            if playerCard == 11:
                                playerCard = 1
                                gameStatus = True
                                condition = 0
                        elif condition == 2:
                            if houseCard == 11:
                                houseCard = 1
                                gameStatus = True
                                condition = 0

                    # checks again after ace conversion
                    gameStatus, condition = game_status(playerScore, houseScore, playerHold, houseHold)

                    # if player busts = 1, house busts = 2, player lose = 3, house lose = 4
                    # So, 1 and 3 initiate the player losing events
                    # And, 2 and 4 initiate the house losing events
                    # returns 5 for a tie
                    if condition == 0:
                        pass
                    elif condition == 1:
                        print("You busted!\nHouse Wins!")
                        houseWins += 1
                    elif condition == 2:
                        print("The house busts!\nYOU WIN!")
                        playerWins += 1
                    elif condition == 3:
                        print(f"You win with a score of {playerScore}!\nCongratulations!")
                        playerWins += 1
                    elif condition == 4:
                        print("House wins!")
                        houseWins += 1
                    elif condition == 5:
                        print("It's a TIE! No winners")

                    if playerHold and houseHold:
                        gameStatus = False

                    if not gameStatus:
                        # display final hand and scores
                        print(
                            f"Your Hand: {playerHand}\nHandValue: {playerScore}\n==========================\nHouse "
                            f"Hand: {houseHand}\nHandValue: {houseScore}\n==========================")
                        sleep(1)
                        print()

                round += 1

        elif choice == 2:
            display_rules()

        else:
            programStatus = False
            print("Thank you for playing!\nGoodbye!")


main()
