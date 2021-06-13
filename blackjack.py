from random import randint
from IPython.display import clear_output

deck=[11,2,3,4,5,6,7,8,9,10,10,10,10]

def card_picker():
  card=deck[randint(0,len(deck)-1)] # remember randint is including both end points
  return card

def keep_score(real_carddeck):
  carddeck=real_carddeck.copy()
  if (sum(carddeck) > 21) and (11 in carddeck):
        while sum(carddeck)>21:
            i=carddeck.index(11)
            carddeck[i]=1
            if 11 not in carddeck: # you will combe back in this loop if some greater than 21 and you dont want that
                break
  score=sum(carddeck)
  #print(score)
  #print(carddeck)
  #print(real_carddeck)
  return score

play='y'

while play=='y':
  clear_output()
  print('''
  .------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      `------'                           |__/           

  ''')
  user_deck=[]
  computer_deck=[]
  print('welcome to blackjack. the computer deals : ')
  for i in range(0,2):
    user_deck.append(card_picker())
    computer_deck.append(card_picker())
  
  print('your hand is : ')
  print(user_deck)
  print(f'your count is : {keep_score(user_deck)}')
  print('the computers first card is : ')
  print(computer_deck[0])
  play='hit'
  dealer_cycle='yes' # for breaking purposes only
  while play=='hit':
  
    play=input('hit or stand?')
    if play=='stand':
      break
    else:
      user_deck.append(card_picker())
      print(f'user deck : {user_deck}')
      if keep_score(user_deck)>21:
        print(f'user deck went over 21 : {user_deck}')
        print('Bust! you lose')
        dealer_cycle='no'
        break
      elif keep_score(user_deck)==21:
        print(f'black jack : {user_deck}')
        break
      else:
        continue
  #now for the dealers appending cycle
  
  if dealer_cycle=='yes':
      while keep_score(computer_deck)<17:
        computer_deck.append(card_picker())
  
      #now for the winner
      print(f'your deck : {user_deck}')
      print(f'your final score : {keep_score(user_deck)}')
      print(f'computer deck : {computer_deck}')  
      print(f'computer final score : {keep_score(computer_deck)}')

      if keep_score(computer_deck)>21:
        print('you win')
      elif keep_score(user_deck)>keep_score(computer_deck):
        print('you win')
      elif keep_score(user_deck)<keep_score(computer_deck):
        print('computer wins')
      elif keep_score(user_deck)<keep_score(computer_deck):
        print('Push!')
      play=input('play again?y/n')
