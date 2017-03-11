import numpy as np
from utils import *

board_box = (100, 136, 681, 653)
img_size = (board_box[2] - board_box[0], board_box[3] - board_box[1])
cell_size = (img_size[0] / 9, img_size[1] / 9)

game_board = np.zeros((board_size, board_size), dtype=np.int32)

'''
 Candy values:
- 0 blue
- 1 green
- 2 orange
- 3 purple
- 4 red
- 5 yellow
- 6 chocolate'''

board_dict = {0: 'blue       ', 1: 's_h_blue   ', 2: 'green      ', 3: 's_h_green  ', 4: 'orange     ',
              5: 's_h_orange ',
              6: 'purple     ', 7: 's_h_purple ', 8: 'red        ', 9: 's_h_red    ', 10: 'yellow   ',
              11: 's_h_yellow ',
              12: 'chocolate', 13: 's_v_blue   ', 14: 's_v_green  ', 15: 's_v_orange ', 16: 's_v_red    ',
              17: 's_v_yellow ', 18: 's_v_purple ', 19: 'blue_wrapped', 20: 'green_wrapped', 21: 'orange_wrapped',
              22: 'purple_wrapped', 23: 'red_wrapped', 24: 'yellow_wrapped', -1: 'empty    '}
