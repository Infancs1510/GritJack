import random as rd

class Card:
    def __init__(self, val, suit):
        self.val = val
        self.suit = suit

class Player:
    def __init__(self):
        self.hand = []
        self.player_val = 0
        self.player_stay = False
        self.num_aces = 0

    def hit(self, deck):
        self.player_stay = False
        card = rd.choice(deck)
        self.hand.append(card)
        self.addCardVal(card)
        deck.remove(card)

    def stay(self):
        self.player_stay = True

    def addCardVal(self, card):
        try:
            val = int(card.val)
        except:
            vals = {"J": 10, "Q": 10, "K": 10, "A": 1}
            val = vals[card.val]
        
        if (card.val == "A"):
            val = 11
            self.num_aces += 1
        
        self.player_val += val

class Game:
    def __init__(self):
        self.deck = self.createDeck()
        self.player = Player()
        self.dealer = Player()


        while True:

            try:
                player_bet = int(input("Enter your bet: "))
                if player_bet <= 0:
                    print("Bruh")
                    continue
                break
            except:
                print("Bruh")


        self.dealer.hit(self.deck)
        self.dealer.hit(self.deck)
        self.player.hit(self.deck)
        self.player.hit(self.deck)

        player_won = self.gameLoop()

        if (player_won):
            if self.player.player_val == 21:
                print(f"You won {player_bet*2.5}")
            else:
                print(f"You won {player_bet*2}")
            
       

    def gameLoop(self):
        print("Player's Hand: ")
        self.disHand(self.player.hand, "player")
        if (self.dealer.player_val < 21 and self.player.player_val == 21):
                print("You won blackjack 🥳")
                return(True)
        if (self.player.player_val < 21 and self.dealer.player_val == 21):
                print("The dealer won blackjack")
                return(False)
        if (self.player.player_val == 21 and self.dealer.player_val == 21):
                print("It's a tie. You lose anyway 🤣")
                return(False)
        while (True):
            

            option = input("Hit or Stay: ")

            if (option == "h" or option == "hit"):
                self.player.hit(self.deck)
                print("Dealer's Hand: ")
                self.disHand(self.dealer.hand, "dealer")
            elif (option == "s" or option == "stay"):
                self.player.stay()

                if self.dealer.player_val < 17:
                    self.dealer.hit(self.deck)
                    self.dealer.stay()
                else:
                    self.dealer.stay()
                print("Dealer's Hand: ")
                self.disHand(self.dealer.hand, "player")
            else:
                print("Bruh")
                continue
            print("Player's Hand: ")
            self.disHand(self.player.hand, "player")

            #print(self.player.player_val)
            
            if self.dealer.player_val > 21 and self.dealer.num_aces > 0:
                while self.dealer.num_aces > 0 and self.dealer.player_val > 21:
                    self.dealer.player_val -= 10
                    self.dealer.num_aces -= 1

            if (self.player.player_val > 21):
                if self.player.num_aces > 0:
                    while self.player.num_aces > 0 and self.player.player_val > 21:
                        self.player.player_val -= 10
                        self.player.num_aces -= 1
                else:
                    print("You went over 21")
                    return(False)
            if (self.player.player_val < 21 and self.dealer.player_val == 21):
                print("The dealer won blackjack")
                return(False)
            if (self.player.player_stay and self.dealer.player_stay):
                if (self.dealer.player_val > self.player.player_val and self.dealer.player_val <= 21):
                    print("The dealer's hand is higher than yours")
                    return(False)
                elif (self.dealer.player_val == self.player.player_val):
                    print("It's a tie. You lose anyway 🤣")
                    return(False)
                elif (self.dealer.player_val < self.player.player_val):
                    print("Your hand is higher than the dealer's")
                    return(True)
            if (self.dealer.player_val > 21):
                print("The dealer went over 21 so you win")
                return(True)
            if (self.player.player_val == 21):
                print("You won blackjack 🥳")
                return(True)
    
    def disHand(self, hand, name):
        dis_hand = []

        if name == "player":
            for card in hand:
                dis_hand.append(card.val)
        elif name == "dealer":
            dis_hand.append(hand[-1].val)
            dis_hand.append("secret card 🤫")
        
        print(dis_hand)

    def createDeck(self):
        vals = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        suits = ["spade", "heart", "daimond", "club"]
        deck = []

        for suit in suits:
            for val in vals:
                deck.append(Card(val, suit))
        return(deck)
    

Game()

