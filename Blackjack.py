import Cards, random, copy

gameDeck = copy.copy(Cards.deck)
playerHand = []
dealerHand = []

#Introducing game and decision of playing as a dealer or player
def intro():
    startAmount = 100
    print('Welcome to the Exam Blackjack game!')
    print('First of all, would you like to play as a dealer or a player? Type quit if you\'d like to leave')
    dealerOrPlayer = input("--> ")
    if (dealerOrPlayer == 'dealer'):
        dealerGame(startAmount)
    elif (dealerOrPlayer == 'player'):
        startGame(startAmount)
    elif (dealerOrPlayer == 'quit'):
        pass
    elif (dealerOrPlayer != 'dealer' or dealerOrPlayer != 'player' or dealerOrPlayer != 'quit'):
        print('Unknown command. Try again')
        intro()
    return dealerOrPlayer

#Playing the game as a player
def startGame(startAmount):
    gameDeck = copy.copy(Cards.deck)
    print('You have ' + str(startAmount) + ' chips to bet with')
    bet = input('How many chips would you like to bet? ')
    try:
        int(bet)
    except ValueError:
        print("You need to enter a number try again")
        startGame(startAmount)
    if (int(bet) > startAmount):
        print('You can\'t afford that. Try again')
        startGame(startAmount)
    if (int(bet) < 0):
        print('You can\'t do that! Try again')
        startGame(startAmount)
    if (int(bet) == 0):
        print('You need to bet something! Try again!')
        startGame(startAmount)
    print('You have placed a bet of ' + str(bet) + ' chips')
    
    del playerHand[:]
    del dealerHand[:]
    playerHand.append(Cards.get_card(gameDeck))
    print('Your starting card is ' + playerHand[0].name)
    print('Your starting score is ' + str(Cards.checkAce(playerHand)))
    keepPlaying(startAmount, bet)

def keepPlaying(startAmount, bet):
    playerScore = 0
    playOn = input('Would you like another card? type \'draw\' if you\'d like another card or \'stay\' to stay: ')
    while playOn == 'draw': 
        playerHand.append(Cards.get_card(gameDeck))
        playerScore = Cards.checkAce(playerHand)
        if(playerScore >= 22):
            print('You drew a ' + str(playerHand[-1]) + ' which gives you the score of ' + str(playerScore))
            print('You\'ve gotten a score of over 21')
            print('___________________________________________')
            print('                 YOU LOSE!')
            print('___________________________________________')
            startAmount -= int(bet)
            playAgain(startAmount)
        print('You drew a ' + str(playerHand[-1]))
        print('Your score is now: ' + str(playerScore))
        playOn = input('Would you like another card? type \'draw\' if you\'d like another card or \'stay\' to stay: ')
        
    if(playOn == 'stay'):
        print('You stayed, the dealer will now play his hand')
        dealerHand.append(Cards.get_card(gameDeck))
        dealerHand.append(Cards.get_card(gameDeck))
        print("The dealer drew a " + dealerHand[0].name + " and a " + dealerHand[1].name)
        print('Which gives him a score of ' + str(Cards.checkAce(dealerHand)))
        dealerScore = Cards.checkAce(dealerHand)

        while dealerScore <= playerScore:
            dealerHand.append(Cards.get_card(gameDeck))
            dealerScore = Cards.checkAce(dealerHand)
            print('The dealer drew a ' + str(dealerHand[-1]))
        print('The dealer stayed on a score of ' + str(Cards.checkAce(dealerHand)))

        if(dealerScore > 21):
            print('___________________________________________')
            print('                 YOU WIN!')
            print('___________________________________________')
            startAmount += int(bet)

        elif(dealerScore >= playerScore):
            print('___________________________________________')
            print('                 YOU LOSE!')
            print('___________________________________________')
            startAmount -= int(bet)
        playAgain(startAmount)
    if(playOn != 'draw' or playOn != 'stay'):
        print('Unknown command entered. Try again!')
        keepPlaying(startAmount, bet)


    

