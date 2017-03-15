import back_decoder
from utils import *
from PIL import Image
from PIL import ImageGrab

import time
board = (77, 164, 652, 670)

backdec = back_decoder.BackRecognizer()
backdec.train()

board_dic = {
    curtain: 'curtain\n',
    end: 'end\n',
    intro: 'intro\n',
    loading: 'loading\n',
    move: 'move\n',
    scoreboard: 'scoreboard\n',
    shop: 'shop\n',
    static: 'static\n'
}

i = 1
while True:
    img = ImageGrab.grab()
    img = img.crop(board)
    print board_dic[backdec.predict(img)]
    time.sleep(0.4)