import random


class Game2048(object):
    def __init__(self):
        self.n = input("Please input a number to create chessboard:")
        self.i = 0
        self.j = 0
        self.check_list = []
        self.panel = [[0 for self.i in range(self.n)] for self.j in range(self.n)]
        self.clear_variable()
        for self.i in range(4):
            self.random_X = random.randint(0, self.n-1)
            self.random_Y = random.randint(0, self.n-1)
            self.check = (self.random_X, self.random_Y)
            while self.check in self.check_list:
                self.random_X = random.randint(0, self.n-1)
                self.random_Y = random.randint(0, self.n-1)
                self.check = (self.random_X, self.random_Y)
            self.check_list.append(self.check)
            self.panel[self.random_X][self.random_Y] = 2
        self.clear_variable()
        self.show()

    def right_choice(self):
        temp = 0
        count = 1
        j = 0
        for each in self.panel:
            for i in range(len(each)-1, -1, -1):
                if each[i] > 0:
                    if count == 2 and each[i] == temp:
                        each[j] = temp * 2
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
            temp = first_appear_of_zero = 0
            for i in range(len(each)-1, -1, -1):
                if each[i] == 0 and temp == 0:
                    first_appear_of_zero = i
                    temp += 1
                elif each[i] > 0 and temp > 0:
                    each[first_appear_of_zero] = each[i]
                    each[i] = 0
                    for j in range(len(each)):
                        if each[j] == 0:
                            first_appear_of_zero = j
                            break
        self.add_random_number()
        self.show()

    def left_choice(self):
        temp = 0
        count = 1
        j = 0
        for each in self.panel:
            for i in range(len(each)):
                if each[i] > 0:
                    if count == 2 and each[i] == temp:
                        each[j] = temp * 2
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
            temp = first_appear_of_zero = 0
            for i in range(len(each)):
                if each[i] == 0 and temp == 0:
                    first_appear_of_zero = i
                    temp += 1
                elif each[i] > 0 and temp > 0:
                    each[first_appear_of_zero] = each[i]
                    each[i] = 0
                    for j in range(len(each)):
                        if each[j] == 0:
                            first_appear_of_zero = j
                            break
        self.add_random_number()
        self.show()

    def up_choice(self):
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
                        self.panel[j][i] = 0
                        count = 1
                    elif count == 2 and self.panel[j][i] != temp:
                        temp = self.panel[j][i]
                        k = j
            count = 1
            k = temp = 0
        for i in range(length):
            temp = first_appear_of_zero = 0
            for j in range(length):
                if self.panel[j][i] == 0 and temp == 0:
                    first_appear_of_zero = j
                    temp += 1
                elif self.panel[j][i] > 0 and temp > 0:
                    self.panel[first_appear_of_zero][i] = self.panel[j][i]
                    self.panel[j][i] = 0
                    for temp_j in range(length):
                        if self.panel[temp_j][i] == 0:
                            first_appear_of_zero = temp_j
                            break
        self.add_random_number()
        self.show()

    def down_choice(self):
        count = 1
        k = temp = 0
        length = len(self.panel)
        for i in range(length):
            for j in range(length-1, -1, -1):
                # print j,
                if self.panel[j][i] > 0:
                    if count == 1:
                        temp = self.panel[j][i]
                        count += 1
                        k = j
                    elif count == 2 and self.panel[j][i] == temp:
                        self.panel[k][i] = temp * 2
                        self.panel[j][i] = 0
                        count = 1
                    elif count == 2 and self.panel[j][i] != temp:
                        temp = self.panel[j][i]
                        k = j
            count = 1
            k = temp = 0
        for i in range(length):
            temp = first_appear_of_zero = 0
            for j in range(length-1, -1, -1):
                if self.panel[j][i] == 0 and temp == 0:
                    first_appear_of_zero = j
                    temp += 1
                elif self.panel[j][i] > 0 and temp > 0:
                    self.panel[first_appear_of_zero][i] = self.panel[j][i]
                    self.panel[j][i] = 0
                    for temp_j in range(length-1, -1, -1):
                        if self.panel[temp_j][i] == 0:
                            first_appear_of_zero = temp_j
                            break
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
        print
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
            exit()

s = Game2048()
while 1:
    choice = raw_input("Please input a direction:")
    if choice == 'w':
        s.up_choice()
    elif choice == 's':
        s.down_choice()
    elif choice == 'a':
        s.left_choice()
    elif choice == 'd':
        s.right_choice()
