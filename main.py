import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
import random

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        
        uic.loadUi("app.ui", self)
        
        # varibles
        self.board = ['','','','','','','','','','']
        self.startinggame = True
        self.p_letter = ['']
        self.chance = 1
        
        self.setLayout(self.gridLayout)
        self.b1.clicked.connect(lambda: self.moves(1))
        self.b2.clicked.connect(lambda: self.moves(2))
        self.b3.clicked.connect(lambda: self.moves(3))
        self.b4.clicked.connect(lambda: self.moves(4))
        self.b5.clicked.connect(lambda: self.moves(5))
        self.b6.clicked.connect(lambda: self.moves(6))
        self.b7.clicked.connect(lambda: self.moves(7))
        self.b8.clicked.connect(lambda: self.moves(8))
        self.b9.clicked.connect(lambda: self.moves(9))

        # intro
        self.intro()
    
    def intro(self):
        self.msg.setText("Welcome to Tic tac toe!! Click any key to start")
    
    def moves(self, ch):
        self.draw_board()
        
        if self.startinggame:
            self.chance = self.whose_goes_first()
            self.player_letter()
            
            self.msg.setText(f"{self.whochance(self.chance)} first move and your letter is {self.p_letter[1]}")
            self.startinggame = False
            
            if self.chance == 2:
                self.moves(1)
            return

        self.msg.setText(f"{self.whochance(self.chance)} - T U R N")
        
        if self.chance == 1:
            if (self.board[ch]) =='':
                self.board[ch] = self.p_letter[1]
                
                self.draw_board()

                if self.win_or_tie():
                    self.disablebtn()
                    return
                self.chance = 2
        
        if self.chance == 2:
            cc = self.critical_check()
            
            if cc != -1:
                self.board[cc] = self.p_letter[2]
            else:
                rn = self.place_random()
                self.board[rn] = self.p_letter[2]
            self.draw_board()
            
            if self.win_or_tie():
                self.disablebtn()
                return
            self.chance = 1
                    
        self.msg.setText(f"{self.whochance(self.chance)} - T U R N")

    
    # tic-tac-toe
    def disablebtn(self):
        self.b1.setEnabled(False)
        self.b2.setEnabled(False)
        self.b3.setEnabled(False)
        self.b4.setEnabled(False)
        self.b5.setEnabled(False)
        self.b6.setEnabled(False)
        self.b7.setEnabled(False)
        self.b8.setEnabled(False)
        self.b9.setEnabled(False)

    def win_or_tie(self):
        if self.check_win():
            self.msg.setText(f"{self.whochance(self.chance)} wins")
            return True
        elif self.check_tie():
            self.msg.setText("match tie!!")
            return True
        return False
    
    def check_win(self):
        lst = ['789', '456', '123', '741', '852', '963', '753', '951']

        for i in lst:
            f = int(i[0])
            s = int(i[1])
            t = int(i[2])
            ch = False

            if (self.board[f] == self.board[s] == self.board[t]) and (self.board[f] == self.board[s] == self.board[t] != ''):
                ch = True
                break
        return ch

    def check_tie(self):
        for i in range(1, 10):
            if self.board[i] == '':
                return False

        if self.check_win():
            return False
        return True

    def critical_check(self):
        '''return -1 if there is no critical moves only for computer'''
        lst = ['789', '456', '123', '741', '852', '963', '753', '951']

        status = False
        letters = (self.p_letter[1:])[::-1]
        for ltr in letters:
            for i in lst:
                f = int(i[0])
                s = int(i[1])
                t = int(i[2])
                ch = -1
                if (self.board[f] == self.board[s] == ltr) and (self.board[t] == ''):
                    ch = t
                    status = True
                    break

                elif (self.board[f] == self.board[t] == ltr) and (self.board[s] == ''):
                    ch = s
                    status = True
                    break

                elif (self.board[s] == self.board[t] == ltr) and (self.board[f] == ''):
                    ch = f
                    status = True
                    break
            if status:
                break
        return ch

    def check_moves_lef(self):
        lst = []
        for i in range(1, 10):
            if self.board[i] == '':
                lst.append(i)
        return lst

    def place_random(self):
        case_lst = []
        lst = self.check_moves_lef()

        if self.board[5] == '':
            return 5

        for i in lst:
            for j in [1, 3, 7, 9]:
                if i == j:
                    case_lst.append(i)

        if len(case_lst) > 0:
            ch = random.randint(0, len(case_lst) - 1)
            return case_lst[ch]

        rn = random.randint(0, len(lst) - 1)
        return lst[rn]

    def whochance(self,ch):
        if ch == 1:
            return 'PLAYER'
        return 'COMPUTER'
    
    def draw_board(self):
        self.b1.setText(str(self.board[1]))
        self.b2.setText(str(self.board[2]))
        self.b3.setText(str(self.board[3]))
        self.b4.setText(str(self.board[4]))
        self.b5.setText(str(self.board[5]))
        self.b6.setText(str(self.board[6]))
        self.b7.setText(str(self.board[7]))
        self.b8.setText(str(self.board[8]))
        self.b9.setText(str(self.board[9]))
    
    def player_letter(self):
        ch = random.randint(1, 2)
        if ch == 1:
            t = ['X', 'O']
        else:
            t = ['O', 'X']
        
        self.p_letter.append(t[0])
        self.p_letter.append(t[1])

    def whose_goes_first(self):
        return random.randint(1, 2)
    




if __name__ == '__main__':
    app = QApplication(sys.argv)

myApp = MyApp()
myApp.show()

sys.exit(app.exec_())
