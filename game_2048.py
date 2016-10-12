# coding:utf-8
import random
import copy  # copy模块是为了执行undo时深拷贝显示用的数组给另一个undo数组.


class GameOf2048(object):
    def __init__(self):
        self.n = 4  # self.n用来定义数组大小,此处的4表示若无其他更改,将会生成一个4*4的二维数组.
        self.i = 0
        self.j = 0
        self.check_list = []  # check_list用于储存已经有数字的坐标,然后检查坐标是否在check_list中,
        # 若不在则在坐标处插入一个随机数字.
        self.panel = [[0 for self.i in range(4)] for self.j in range(4)]  # 用于储存数字的数组(游戏面板)
        self.undo_panel = [[0 for self.i in range(4)] for self.j in range(4)]  # 用于执行undo的数组.
        self.random_X = 1  # X坐标
        self.random_Y = 1  # Y坐标
        self.check = (1, 1)  # 用于检查是否重复的元组
        self.score = 0  # 用于记录分数
        self.GameStatus = 'PLAYING'  # 游戏状态

    def initial_chessboard(self):
        self.panel = [[0 for self.i in range(self.n)] for self.j in range(self.n)]
        self.undo_panel = [[0 for self.i in range(self.n)] for self.j in range(self.n)]
        self.clear_variable()
        for self.i in range(4):  # 在二维数组中随机插入4个数字
            self.random_X = random.randint(0, self.n-1)
            self.random_Y = random.randint(0, self.n-1)
            self.check = (self.random_X, self.random_Y)
            while self.check in self.check_list:
                self.random_X = random.randint(0, self.n-1)
                self.random_Y = random.randint(0, self.n-1)
                self.check = (self.random_X, self.random_Y)
            self.check_list.append(self.check)
            self.panel[self.random_X][self.random_Y] = 2  # 若(X,Y)处没有数字就插入一个2
        self.clear_variable()
        self.show()

    def right_choice(self):  # 向右移动指令的实现函数
        self.undo_panel = copy.deepcopy(self.panel)  # 为了执行undo需要把执行向右操作前的数组深复制到undo_panel中.
        temp = 0  # 当一个数字第一次出现时,就把这个数赋给temp
        count = 1  # count用于判断一个数是否是第一次出现.
        j = 0
        for each in self.panel:
            for i in range(len(each)-1, -1, -1):
                if each[i] > 0:  # 如果在一行中一个数大于0则进行下面的判断.
                    if count == 2 and each[i] == temp:  # 当count等于2时表示temp中已记录一个数字,若此时该数等于temp
                        # 则将该位置处的数置0,each[j]处数字乘2,再将分数做相应的相加,然后count置1,用于temp接受下个数.
                        each[j] = temp * 2
                        self.score += temp * 2
                        each[i] = 0
                        count = 1
                        j = 0
                    elif count == 2 and each[i] != temp:  # 如果each[i]不等于temp,则更新temp,同时记录该处位置
                        temp = each[i]
                        j = i
                    elif count == 1:  # count==1,表示该数在此行中第一次出现,然后将该数赋给temp,将该数出现的位置赋给变量 j,然后将count加1
                        temp = each[i]
                        j = i
                        count += 1
            temp = 0  # 一次循环后,将相应变量置零
            count = 1
            j = 0
        for each in self.panel:
            count = temp = first_appear_of_zero = 0
            # first_appear_of_zero表示相对的第一次出现0的位置.
            for i in range(len(each)-1, -1, -1):
                if each[i] == 0 and temp == 0:  # 若temp等于0,表示之前还没有出现过0,现在找到的是第一次出现0的地方,
                    # 把位置存入first_appear_of_zero,然后temp加1.(这个循环好像可以改改,但我懒得改了........)
                    first_appear_of_zero = i
                    temp += 1
                elif each[i] > 0 and temp > 0:
                    each[first_appear_of_zero] = each[i]
                    # 在此处数字不再为0,则将该处数字移到first_appear_of_zero处,再将该处数字置零.
                    each[i] = 0
                    for j in range((len(each) - count)-1, -1, -1):  # 继续寻找第一次出现0的地方.
                        if each[j] == 0:
                            first_appear_of_zero = j
                            break
                    count += 1  # count是为了用来减少找0时的循环次数,因为上面的循环一旦执行过一次,这一行的最右肯定不为0,
                    #            没必要判断.
        self.add_random_number()  # 移完后随机加一个数字.
        self.show()

    def left_choice(self):  # 和上面一个函数类似.
        self.undo_panel = copy.deepcopy(self.panel)
        temp = 0
        count = 1
        j = 0
        for each in self.panel:
            for i in range(len(each)):
                if each[i] > 0:
                    if count == 2 and each[i] == temp:
                        each[j] = temp * 2
                        self.score += temp * 2
                        each[i] = 0
                        count = 1
                        j = 0
                    elif count == 2 and each[i] != temp:
                        temp = each[i]
                        j = i
                    elif count == 1:
                        temp = each[i]
                        j = i
                        count += 1
            temp = 0
            count = 1
            j = 0
        for each in self.panel:
            count = temp = first_appear_of_zero = 0
            for i in range(len(each)):
                if each[i] == 0 and temp == 0:
                    first_appear_of_zero = i
                    temp += 1
                elif each[i] > 0 and temp > 0:
                    each[first_appear_of_zero] = each[i]
                    each[i] = 0
                    for j in range(len(each) + count):
                        if each[j] == 0:
                            first_appear_of_zero = j
                            break
                    count += 1
        self.add_random_number()
        self.show()

    def up_choice(self):  # 和上面一个函数类似.
        self.undo_panel = copy.deepcopy(self.panel)
        count = 1
        k = temp = 0
        length = len(self.panel)
        for i in range(length):
            for j in range(length):
                if self.panel[j][i] > 0:
                    if count == 1:
                        temp = self.panel[j][i]
                        count += 1
                        k = j
                    elif count == 2 and self.panel[j][i] == temp:
                        self.panel[k][i] = temp * 2
                        self.score += temp * 2
                        self.panel[j][i] = 0
                        count = 1
                    elif count == 2 and self.panel[j][i] != temp:
                        temp = self.panel[j][i]
                        k = j
            count = 1
            k = temp = 0
        for i in range(length):
            count = temp = first_appear_of_zero = 0
            for j in range(length):
                if self.panel[j][i] == 0 and temp == 0:
                    first_appear_of_zero = j
                    temp += 1
                elif self.panel[j][i] > 0 and temp > 0:
                    self.panel[first_appear_of_zero][i] = self.panel[j][i]
                    self.panel[j][i] = 0
                    for temp_j in range(length + count):
                        if self.panel[temp_j][i] == 0:
                            first_appear_of_zero = temp_j
                            break
                    count += 1
        self.add_random_number()
        self.show()

    def down_choice(self):  # 和上面一个函数类似.
        self.undo_panel = copy.deepcopy(self.panel)
        count = 1
        k = temp = 0
        length = len(self.panel)
        for i in range(length):
            for j in range(length-1, -1, -1):
                if self.panel[j][i] > 0:
                    if count == 1:
                        temp = self.panel[j][i]
                        count += 1
                        k = j
                    elif count == 2 and self.panel[j][i] == temp:
                        self.panel[k][i] = temp * 2
                        self.score += temp * 2
                        self.panel[j][i] = 0
                        count = 1
                    elif count == 2 and self.panel[j][i] != temp:
                        temp = self.panel[j][i]
                        k = j
            count = 1
            k = temp = 0
        for i in range(length):
            count = temp = first_appear_of_zero = 0
            for j in range(length-1, -1, -1):
                if self.panel[j][i] == 0 and temp == 0:
                    first_appear_of_zero = j
                    temp += 1
                elif self.panel[j][i] > 0 and temp > 0:
                    self.panel[first_appear_of_zero][i] = self.panel[j][i]
                    self.panel[j][i] = 0
                    for temp_j in range(length-1-count, -1, -1):
                        if self.panel[temp_j][i] == 0:
                            first_appear_of_zero = temp_j
                            break
                    count += 1
        self.add_random_number()
        self.show()

    def clear_variable(self):
        self.i = 0
        self.j = 0

    def add_random_number(self):
        number = random.choice([2, 4, 8])
        self.random_X = random.randint(0, self.n-1)
        self.random_Y = random.randint(0, self.n-1)
        while self.panel[self.random_X][self.random_Y] > 0:
            self.random_X = random.randint(0, self.n-1)
            self.random_Y = random.randint(0, self.n-1)
        self.panel[self.random_X][self.random_Y] = number

    def show(self):
        temp = ''
        for each in self.panel:
            for number in each:
                lens = len(str(number))
                zero_num = 4 - lens
                for i in range(zero_num):
                    temp += ' '
                final_string = temp + str(number)
                temp = ''
                print final_string,
            print
        print "Score: " + str(self.score)
        self.win_or_fail()

    def win_or_fail(self):
        count = 0
        for i in range(self.n):
            for j in range(self.n):
                if self.panel[i][j] == 2048:
                    print "Congratulation you have finish it,please keep on moving."
                else:
                    if self.panel[i][j] == 0:
                        count += 1
        if count == 0:
            print "Sorry,you failed."
            self.GameStatus = "END"
            #  exit()

    def set_n(self, n):
        self.n = n

    def undo_back(self):
        self.panel = copy.deepcopy(self.undo_panel)

g = GameOf2048()
g.initial_chessboard()
while 1:
    c = raw_input('输入一个方向(wsad)')
    if c == 'w':
        g.up_choice()
    elif c == 's':
        g.down_choice()
    elif c == 'a':
        g.left_choice()
    elif c == 'd':
        g.right_choice()