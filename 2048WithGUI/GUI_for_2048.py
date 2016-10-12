# coding:utf-8
import pygame
import sys
import os
from game_2048 import GameOf2048
from pygame.locals import *
# import time


class GUIScreen(object):
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Small model of game 2048')  # 设置标题
        self.row_column_number = input("Please input a number to create chessboard:")
        self.unit_size = 100
        self.ROWS = self.row_column_number
        self.COLUMN = self.row_column_number
        self.size = self.ROWS * self.unit_size, self.COLUMN * self.unit_size + 50
        self.chessboard_2 = [[]]

        self.WHITE = (255, 255, 255)    # Define colors.And load pictures
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (20, 160, 15)
        self.GREY = (166, 160, 153)
        self.pic_0 = self.load_img('g0.jpg')
        self.pic_2 = self.load_img('g2.jpg')
        self.pic_4 = self.load_img('g4.jpg')
        self.pic_8 = self.load_img('g8.jpg')
        self.pic_16 = self.load_img('g16.jpg')
        self.pic_32 = self.load_img('g32.jpg')
        self.pic_64 = self.load_img('g64.jpg')
        self.pic_128 = self.load_img('g128.jpg')
        self.pic_256 = self.load_img('g256.jpg')
        self.pic_512 = self.load_img('g512.jpg')
        self.pic_1024 = self.load_img('g1024.jpg')
        self.pic_2048 = self.load_img('g2048.jpg')
        self.pic_4096 = self.load_img('g4096.jpg')
        self.pic_8192 = self.load_img('g8192.jpg')
        self.pic_16384 = self.load_img('g16384.jpg')
        self.pic_32768 = self.load_img('g32768.jpg')
        self.pic_score = self.load_img('gscore.jpg')

        self.GAME_STATE = 'playing'
        self.SCORE = 0
        self.IS_SCREEN_FULL = False
        self.screen = None
        self.fontObj = pygame.font.SysFont('楷体.ttf', 20)
        self.ScoreObj = self.fontObj.render(u'SCORE:', False, self.RED)
        self.Score_Word = self.fontObj.render(str(self.SCORE), False, self.WHITE)

        self.GameStart = GameOf2048()  # initial of game.
        self.GameStart.set_n(self.row_column_number)  # set chessboard's width and length.
        self.GameStart.initial_chessboard()
        self.chessboard_2 = self.GameStart.panel

    def new_screen(self):
        if self.IS_SCREEN_FULL:
            self.screen = pygame.display.set_mode(self.size, FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode(self.size)

    # def load_sound(self, filename):
    #     return pygame.mixer.Sound(os.path.join('res', filename))

    def load_img(self, filename):
        return pygame.image.load(os.path.join('img', filename))

    def draw_final(self):
        # pygame.draw.rect(self.screen, self.RED, (200, 120, 400, 300))
        # pygame.draw.rect(self.screen, self.BLACK, (210, 130, 380, 280))
        over_text = self.fontObj.render(u'GAME OVER!', True, self.RED)
        score_text = self.fontObj.render(u'Final Score: ' + str(self.SCORE), True, self.WHITE)
        prompt_text = self.fontObj.render(u'Press "Enter" to replay', True, self.WHITE)
        self.screen.blit(over_text, (15, 20))
        #  self.screen.blit(score_text, (self.unit_size + 30, self.unit_size))
        self.screen.blit(prompt_text, (300, 290))

    def turn_left(self):
        self.GameStart.left_choice()
        self.SCORE = self.GameStart.score
        self.Score_Word = self.fontObj.render(str(self.SCORE), False, self.WHITE)

    def turn_right(self):
        self.GameStart.right_choice()
        self.SCORE = self.GameStart.score
        self.Score_Word = self.fontObj.render(str(self.SCORE), False, self.WHITE)

    def turn_up(self):
        self.GameStart.up_choice()
        self.SCORE = self.GameStart.score
        self.Score_Word = self.fontObj.render(str(self.SCORE), False, self.WHITE)

    def turn_down(self):
        self.GameStart.down_choice()
        self.SCORE = self.GameStart.score
        self.Score_Word = self.fontObj.render(str(self.SCORE), False, self.WHITE)

    def undo_back(self):
        self.GameStart.undo_back()
        self.chessboard_2 = self.GameStart.panel
        self.SCORE = self.GameStart.score
        self.Score_Word = self.fontObj.render(str(self.SCORE), False, self.WHITE)

    def draw_pic_on_screen(self):
        self.GAME_STATE = self.GameStart.GameStatus
        length = self.row_column_number
        self.screen.fill(self.GREY)
        self.screen.blit(self.pic_score, ((self.row_column_number - 1) * self.unit_size, 10))
        self.screen.blit(self.Score_Word, ((self.row_column_number - 1) * self.unit_size + 22, 30))
        for i in range(length):
            for j in range(length):
                x_coordinate = j * self.unit_size
                y_coordinate = i * self.unit_size + 50
                coordinate = (x_coordinate, y_coordinate)
                if self.chessboard_2[i][j] == 0:
                    self.screen.blit(self.pic_0, coordinate)
                elif self.chessboard_2[i][j] == 2:
                    self.screen.blit(self.pic_2, coordinate)
                elif self.chessboard_2[i][j] == 4:
                    self.screen.blit(self.pic_4, coordinate)
                elif self.chessboard_2[i][j] == 8:
                    self.screen.blit(self.pic_8, coordinate)
                elif self.chessboard_2[i][j] == 16:
                    self.screen.blit(self.pic_16, coordinate)
                elif self.chessboard_2[i][j] == 32:
                    self.screen.blit(self.pic_32, coordinate)
                elif self.chessboard_2[i][j] == 64:
                    self.screen.blit(self.pic_64, coordinate)
                elif self.chessboard_2[i][j] == 128:
                    self.screen.blit(self.pic_128, coordinate)
                elif self.chessboard_2[i][j] == 256:
                    self.screen.blit(self.pic_256, coordinate)
                elif self.chessboard_2[i][j] == 512:
                    self.screen.blit(self.pic_512, coordinate)
                elif self.chessboard_2[i][j] == 1024:
                    self.screen.blit(self.pic_1024, coordinate)
                elif self.chessboard_2[i][j] == 2048:
                    self.screen.blit(self.pic_2048, coordinate)
                elif self.chessboard_2[i][j] == 4096:
                    self.screen.blit(self.pic_4096, coordinate)
                elif self.chessboard_2[i][j] == 8192:
                    self.screen.blit(self.pic_8192, coordinate)
                elif self.chessboard_2[i][j] == 16384:
                    self.screen.blit(self.pic_16384, coordinate)
                elif self.chessboard_2[i][j] == 32768:
                    self.screen.blit(self.pic_32768, coordinate)
        pygame.display.update()
    # def test_everything(self):
start_game = GUIScreen()
start_game.new_screen()
start_game.draw_pic_on_screen()
while True:
    if start_game.GAME_STATE == 'END':
        start_game.draw_final()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key in (K_DOWN, K_s):
                start_game.turn_down()
            elif event.key in (K_UP, K_w):
                start_game.turn_up()
            elif event.key in (K_LEFT, K_a):
                start_game.turn_left()
            elif event.key in (K_RIGHT, K_d):
                start_game.turn_right()
            elif event.key == K_f and (not start_game.IS_SCREEN_FULL):
                start_game.IS_SCREEN_FULL = True
                start_game.new_screen()
            elif event.key == K_f and start_game.IS_SCREEN_FULL:
                start_game.IS_SCREEN_FULL = False
                start_game.new_screen()
            elif event.key == K_b:
                start_game.undo_back()
                # start_game.new_screen()
            start_game.draw_pic_on_screen()
            pygame.display.update()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()
    pygame.display.update()