def dealerGame(startAmount):
    print('___________________________________________')
    gameDeck = copy.copy(Cards.deck)
    print('Welcome to the dealers side of the table!')
    print('The player will now make his bet and draw his cards')

    print('The player has ' + str(startAmount) + ' chips to bet with')
    bet = random.randint(1, startAmount)
    
    print('The player has placed a bet of ' + str(bet) + ' chips')
    del playerHand[:]
    del dealerHand[:]
    playerHand.append(Cards.get_card(gameDeck))
    playerHand.append(Cards.get_card(gameDeck))

    print("The player drew a " + playerHand[0].name + " and a " + playerHand[1].name)
    print('Which gives him a score of ' + str(Cards.checkAce(playerHand)))
    playerScore = Cards.checkAce(playerHand)

    while playerScore < 16:
        playerHand.append(Cards.get_card(gameDeck))
        playerScore = Cards.checkAce(playerHand)
        print('The player drew a ' + str(playerHand[-1]))
    print('The player stayed on a score of ' + str(Cards.checkAce(playerHand)))
    if(playerScore >= 22):
        print('The player drew a ' + str(playerHand[-1]) + ' which gives the player the score of ' + str(playerScore))
        print('The player has gotten a score of over 21')
        print('___________________________________________')
        print('                 YOU WIN!')
        print('___________________________________________')
        startAmount -= bet
        playAgain(startAmount)

    
    print('_________________________________________________')
    print('')


    dealerHand.append(Cards.get_card(gameDeck))
    Cards.checkAce(playerHand)
    print('You will now draw your first card, which is ' + str(dealerHand[-1]))
    print('Your score is ' + str(Cards.checkAce(dealerHand)))
    keepPlayingDealer(startAmount, bet, playerScore)
    
def keepPlayingDealer(startAmount, bet, playerScore):
    playOn = input('Would you like another cards? type \'draw\' if you\'d like another card or \'stay\' to stay: ')
    while playOn == 'draw':
        dealerHand.append(Cards.get_card(gameDeck))
        dealerScore = Cards.checkAce(dealerHand)
        if(dealerScore >= 22):
            print('You drew a ' + str(dealerHand[-1]) + ' which gives you the score of ' + str(dealerScore))
            print('You\'ve gotten a score of over 21')
            print('___________________________________________')
            print('                 YOU LOSE!')
            print('___________________________________________')
            startAmount += bet
            playAgain(startAmount)
        print('You drew a ' + str(dealerHand[-1]))
        print('Your score is now: ' + str(dealerScore))
        playOn = input('Would you like another card? type \'draw\' if you\'d like another card or \'stay\' to stay: ')
    
    if(playOn == 'stay'):
        print('You stayed on ' + str(Cards.checkAce(dealerHand)))

        if(Cards.checkAce(dealerHand) > 21):
            print('___________________________________________')
            print('                 YOU LOSE!')
            print('___________________________________________')
            startAmount += bet

        elif (Cards.checkAce(playerHand) > Cards.checkAce(dealerHand)):
            print('___________________________________________')
            print('                 YOU LOSE!')
            print('___________________________________________')
            startAmount += bet

        elif(Cards.checkAce(dealerHand) >= Cards.checkAce(playerHand)):
            print('___________________________________________')
            print('                 YOU WIN!')
            print('___________________________________________')
            startAmount -= bet
        playAgain(startAmount)
    if(playOn != 'draw' or playOn != 'stay'):
        print('Unknown command entered. Try again!')
        keepPlayingDealer(startAmount, bet, playerScore)

        

def playAgain(startAmount):
    if (startAmount == 0):
        print('You have ' + str(startAmount) + ' chips, and can therefore not play anymore.')
        print('___________________________________________')
        print('                 GAME OVER!')
        print('___________________________________________')
        exit()
    newGame = input('Would you like to play another game? y/n ')
    if(newGame == 'y'):
        playerOrDealer = input('Would you like to play as a player or a dealer? ')
        if (playerOrDealer == 'player'):
            startGame(startAmount)
        elif (playerOrDealer == 'dealer'):
            dealerGame(startAmount)
        elif (playerOrDealer != 'player' or playerOrDealer != 'dealer'):
            print('Unknown character. Try again')
            playAgain(startAmount)

    elif(newGame == 'n'):
        exit()
    elif(newGame != 'y' or newGame != 'n'):
        print('Unknown character. Try again')
        playAgain(startAmount)
    



if __name__ == "__main__":
    intro()