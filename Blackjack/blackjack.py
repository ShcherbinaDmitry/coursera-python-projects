# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = [] 
        # create Hand object

    def __str__(self):
        ans = "hand contains "
        for i in range(len(self.hand)):
            ans += str(self.hand[i]) + ' ' 
        return ans	# return a string representation of a hand

    def add_card(self, card):
        self.hand.append(card)	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        val = 0
        check = False
        for i in range(len(self.hand)):
            val += VALUES[self.hand[i].get_rank()]
            if self.hand[i].get_rank() == "A":
                check = True
        if check and (val + 10 <= 21):
            val += 10
        return val
            # compute the value of the hand, see Blackjack video
   
    def draw(self, canvas, pos):
        for i in range(len(self.hand)):
            self.hand[i].draw(canvas, (pos[0]+i*CARD_SIZE[0],pos[1]))
            # draw a hand on the canvas, use the draw method for cards
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank)) # create a Deck object

    def shuffle(self):
        random.shuffle(self.deck)	# return a string representation of a hand
    # shuffle the deck 
           # use random.shuffle()

    def deal_card(self):
        return self.deck.pop()	# deal a card object from the deck
    
    def __str__(self):
        ans = "Deck contains "
        for i in range(len(self.deck)):
            ans += str(self.deck[i]) + ' ' 
        return ans
        # return a string representing the deck



#define event handlers for buttons
def deal():
    global outcome, in_play, deck, player_hand, dealer_hand, score
    if in_play:
        score -= 1
    deck = Deck()        
    player_hand = Hand()
    dealer_hand = Hand()
    # your code goes here
    in_play = True
    outcome = 'Hit or Stand?'
    deck.shuffle()
    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())

def hit():
    # replace with your code below
    # if the hand is in play, hit the player
    global deck, player_hand, outcome, in_play, score
    if in_play:
        outcome = 'Hit or Stand?'
        player_hand.add_card(deck.deal_card())
        if player_hand.get_value() > 21:
            outcome = "You're busted! New deal?"
            in_play = False
            score -= 1
    # if busted, assign a message to outcome, update in_play and score  
def stand():
    global in_play, deck, outcome, dealer_hand, player_hand, score
    if in_play:
        while (dealer_hand.get_value() < 17):
            dealer_hand.add_card(deck.deal_card())
            if (dealer_hand.get_value() >= player_hand.get_value()) and ( dealer_hand.get_value() <= 21):
                in_play = False
                score -= 1
                outcome = "Dealer have won! New deal?"          
            else:
                in_play = False
                score += 1
                outcome = "You have won! New deal?"
        if (dealer_hand.get_value() >= 17) and (dealer_hand.get_value() <= 21):
            if dealer_hand.get_value() >= player_hand.get_value():
                in_play = False
                score -= 1
                outcome = "Dealer have won! New deal?"  
            else:
                in_play = False
                score += 1
                outcome = "You have won! New deal?"    
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below  
    player_hand.draw(canvas, (50, 50))
    if in_play:
        dealer_hand.draw(canvas, (50, 450))
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [50+CARD_BACK_CENTER[0], 450 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
    else:
        dealer_hand.draw(canvas, (50, 450))
    canvas.draw_text('BLACKJACK', (380, 50), 36, 'Black')
    canvas.draw_text('Player', (50, 40), 36, 'Black')
    canvas.draw_text('Dealer', (50, 580), 36, 'Black')
    canvas.draw_text(outcome, (100, 300), 36, 'Black')
    canvas.draw_text('score:' + str(score), (450, 550), 36, 'Black')
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()
# remember to review the gradic rubric
