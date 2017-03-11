import utils


class MoveMaker:
    def __init__(self):
        self.board_size = utils.board_size
        self.match_list = utils.match_list

        self.special_candies = utils.special_candies
        self.simple_candies = utils.simple_candies

        self.striped_candies_h = utils.striped_candies_h
        self.striped_candies_v = utils.striped_candies_v
        self.striped_candies = utils.striped_candies

        self.wrapped_candies = utils.wrapped_candies
        self.chocolate = utils.chocolate

        self.game_board = None
        self.potential_start_coords = set()

    # The lower priority candy gets lower score, hence, easier to choose the overall move
    def get_score(self, candy_type):
        if candy_type in self.simple_candies:
            return 20
        if candy_type in self.striped_candies:
            return 120
        if candy_type in self.wrapped_candies:
            return 300
        return 0

    # Calculate scores based on different candies and get their total.
    def compute_score(self, board, candies_coords):
        score = 0
        for coords in candies_coords:
            candy_value = board[coords[0]][coords[1]]
            score += self.get_score(candy_value)

        if len(candies_coords) == 4:
            return score * 3
        elif len(candies_coords) >= 5:
            return score * 10
        else:
            return score

    # see if the two kinds of candies match
    def candy_matches(self, type1, type2):
        if type1 == type2:
            return True
        else:
            for match in self.match_list:
                if type1 in match and type2 in match:
                    return True
        return False

    # returns the coords of all the candies that would explode with the chocolate
    def get_chocolate_exploding_candies(self, board, color):
        exploding = []
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.candy_matches(board[i][j], color):
                    exploding.append((i, j))
        return exploding

    # returns the coords of all candies that would explode with the striped candy
    def get_striped_exploding_candies(self, board, coords):
        exploding = []
        candy_type = board[coords[0]][coords[1]]
        if candy_type in self.striped_candies_h:
            for k in range(self.board_size):
                exploding.append((coords[0], k))  # Horizontal candies
        if candy_type in self.striped_candies_v:
            for k in range(self.board_size):
                exploding.append((k, coords[1]))  # Vertical candies

        return exploding

# TODO: Complete this class with the evaluation functions as discussed.
# TODO: Create the explosions function to see the benefits from the special candies (if any)