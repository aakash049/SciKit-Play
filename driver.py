import time
import win32api
import ctypes
import numpy as np
import sys
import win32con
from PIL import Image
from PIL import ImageGrab

import move_maker
from back_decoder import BackRecognizer
from cell_decoder import CellRecognizer
from utils import *

class Driver:
    def __init__(self, board_coords):
        self.ref_img = None
        self.board_box = board_coords
        print self.board_box
        self.img_size = (board_coords[2] - board_coords[0], board_coords[3] - board_coords[1])
        self.cell_size = (self.img_size[0] / 9, self.img_size[1] / 9)
        self.game_board = np.zeros((board_size, board_size), dtype=np.int32)
        self.cell_recognizer = CellRecognizer()
        self.cell_recognizer.train()

        self.prev_board = None

        self.back_recognizer = BackRecognizer()
        self.back_recognizer.train()

        self.mover = move_maker.MoveMaker()

        fx = open('movefile.txt', "w+")
        fx.write('')
        fx.close()


    def close_script(self):
        print 'wow'
        sys.exit()

    def play(self):
        fx = open("flag.txt", "w+")
        fx.write("0")
        fx.close()
        fx = open("prev.txt", "w+")
        fx.write("[(0, 0), (0, 0)]")
        fx.close()
        while True:
            if not self.board_is_moving():
                board_img = self.grab_board()
                board_state = self.back_recognizer.predict(board_img)
                print 'working yo! '
                print board_state
                if board_state == scoreboard:
                    break
                else:
                    move = self.mover.solve_board(self.game_board)
                    self.do_move(move)
            time.sleep(0.4)  # wait for the cells to finish moving


    # It takes the screenshot of the board and then crops each cell using a nested loop
    def grab_board(self):
        # global game_board
        # global temp_board
        img = ImageGrab.grab()
        img = img.crop(self.board_box)
        for y in range(0, 9):
            for x in range(0, 9):
                cell_box = (
                    x * self.cell_size[0], y * self.cell_size[1], (x + 1) * self.cell_size[0],
                    (y + 1) * self.cell_size[1])
                cell = img.crop(cell_box)
                self.game_board[y][x] = self.cell_recognizer.predict(cell)
                #temp_board[y][x] = self.game_board[y][x]
                #print self.game_board[y][x]
        img = img.resize((img.size[0] / 4, img.size[1] / 4), Image.NEAREST)
        return img

    # checks if the board is in moving state (It is in moving state after the candies have been exploded)
    def board_is_moving(self):
        img = ImageGrab.grab()
        img = img.crop(self.board_box)
        img = img.resize((img.size[0] / 4, img.size[1] / 4), Image.NEAREST)

        has_movement = True
        if self.ref_img:
            has_movement = self.compare_images(img, self.ref_img, threshold=100) > 100

        self.ref_img = img
        return has_movement

    # for comparing the pixels of the cell board
    @staticmethod
    def are_pixels_equal(p1, p2, threshold):
        diff = 0
        for i in range(3):
            diff += abs(p1[i] - p2[i])
        return diff < threshold

    def compare_images(self, current, reference, threshold):
        current_data = np.array(current.getdata())
        ref_data = np.array(reference.getdata())

        diff_pixels = 0
        total_size = current.size[0] * current.size[1]
        for i in range(0, total_size - 3, 3):
            if not self.are_pixels_equal(current_data[i], ref_data[i], threshold):
                diff_pixels += 1

        #print diff_pixels
        return diff_pixels

    #  for imitating the clicks on the board
    def win32_click(self, x, y):
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

    # it gets the coords of the central part of the cell
    def get_desktop_coords(self, cell):
        x = self.board_box[0] + cell[1] * self.cell_size[0] + self.cell_size[0] / 2
        y = self.board_box[1] + cell[0] * self.cell_size[1] + self.cell_size[1] / 2
        return x, y

    # sort of main function for win32 api
    def do_move(self, move):
        start = move[0]
        end = move[1]

        start_w = self.get_desktop_coords(start)
        end_w = self.get_desktop_coords(end)

        win32api.SetCursorPos(start_w)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, start_w[0], start_w[1], 0, 0)
        time.sleep(0.3)  # for waiting the board to settle down after explosions
        win32api.SetCursorPos(end_w)
        time.sleep(0.3)  # for waiting the board to settle down after explosions
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, end_w[0], end_w[1], 0, 0)
        win32api.SetCursorPos((self.board_box[0] - 50, self.board_box[1] - 50))
