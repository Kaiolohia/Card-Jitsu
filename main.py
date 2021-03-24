import random
from os import system, name
#YOU CAN EDIT THIS VAR AND NOT BREAK THINGS!!! 
#StringSetting1 gives complicated card information per card and is a paragraph of text per turn while
#stringSetting0 is a simple version
stringsetting = 0


deck = []
selfhand = []
enemyhand = []
selfBank = []
enemyBank = []


#this class deals with the data of an indivdual card
class Card:

  def __init__(self, givenColor, givenElement, givenValue):
    color = ['red', 'orange', 'yellow','green', 'blue', 'purple']
    element = ['Water', 'Fire', 'Snow']
    self.color = color[givenColor]
    self.element = element[givenElement]
    self.value = givenValue

  def getCard(self):
    returnThis = []
    returnThis.append(self.color)
    returnThis.append(self.element)
    returnThis.append(self.value)
    return returnThis

  def useCard(index, who):
    if who == 'self':
      deal.dealOneCardToSelf()
      return selfhand.pop(index)
    if who == 'enemy':
      deal.dealOneCardToEnemy()
      return enemyhand.pop(index)


#this class deals with everything about dealing cards along with the inital 5 cards and is called 
class deal:

  def dealNewHandToSelf():
    for index in range(5):
        deckindex = random.randint(0, len(deck)-1)
        selfhand.append(deck[deckindex])
        deck.pop(deckindex)
    return selfhand

  def dealNewHandToEnemy():
    for index in range(5):
        deckindex = random.randint(0, len(deck)-1)
        enemyhand.append(deck[deckindex])
        deck.pop(deckindex)
    return enemyhand
  
  def dealOneCardToSelf():
    deckindex = random.randint(0, len(deck)-1)
    selfhand.append( deck[deckindex])
    deck.pop(deckindex)
    return selfhand

  def dealOneCardToEnemy():
    deckindex = random.randint(0, len(deck)-1)
    enemyhand.append(deck[deckindex])
    deck.pop(deckindex)
    return enemyhand
#The user Interface class is called to print and process card data to strings
class ui:
  def whatIsMyHand():
    if stringsetting == 0:
      print('❰ Your Hand ❱\n| 1. ' + ui.simplecardformatter(selfhand[0]) + '\n| 2. ' + ui.simplecardformatter(selfhand[1]) + '\n| 3. ' + ui.simplecardformatter(selfhand[2]) + '\n| 4. ' + ui.simplecardformatter(selfhand[3]) + '\n| 5. ' + ui.simplecardformatter(selfhand[4]) + '\n―――――――――――――')
    if stringsetting == 1:
      print('--------------Your Hand--------------\n| 1. a '+ str(selfhand[0][0]) + ' ' + str(selfhand[0][1]) + ' with a value of ' + str(selfhand[0][2]) + ' ' + ui.symbols(selfhand[0][1]) + '\n| 2. a ' + str(selfhand[1][0]) + ' ' + str(selfhand[1][1]) + ' with a value of ' + str(selfhand[1][2]) + ' ' + ui.symbols(selfhand[1][1]) + '\n| 3. a ' + str(selfhand[2][0]) + ' ' + str(selfhand[2][1]) + ' with a value of ' + str(selfhand[2][2]) + ' ' + ui.symbols(selfhand[2][1]) + '\n| 4. a ' + str(selfhand[3][0]) + ' ' + str(selfhand[3][1]) + ' with a value of ' + str(selfhand[3][2]) + ' ' + ui.symbols(selfhand[3][1]) + '\n| 5. and a ' + str(selfhand[4][0]) + ' ' + str(selfhand[4][1]) + ' with a value of ' + str(selfhand[4][2]) + ' ' + ui.symbols(selfhand[0][1]) + '\n-------------------------------------')
  
  def cardInfoToString(card):
    return 'a '+ str(card[0]) + ' ' + str(card[1]) + ' '  + str(card[2])
  def whatsInDaBank():
    if len(selfBank) == 0:
      print('\nYou have no cards in the bank.\n')
    else:
      if stringsetting == 0:
        print('\n❰ Your Bank ❱')
        for x in range(len(selfBank)):
          print('| ' + str(x+1) + '. ' + ui.simplecardformatter(selfBank[x]))
        print('')
      else:
        print('\n❰ Your Bank ❱')
        for x in range(len(selfBank)):
          print('| ' + str(x+1) + '. ' + ui.cardInfoToString(selfBank[x]))
        print('')

  def simplecardformatter(card):
    color = ui.colors(card[0])
    symbol = ui.symbols(card[1])
    value = card[2]
    return str(color) + ' ' + str(symbol) + ' ' + str(value)
  def symbols(input):
    if input == 'Fire':
      return '🔥'
    if input == 'Snow':
      return '❆'
    if input == 'Water':
      return '💧'
    if input == 'Bank':
      return '𓍝'
  def colors(input):
    if input == 'red':
      return '🟥'
    if input == 'orange':
      return '🟧'
    if input == 'yellow':
      return '🟨'
    if input == 'green':
      return '🟩'
    if input == 'blue':
      return '🟦'
    if input == 'purple':
      return '🟪'

