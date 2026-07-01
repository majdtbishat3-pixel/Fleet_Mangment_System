'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
class player:
    def __init__(self):
        self.name=''
        self.sympol=''
    def choose_name(self):
        while True:
            name=input('enter the name only letters')
            if name.isalha():
                self.name=name
                break
            else:
                print('invalid name please use letters only')
            
        
    def choose_sympol(self):
        while True:
            sympol=input('enter the sympol of  sigle leteer only')
            if sympol.isalpha() and len(sympol)==1:
                self.sympol==sympol
                break
            print('invalid sympol please use single letters only')
class menu:
    def display_menu(self):
        print('welcome to x o game')
        print('1_ start game')
        print('2_end game')
        choice=int(input('enter the choice'))
        if choice==1 or choice==2:
            return choice
        return 'invalid number please enter correct choice'
    def dispaly_end_menu(self):
        print('game over')
        print('1_restart game')
        print('2_quit game')
        choice=int(input('enter the number choice'))
        if choice==1 or choice==2:
            return choice
class board:
    def __init__(self):
        self.board=[str(i) for in range(1,10)]#board=[]for i in range(1,10):for i in range(1,10):
        # عملناها string عشان ما بقدر اتعامل معاه عند استخدام داله join الا باستخدام نص 
        print('|'.join(self.board[i:i+3]))  
        