class Deck:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.is_alive = True

class Ship:
    def __init__(self, start, end):
        # Create decks and save them to a list `self.decks`
        self.start = start
        self.end = end
        self.is_drowned = False
        self.decks = []

    def crate_decks(self, i, j):
        self.decks.append(Deck(i, j))

    # def get_deck(self, row, column):
    #     # Find the corresponding deck in the list
    #     for deck in self.decks:
    #         if deck.row == row and deck.column == column:
    #             return deck

    def fire(self, row, column):
        # Change the `is_alive` status of the deck
        # And update the `is_drowned` value if it's needed
        health_ship = []

        for deck in self.decks:
            if deck.row != row or deck.column != column:
                health_ship.append(deck.is_alive)
            elif deck.row == row or deck.column == column:
                deck.is_alive = False
                health_ship.append(deck.is_alive)
        # print(health_ship)
        if not any(health_ship):
            self.is_drowned = False
            return False
        return True


class Battleship:
    def __init__(self, ships):
        # Create a dict `self.field`.
        # Its keys are tuples - the coordinates of the non-empty cells,
        # A value for each cell is a reference to the ship
        # which is located in it
        self.ships = ships
        self.field = {}

    def create_field_dict(self):
        for ship in self.ships:
            instance_ship = Ship(ship[0], ship[1])
            for i in range(ship[0][0], ship[1][0] + 1):
                for j in range(ship[0][1], ship[1][1] + 1):
                    instance_ship.crate_decks(i, j)
                    self.field[i, j] = instance_ship

    def fire(self, location: tuple):
        # This function should check whether the location
        # is a key in the `self.field`
        # If it is, then it should check if this cell is the last alive
        # in the ship or not.

        # self.create_field_dict()
        print(self.field)
        if location not in self.field:
            return "Miss!"
        if location in self.field:
            n = self.field.get(location)
            if n.fire(location[0], location[1]):
                return "Hit!"
            return "Sunk!"
