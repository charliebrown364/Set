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
        """Runs a full game of Set!. Takes in a boolean enable_hints, which
        determines if hints are given to the user."""

        # Prints game info
        print("\nYou're playing Set!")
        print("\nInput the indices of 3 cards that form a set, separated by spaces.")
        print("Example: If the 1st, 4th, and 12th cards form a set, type \"1 4 12\" (without the quotes)")

        # Initializes the deck and board, and prints the board
        self.initialize_deck()
        self.fill_board(12)
        self.print_board()

        # Loops until the deck is empty
        while self.deck != []:

            # Prompts the user for input
            inputted_cards = self.get_user_input()
            while not inputted_cards:
                print("That input is invalid. Try again!")
                inputted_cards = self.get_user_input()

            # Checks if the inputted cards form a set
            if self.cards_form_a_set(inputted_cards):
                # If so, removes the cards from the board...
                self.remove_cards_from_board(inputted_cards)
                print(f"Correct! That was a set. You have found {self.score} out of 27 sets.")
                # ... and adds new cards to the board
                self.fill_board(3)
                self.print_board()
            else:
                # If not, gives the user a hint (if enable_hints is True)
                print("Sorry, that is not a set. Try again!")
                if enable_hints:
                    self.print_sets()

        # Ends the game
        print("\nYou win! Thanks for playing.")

    def initialize_deck(self) -> None:
        """Initializes the deck w/ all possible cards."""
        for number in ["1", "2", "3"]:
            for opacity in ["blank", "striped", "full"]:
                for color in ["red", "green", "purple"]:
                    for shape in ["stadium", "diamond", "squiggle"]:
                        card = Card(number, opacity, color, shape)
                        self.deck.append(card)

    def get_user_input(self) -> list[Card] | bool:
        """Gets input from the user and checks if the input is a valid
        guess. If so, it returns the guess, but if not, it returns false."""

        # Gets user input
        user_input = input("\nYour guess: ")

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

    def cards_form_a_set(self, guessed_cards: list[Card]) -> bool:
        """Checks if the given cards form a set."""
        for attr in ["number", "opacity", "color", "shape"]:
            elems = [getattr(card, attr) for card in guessed_cards]
            if len(set(elems)) == 2:
                return False
        return True

    def fill_board(self, num_cards: int) -> None:
        """Adds new cards to the board, and removes them from the deck."""
        self.board += random.sample(self.deck, k = num_cards)
        self.remove_cards_from_list(self.board, self.deck)

    def remove_cards_from_board(self, guessed_cards: list[Card]) -> None:
        """Removes cards from the board, and increments the user's score."""
        self.board = self.remove_cards_from_list(guessed_cards, self.board)
        self.score += 1

    def remove_cards_from_list(self, cards: list[Card], card_list: list[Card]) -> list[Card]:
        """Removes the cards in one list (cards) from a 2nd list (card_list)."""
        return [card for card in card_list if card not in cards]

    def print_board(self) -> None:
        """Prints each card on the board."""
        print("\nCards:")
        for i, card in enumerate(self.board):
            print(f"{i + 1}: {str(card)}")

    def print_sets(self) -> None:
        """Prints each combination of cards that form a set."""
        print("\nHint: these cards form a set!")
        for guess in combinations(self.board, 3):
            card_1, card_2, card_3 = guess
            if card_1 != card_2 and card_1 != card_3 and card_2 != card_3:
                if self.cards_form_a_set(guess):
                    print(f"{str(card_1)}, {str(card_2)}, and {str(card_3)}")
