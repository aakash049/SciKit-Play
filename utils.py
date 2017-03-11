# values for normal and striped H candies
blue = 0
blue_s_h = 1
green = 2
green_s_h = 3
orange = 4
orange_s_h = 5
purple = 6
purple_s_h = 7
red = 8
red_s_h = 9
yellow = 10
yellow_s_h = 11
chocolate_c = 12

# values for striped V candies
blue_s_v = 13
green_s_v = 14
orange_s_v = 15
purple_s_v = 16
red_s_v = 17
yellow_s_v = 18

# values for wrapped candies
blue_w = 19
green_w = 20
orange_w = 21
purple_w = 22
red_w = 23
yellow_w = 24

# values for boards
board_size = 9

# lists for different candy types
match_list = [(blue, blue_s_h, blue_s_v, blue_w),
              (green, green_s_h, green_s_v, green_w),
              (orange, orange_s_h, orange_s_v, orange_w),
              (purple, purple_s_h, yellow_s_v, purple_w),
              (red, red_s_h, purple_s_v, red_w),
              (yellow, yellow_s_h, red_s_v, yellow_w)]

special_candies = [blue_s_h, green_s_h, orange_s_h, purple_s_h, red_s_h, yellow_s_h,
                   chocolate_c, blue_s_v, green_s_v, orange_s_v, red_s_v, yellow_s_v,
                   purple_s_v, blue_w, green_w, orange_w, purple_w, red_w, yellow_w]

simple_candies = [blue, green, orange, purple, red, yellow]

striped_candies_h = [blue_s_h, green_s_h, orange_s_h, purple_s_h, red_s_h, yellow_s_h]

striped_candies_v = [blue_s_v, green_s_v, orange_s_v, purple_s_v, red_s_v, yellow_s_v]

striped_candies = striped_candies_h[:]
striped_candies.extend(striped_candies_v)

wrapped_candies = [blue_w, green_w, orange_w, purple_w, red_w, yellow_w]
chocolate = [chocolate_c]

# name for the cell recognizer file
cell_recognizer = 'cell.dat'
