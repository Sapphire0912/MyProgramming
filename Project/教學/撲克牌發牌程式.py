class Card():
    '''A playing card.'''
    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] # 13張牌
    suits = ["梅", "方", "紅", "黑"] # 4種花色

    def __init__(self, rank, suit, face_up = True):
        self.rank = rank # 牌面數字
        self.suit = suit # 花色
        self.is_face_up = face_up # 牌面是否為正面(True 為正面, False 為背面)

    def __str__(self): # 重新定義 print() 方法, 列印一張牌的資訊
        if self.is_face_up:
            rep = self.suit + self.rank
        else:
            rep = "XX"
        return rep
    
    def pie_order(self): # 牌的順序號 <- 為了之後圖形化牌面而保留的
        if self.rank == "A":
            FaceNum = 1
        elif self.rank == "J":
            FaceNum = 11
        elif self.rank == "Q":
            FaceNum = 12
        elif self.rank == "K":
            FaceNum = 13
        else:
            FaceNum = int(self.rank)
        
        if self.suit == "梅":
            Suit = 1
        elif self.suit == "方":
            Suit = 2
        elif self.suit == "紅":
            Suit = 3
        elif self.suit == "黑":
            Suit = 4
        return (Suit-1) * 13 + FaceNum
    
    def filp(self): # 翻牌方法
        self.is_face_up = not self.is_face_ups

class Hand():
    '''A hand of playing cards.'''
    def __init__(self):
        self.cards = [] # cards 清單變數儲存牌手的牌
    
    def __str__(self): # 重新定義 print() 方法, 列印出手牌的所有牌
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + "\t"
        else:
            rep = "無牌"
        return rep
    
    def clear(self): # 清空手裡的牌
        self.cards = []
    
    def add(self, card): # 增加牌
        self.cards.append(card) 
    
    def give(self, card, other_hand): # 把一張牌給其他牌手
        self.cards.remove(card)
        other_hand.add(card)
    
class Poke(Hand):
    '''A deck of playing cards.'''
    def populate(self): # 產生一副牌
        for suit in Card.suits:
            for rank in Card.ranks:
                self.add(Card(rank, suit))
    
    def shuffle(self): # 洗牌
        import random
        random.shuffle(self.cards) # 打亂牌的順序

    def deal(self, hands, per_hand = 13): # 發牌, 發給玩家預設 13 張牌
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.cards.remove(top_card)
                    hand.add(top_card)
                else:
                    print("不能繼續發牌, 牌已經發完!")

if __name__ == "__main__":
    print("This is a module with classes for playing cards.")
    # 4個玩家
    players = [Hand(), Hand(), Hand(), Hand()]
    pokel = Poke()
    pokel.populate() # 產生一副牌
    pokel.shuffle() # 洗牌
    pokel.deal(players, 13) # 發給玩家每人 13 張牌

    # 顯示 4 位元牌手的牌
    n = 1
    for hand in players:
        print("牌手", n, end = ":")
        print(hand)
        n += 1
    # input("\nPress the enter key to exit.")
# 之後用到記得改編碼格式