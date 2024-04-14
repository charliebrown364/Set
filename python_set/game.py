import random
from itertools import combinations
from card import Card

class Set:

    def __init__(self) -> None:
        """Initializes the game attributes."""
        self.deck = []
        self.board = []
        self.score = 0

    def run(self, *, enable_hints: bool = False) -> None:
        """Runs a full game of Set. Takes in a boolean enable_hints,
        which determines if hints are given to the user."""

        # Initializes the deck and board
        self.initialize_deck()
        self.initialize_board()

        # Prints information about the game and board
        self.print_game_info()
        self.print_board()

        # Loops until the deck is empty
        while self.deck != []:

            # Prompts the user for input
            inputted_cards = self.get_user_input()

            if self.check_for_set(inputted_cards):
                # If the inputted cards form a set, replace them with new cards
                self.replace_cards(inputted_cards)
                self.print_score()
                self.print_board()
            else:
                # Otherwise, gives the user a hint (if enable_hints is true)
                self.print_hint(enable_hints)

        # Ends the game
        print("\nYou win! Thanks for playing Set!")

    def initialize_deck(self) -> None:
        """Initializes the deck w/ all possible cards."""
        for number in ["1", "2", "3"]:
            for opacity in ["blank", "striped", "full"]:
                for color in ["red", "green", "purple"]:
                    for shape in ["stadium", "diamond", "squiggle"]:
                        card = Card(number, opacity, color, shape)
                        self.deck.append(card)

    def get_user_input(self) -> list[Card]:
        """Gets user input, running until the user inputs a properly-formatted guess."""
        while True:
            user_input = input("\nYour guess: ")
            validation = self.validate_user_input(user_input)
            if validation:
                return validation
            print("That input is invalid. Try again!")

    def validate_user_input(self, user_input: str) -> list[Card] | bool:
        """Checks if the user input is a valid guess. If so, it returns
        the guess, but if not, it returns false."""

        # Checks if the input contains non-numerical characters
        for char in user_input:
            if char not in "1234567890 ":
                return False
        
        # Checks if the input is not length 3
        user_input = user_input.split()
        if len(set(user_input)) != 3:
            return False

        # Checks if the inputted indices are between 1 and 12
        user_input = [int(index) - 1 for index in user_input]
        for index in user_input:
            if index < 0 or index > 11:
                return False

        # Returns the cards corresonding with the inputted indices
        return [self.board[i] for i in user_input]

    def check_for_set(self, cards: list[Card]) -> bool:
        """Checks if the given cards form a set."""
        for attr in ["number", "opacity", "color", "shape"]:
            elems = [getattr(card, attr) for card in cards]
            if len(set(elems)) == 2:
                return False
        return True

    def initialize_board(self) -> None:
        """Adds new cards to the board, and removes them from the deck."""
        self.board = random.sample(self.deck, k = 12)
        self.deck = [card for card in self.deck if card not in self.board]

    def replace_cards(self, cards: list[Card]) -> None:
        """Replaces the given cards on the board with new cards, in their same positions."""
        for i, card in enumerate(self.board):
            if card in cards:
                cards.remove(card)
                new_card = random.choice(self.deck)
                self.deck.remove(new_card)
                self.board[i] = new_card

    def print_game_info(self) -> None:
        """Displays information about the game to the terminal."""
        print("\nYou're playing Set!")
        print("\nInput the indices of 3 cards that form a set, separated by spaces.")
        print("Example: If the 1st, 4th, and 12th cards form a set, type \"1 4 12\" (without the quotes)")

    def print_board(self) -> None:
        """Displays each card on the board in the terminal."""
        print("\nCards:")
        for i, card in enumerate(self.board):
            print(f"{i + 1}: {str(card)}")

    def print_score(self) -> None:
        """Increments the user's score and displays it in the terminal."""
        self.score += 1
        print(f"Correct! That was a set. You have found {self.score} out of 27 sets.")

    def print_hint(self, enable_hints: bool) -> None:
        """Displays in the terminal each combination of cards that form a set."""
        
        print("Sorry, that is not a set. Try again!")
        if not enable_hints:
            return
        
        print("\nHint: these cards form a set:")
        for guess in combinations(self.board, 3):
            card_1, card_2, card_3 = guess
            if card_1 != card_2 and card_1 != card_3 and card_2 != card_3:
                if self.check_for_set(guess):
                    print(f"{str(card_1)}, {str(card_2)}, and {str(card_3)}")
