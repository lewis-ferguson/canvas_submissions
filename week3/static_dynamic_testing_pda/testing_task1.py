

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1: #Should be a '==' instead of =, to check if its equal to, and not assigning it a value
      return True
    else               #missing colon after else
      return False
   
                                        #comma missing between card1 and card 2
  dif highest_card(self, card1 card2):  #spelling mistake dif instead of def
  if card1.value > card2.value:         #indentation error on this line
    return card                         #this should be card1, not card, as only card1 and card2 are passed in
  else:
    return card2
  


def cards_total(self, cards): #indentation error, this will not run
  total              #total must be set to a value, it is assigned to nothing
  for card in cards:
    total += card.value
    return "You have a total of" + total