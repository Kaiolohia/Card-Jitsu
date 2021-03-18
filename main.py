import random
selfhand = []
enemyhand = []
deck = []
selfBank = []
enemyBank = []
class Card:
  def __init__(self, givenColor, givenElement, givenValue):
    color = ['red', 'orange', 'yellow','green', 
    'blue', 'purple']
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
for value in range(2,13):
  for color in range(6):
    for element in range(3):
       newCard = Card(color, element, value)
       deck.append(newCard.getCard())

class deal:
  def dealNewHandToSelf():
    for index in range(5):
        deckindex = random.randint(0, len(deck))
        selfhand.append(deck[deckindex])
        deck.pop(deckindex)
    return selfhand
  def dealNewHandToEnemy():
    for index in range(5):
        deckindex = random.randint(0, len(deck))
        enemyhand.append(deck[deckindex])
        deck.pop(deckindex)
    return enemyhand
  
  def dealOneCardToSelf():
    deckindex = random.randint(0, len(deck))
    selfhand.append( deck[deckindex])
    deck.pop(deckindex)
    return selfhand

  def dealOneCardToEnemy():
    deckindex = random.randint(0, len(deck))
    enemyhand.append( deck[deckindex])
    deck.pop(deckindex)
    return enemyhand

class ui:
  def whatIsMyHand():
    print('You have a '+ str(selfhand[0][0]) + ' ' + str(selfhand[0][1]) + ' with a value of ' + str(selfhand[0][2]) + ', a ' + str(selfhand[1][0]) + ' ' + str(selfhand[1][1]) + ' with a value of ' + str(selfhand[1][2]) + ', a ' + str(selfhand[2][0]) + ' ' + str(selfhand[2][1]) + ' with a value of ' + str(selfhand[2][2]) + ', a ' + str(selfhand[3][0]) + ' ' + str(selfhand[3][1]) + ' with a value of ' + str(selfhand[3][2]) + ',and a ' + str(selfhand[4][0]) + ' ' + str(selfhand[4][1]) + ' with a value of ' + str(selfhand[4][2]))
  def cardInfoToString(card):
    return 'a '+ str(card[0]) + ' ' + str(card[1]) + ' '  + str(card[2])
  def whatsInDaBank():
    if len(selfBank) == 0:
      print('You have no cards in the bank.')
    else:
      print('In the bank you have..')
      for x in range(len(selfBank)):
        print(ui.cardInfoToString(selfBank[x]))

def game():
    activeGame = False
    readyOrNot = input('Would you like to play Card Jitsu? Y/N: ').lower()
    if readyOrNot == 'y':
      activeGame = True
      deal.dealNewHandToSelf()
      deal.dealNewHandToEnemy()
      while activeGame == True:
        ui.whatIsMyHand()
        ui.whatsInDaBank()
        playedCard = int(input('Use card 1, 2, 3, 4, or 5:'))
        EnemyCardPlayed = random.randint(0,4)
        print('\nYou '+ roundWinner(playedCard,EnemyCardPlayed) + ' this round to ' + ui.cardInfoToString(enemyhand[EnemyCardPlayed]))
        bankUpdate(roundWinner(playedCard,EnemyCardPlayed),selfhand[playedCard-1],enemyhand[EnemyCardPlayed])
        useCard(playedCard - 1, 'self')
        useCard(EnemyCardPlayed,'enemy')
        print('\n')
        if didIWinYet(enemyBank) == True:
          activeGame = False
          print('You Lost\nThese are the cards your opponet had:')
          for x in range(len(enemyBank)):
            print(ui.cardInfoToString(enemyBank[x]))
        if didIWinYet(selfBank) == True:
          activeGame = False
          print('You won with these cards: ')
          for x in range(len(selfBank)):
            print(ui.cardInfoToString(selfBank[x]))
    else:
      print('Maybe another time...')

def useCard(index, who):
  if who == 'self':
    deal.dealOneCardToSelf()
    return selfhand.pop(index)
  elif who == 'enemy':
    deal.dealOneCardToEnemy()
    return enemyhand.pop(index)
  else:
    print('spelt input wrong... dumbass')

def roundWinner(playedcard,enemyCard):
  currentSelfCard = selfhand[playedcard - 1]
  
  currentEnemyCard = enemyhand[enemyCard]
  if typeWinCons(currentSelfCard, currentEnemyCard):
    return 'Won'
  if typeWinCons(currentEnemyCard, currentSelfCard):
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
  Fire = False
  Water = False
  Snow = False
  for x in range(len(bank)):
    if bank[x][1] == "Fire":
      Fire = True
  for x in range(len(bank)):
    if bank[x][1] == "Water":
      Water = True
  for x in range(len(bank)):
    if bank[x][1] == "Snow":
      Snow = True
  if Fire == True and Water == True and Snow == True:
    return True

game()