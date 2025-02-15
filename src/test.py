

class card_Game():
    def __init__(self, pairs:int):
        """
        Parameters:
            pairs: number of pairs to be generated
        """

        # Initialize size of game for difficulty
        self.size = pairs*2

        # 2D array of cards to be saved
        self.arr = [[None]*pairs for i in range(2)]
    
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

        # SOMEONE DO THIS I CANT IMPORT OPENAI /shrug

    def play(self):
        pass
        
    
    

def main():
    card = card_Game(4)
    print(card.get_size())
    

if __name__ == "__main__":
    main()