#the utilities class deals with the un organized functions required to make the game work such as win conditions and bank work.
class utils:

  def roundWinner(playedcard,enemyCard):
    currentSelfCard = selfhand[playedcard - 1]
    currentEnemyCard = enemyhand[enemyCard]
    if utils.typeWinCons(currentSelfCard, currentEnemyCard):
      return 'Won'
    if utils.typeWinCons(currentEnemyCard, currentSelfCard):
      return 'Lost'
    if currentSelfCard[2] == currentEnemyCard[2]:
      return 'Tied'
    if currentSelfCard[2] > currentEnemyCard[2]:
      return 'Won'
    return 'Lost'

  def typeWinCons(card1, card2): 
    if card1[1] == "Water" and card2[1] == "Fire" or card1[1] == "Fire" and card2[1] == "Snow" or card1[1] == "Snow" and card2[1] == "Water":
      return True

  def bankUpdate(roundwinner, selfcard, enemycard):
    if roundwinner == 'Won':
      selfBank.append(enemycard)
      return
    if roundwinner == 'Lost':
      enemyBank.append(selfcard)
      return
    return
  
  def didIWinYet(bank):
    #elements check
    Fire = False
    Water = False
    Snow = False
    FireColors = []
    WaterColors = []
    SnowColors = []
    for x in range(len(bank)):
      if bank[x][1] == "Fire":
        Fire = True
        FireColors.append(bank[x][0])
        FireColors = list(set(FireColors))
    for x in range(len(bank)):
      if bank[x][1] == "Water":
        Water = True
        WaterColors.append(bank[x][0])
        WaterColors = list(set(SnowColors))
    for x in range(len(bank)):
      if bank[x][1] == "Snow":
        Snow = True
        SnowColors.append(bank[x][0])
        SnowColors = list(set(SnowColors))
    if Fire == True and Water == True and Snow == True:
      return True
    if len(FireColors) == 3 or len(WaterColors) == 3 or len(SnowColors) == 3:
      return True
  
    
  def mainlogo():
    print('_________                  .___      ____.__  __                ')
    print('\_   ___ \_____ _______  __| _/     |    |__|/  |_  ________ __ ')
    print('/    \  \/\__  \\\\_  __ \/ __ |      |    |  \   __\/  ___/  |  \\')
    print('\     \____/ __ \|  | \/ /_/ |  /\__|    |  ||  |  \___ \|  |  /')
    print(' \______  (____  /__|  \____ |  \________|__||__| /____  >____/ ')
    print('        \/     \/           \/                         \/       ')
    print('Developed by Kai \nVersion: 0.2\nDisc: Trux#0001\n')

  def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

#this is the main game function that runs the entire thing. We use an input to start the game that way we can restart after the game is played or refuse to play if it is accidentally started.
def game(readyOrNot):
    activeGame = False
    deck.clear()
    selfhand.clear()
    enemyhand.clear()
    selfBank.clear()
    enemyBank.clear()
    for value in range(2,13):
      for color in range(6):
        for element in range(3):
          newCard = Card(color, element, value)
          deck.append(newCard.getCard())
    if readyOrNot == 'y':
      activeGame = True
      deal.dealNewHandToSelf()
      deal.dealNewHandToEnemy()
      utils.clear()
      utils.mainlogo()
      while activeGame == True:
        validInput = False
        ui.whatIsMyHand()
        ui.whatsInDaBank()
        while validInput == False:
          playedCard = int(input('Use card 1, 2, 3, 4, or 5:'))
          if playedCard <= 5 and playedCard >= 1:
            validInput = True
          else:
            print('Invalid Input\nPlease try again.')
        EnemyCardPlayed = random.randint(0,4)
        utils.clear()
        utils.mainlogo()
        print('\n▶ You '+ utils.roundWinner(playedCard,EnemyCardPlayed) + ' this round to ' + ui.cardInfoToString(enemyhand[EnemyCardPlayed]) +' ◀')
        utils.bankUpdate(utils.roundWinner(playedCard,EnemyCardPlayed),selfhand[playedCard-1],enemyhand[EnemyCardPlayed])
        Card.useCard(playedCard - 1, 'self')
        Card.useCard(EnemyCardPlayed,'enemy')
        print('\n')
        
        if utils.didIWinYet(enemyBank) == True:
          activeGame = False
          print('You Lost\nThese are the cards your opponet had:')
          if stringsetting == 0:
            for x in range(len(enemyBank)):
              print(ui.simplecardformatter(enemyBank[x]))
          else:
            for x in range(len(enemyBank)):
              print(ui.cardInfoToString(enemyBank[x]))
          game(input('\nWould you like to play again? Y/N: ').lower())
        if utils.didIWinYet(selfBank) == True:
          activeGame = False
          print('You won with these cards: ')
          if stringsetting == 0:
            for x in range(len(selfBank)):
              print(ui.simplecardformatter(selfBank[x]))
          else:
            for x in range(len(selfBank)):
              print(ui.cardInfoToString(selfBank[x]))
          game(input('\nWould you like to play again? Y/N: ').lower())
    else:
      print('Maybe another time...')
utils.mainlogo()
game(input('Would you like to play Card Jitsu? Y/N: ').lower())