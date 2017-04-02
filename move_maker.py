from copy import deepcopy as dc

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

    def compute_explosions_lines(self, board, start):
        directions_to_visit = [[(-1, 0), (1, 0)],  # vertical
                               [(0, -1), (0, 1)]]  # horizontal
        to_explode = []
        for dirs in directions_to_visit:
            open_list = [start]
            for d in dirs:
                i = start[0] + d[0]
                j = start[1] + d[1]
                while 0 <= i < self.board_size and 0 <= j < self.board_size and board[i][j] != -1 \
                        and self.candy_matches(board[i][j], board[start[0]][start[1]]):
                    open_list.append((i, j))
                    i += d[0]
                    j += d[1]

            if len(open_list) >= 3:
                for element in open_list:
                    if element not in to_explode:
                        if board[element[0]][element[1]] in self.striped_candies:
                            to_explode.extend(self.get_striped_exploding_candies(board, element))
                        else:
                            to_explode.append(element)

        return to_explode

    # calculates explosions sorted by priority
    def compute_explosions(self, start, end, board):
        chocolate_multiplier = 1
        to_explode = []

        if board[start[0]][start[1]] in self.special_candies and board[end[0]][end[1]] in self.special_candies:
            score = 500000
            to_explode = [start, end]
        else:
            if board[start[0]][start[1]] == 12:  # chocolate
                to_explode = self.get_chocolate_exploding_candies(board, board[end[0]][end[1]])
                chocolate_multiplier = 100
            else:
                to_explode = self.compute_explosions_lines(board, start)

            to_explode.sort(key=(lambda x: x[0]))
            score = self.compute_score(board, to_explode) * chocolate_multiplier

        if len(to_explode) == 4 and board[start[0]][start[1]] != 12:  # striped candy
            board[start[0]][start[1]] += 1
            to_explode.remove(start)

        # Slide the other candies down after explosions take place
        for coord in to_explode:
            i, j = coord

            while i > 0:
                if board[i - 1][j] != -1 and (i - 1, j) not in self.potential_start_coords:
                    self.potential_start_coords.add((i, j))
                board[i][j], board[i - 1][j] = board[i - 1][j], board[i][j]
                i -= 1
            board[i][j] = -1

        return score, board

    # evaluates the board for score which can be obtained after a certain move
    def evaluate_board(self, start, end, board):
        total_score, new_board = self.compute_explosions(start, end, board)
        score = total_score
        multiplier = 1
        while score > 0:
            use_new = False
            if use_new:
                potential_start = dc(self.potential_start_coords)
                self.potential_start_coords = set()
                score = 0
                for coord in potential_start:
                    score, new_board = self.compute_explosions((coord[0], coord[1]), end, new_board)
                    if score > 0:
                        total_score += score + multiplier * 60
                        multiplier += 2
            else:
                for i in range(0, self.board_size):
                    for j in range(0, self.board_size):
                        score, new_board = self.compute_explosions((i, j), end, new_board)
                        if score > 0:
                            total_score += score + multiplier * 60
                            multiplier += 2

        return total_score, new_board

    # checks for all the feasible directions which can traversed for candies
    def check_direction(self, start, dir):
        end = (start[0] + dir[0], start[1] + dir[1])
        board = dc(self.game_board)
        if start[0] < 0 or start[0] > self.board_size or end[0] < 0 or end[0] > self.board_size \
                or start[1] < 0 or start[1] > self.board_size or end[1] < 0 or end[1] > self.board_size:
            return -1, [], None

        # swap
        board[start[0]][start[1]], board[end[0]][end[1]] = board[end[0]][end[1]], board[start[0]][start[1]]
        score_start, start_board = self.evaluate_board(start, end, board)
        score_end, end_board = self.evaluate_board(end, start, board)

        if score_start > score_end:
            return score_start, [start, end], start_board
        else:
            return score_end, [end, start], end_board

    # main function to start solving the board
    def solve_board(self, board, moves):
        self.game_board = board
        max_score = 0
        chosen_move = []
        for i in range(0, 8):
            for j in range(0, 8):
                possible_directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for d in possible_directions:
                    score, move, b = self.check_direction((i, j), d)
                    if score >= max_score:
                        if len(moves) is 0:
                            max_score = score
                            chosen_move = move
                        elif moves.count(move) is 0:
                            max_score = score
                            chosen_move = move

        if(chosen_move[0][0] == chosen_move[1][0]):
            print 1
        else:
            print 0

        return max_score, chosen_move

# DONE: Complete this class with the evaluation functions as discussed.
# DONE: Create the explosions function to see the benefits from the special candies (if any)
