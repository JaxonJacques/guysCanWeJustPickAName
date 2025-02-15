import random 



class card_Game():
    def __init__(self, pairs:int):
        """
        Parameters:
            pairs: number of pairs to be generated
        """

        # Initialize size of game for difficulty
        self.size = pairs*2
        self.errors = pairs*2

        # 2D array of cards to be saved
        self.arr = [[2]*pairs for i in range(2)]
    
    def get_arr(self)->list:
        """
        Returns:
            array of cards
        """
        return self.arr

    def get_size(self)->int:
        """
        Returns:
            size in type int
        """
        return self.size

    def generate_cards(self):
        """
        Generates random cards to memorize for playing
        """

        for i in range(self.size/2):
            for j in range(2):
                y, x = 0
                while self.arr[x][y] != None:
                    y = random.randint(0, 2)
                    x = random.randint(0, self.size/2-1)
                self.arr[y][x] = i

        # SOMEONE DO THIS I CANT IMPORT OPENAI /shrug

    def flip_cards(self, card_1:tuple, card_2:tuple)->bool:
        """
        Takes 2D location of cards in list and returns if both are equal
        If equal then replaces positions as None Type
        Parameters:
            card_1: location of first card
            card_2: location of second card
        Returns:
            whether if cards are equal
        """
        if (self.arr[card_1[0]][card_1[1]] == self.arr[card_2[0]][card_2[1]]):
            self.arr[card_1[0]][card_1[1]] = None
            self.arr[card_2[0]][card_2[1]] = None
            return True
        else:
            return False

    def play(self):
        while not all(j == None for i in self.arr for j in i) and self.errors > 0:
            
            print(self.arr)
        return self.errors > 0
    
    

def main():
    card = card_Game(2)
    print(card.get_size())
    if card.play():
        print("You won!")
    else:
        print("Stupid MF.")
    

if __name__ == "__main__":
    main()