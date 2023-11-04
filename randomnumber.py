# Python 3.9
# -*- coding: utf-8 -*-

import random
import easygui as eg
from sys import exit
import os

'''
names = [u'李睿哲', u'翟田桢', u'麻天皓', u'贺瑞涵', u'郭巍然', u'曾博妍', u'张语茜', u'穆禹璋', u'杨佳宜', u'公惟伯', u'肖宇昕', u'于凯瑞', u'梁羽潇',
         u'赵丹阳', u'赵梓羽', u'朱美鑫', u'田宏震宇', u'张修瑜', u'程心怡', u'王兆欣', u'武子昂', u'李雨桐', u'张睿萱', u'李子聃', u'李刘泽宇', u'桑潘',
         u'余思钧', u'张靖坤', u'赵皓石', u'王星砚', u'刘琼璟', u'刘亦白', u'顾书瑜', u'温宸孟泽', u'张皓翔', u'王易涵', u'吉书毅', u'张芷菲', u'李沫瑶',
         u'陈涵霖', u'季子苏', u'张锦轩', u'王兰乐贝儿', u'张昊驰', u'郭泽豪', u'陈昱瑾', u'贺鑫梾', u'朱朗月', u'刘晨熙', u'岳冰慈', u'魏瑜圃', u'辛子珩',
         u'张尊赫', u'魏思玥', u'张家宁', u'刘子闻']

nameGenerate = names
'''

with open('config.txt', mode='r', encoding='utf-8', errors='ignore') as configFile:
    _config: list = configFile.readlines()
    _config = list(map(lambda s: s.strip(), _config))
    # map function: map the operation at the head to the following list.
    # strip method: delete the '\n's and spaces in the string.

# print(_config)
for line in _config:
    # print(line, line.startswith("#"))
    if line.startswith("#") or (line == ''):
        _config.remove(line)
# print(_config)
# FIXME Continuous hashes in the config file cause error.

# the default variables
if _config[0] == 'empty':
    defaultContext: str = ''  # replace 'empty' with '' -> see above.
else:
    defaultContext: str = _config[0]
defaultNameListFile: str = _config[1]
defaultReadmeFile: str = _config[2]
ifHideControlPanel: int = int(_config[3])


# BAGELS FUNCTIONS START
def getSecretNum(numDigits: int) -> str:  # get the secret number by the digit
    numbers = list(range(10))
    random.shuffle(numbers)  # random.shuffle() means disrupt a list
    secretNumber = ''
    for j in range(numDigits):
        secretNumber += str(numbers[j])
    return secretNumber


def getClues(guessNumber: str, secretNumber: str) -> str:  # get clues:Fermi Pico or Bagels
    if guessNumber == secretNum:
        return 'You got it!:-)'
    clueList = []
    for j in range(len(guessNumber)):
        if guessNumber[j] == secretNumber[j]:
            clueList.append('Fermi')
        elif guessNumber[j] in secretNumber:
            clueList.append('Pico')
    if len(clueList) == 0:
        return 'Bagels'
    clueList.sort()
    return ' '.join(clueList)


def isOnlyDigits(_number: str) -> bool:  # detect if a string is only made up of numbers
    if _number == '':
        return False
    for j in _number:
        if j not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False
    return True
# GUESS NUMBER 2 FUNCTIONS END


# Tic Tac Toe FUNCTIONS
def isTicTacToeWin(bo: list[str], le: str) -> bool:  # detect if a Tic Tac Toe game is over.
    return ((bo[6] == le and bo[7] == le and bo[8] == le) or
            (bo[3] == le and bo[4] == le and bo[5] == le) or
            (bo[0] == le and bo[1] == le and bo[2] == le) or
            (bo[6] == le and bo[3] == le and bo[0] == le) or
            (bo[7] == le and bo[4] == le and bo[1] == le) or
            (bo[8] == le and bo[5] == le and bo[2] == le) or
            (bo[6] == le and bo[4] == le and bo[2] == le) or
            (bo[8] == le and bo[4] == le and bo[0] == le))


def about() -> None:  # the "about" page
    eg.msgbox(u'''Proj. Random Name, version 0.3
        Designed by zjk
        Programmed by zjk
        Debugged by wyd
        (Tips:Try control panel)''')


def generateNamelist(_list: str) -> list:
    # Read name.txt file and get the name list.
    with open(_list, mode='r', encoding='utf-8') as File:
        _name = File.readlines()
    return _name


names: list = generateNamelist(defaultNameListFile)
nameGenerate: list = generateNamelist(defaultNameListFile)


while True:  # the main loop
    number = random.randint(0, len(nameGenerate) - 1)
    if ifHideControlPanel:
        b = eg.buttonbox(u"按“随机”按钮产生随机名字", choices=[u'随机', u'退出'], title='Random Name')
    else:
        b = eg.buttonbox(u"按“随机”按钮产生随机名字", choices=[u'随机', u'控制台', u'关于', u'退出'], title='Random Name')
    if b == u'退出':
        exit(0)  # exit method powered by sys module
    if b == u'随机':
        eg.msgbox(nameGenerate[number])  # get the random name
    if b == u'关于':
        about()
    if b == u'控制台':
        command = eg.enterbox('Type command', default=defaultContext)  # the default context of the context
        # GUESS NUMBER 1
        if command == 'guess-number':
            currentNumber = random.randint(1, 50)
            for i in range(6):
                num = eg.enterbox('Im thinking a number between 1 and 50.Guess it.Ill give you 6 guesses.')
                try:
                    num = int(num)
                except ValueError:
                    eg.msgbox('ValueError: invalid input: input should be a number')
                    break
                except TypeError:
                    eg.msgbox('Aborted.')
                    break
                if num > currentNumber:
                    eg.msgbox("Large")
                elif num < currentNumber:
                    eg.msgbox('Small')
                elif num == currentNumber:
                    eg.msgbox('You win!:-)')
                    break
            eg.msgbox('Game over.')

        if command == 'set':
            try:
                set_name = eg.enterbox('The name of a person')
                set_value = int(eg.enterbox('The value'))
                for i in range(set_value):
                    nameGenerate.append(set_name)
            except ValueError:
                eg.msgbox('ValueError: invalid input')
            except TypeError:
                eg.msgbox('Aborted.')

        # MINE
        if command == "mine":
            pass

        # BAGELS
        if command == 'bagels':
            numberDigits = eg.enterbox('Number digits', default='3')
            maxGuess = eg.enterbox('Max Guesses', default='10')
            try:
                eg.msgbox('Bagels\nIm thinking of a ' + str(numberDigits) + '-digit number.Try to guess what it is.')
                eg.msgbox(
                    '''When I say:            That means:
Pico             One digit is correct but in the wrong position
Fermi            One digit is correct and in the right position.
Bagels           No digit is correct.''')
                secretNum = getSecretNum(int(numberDigits))
                eg.msgbox('I have thought up a number.You have ' + str(maxGuess) + ' guesses to get it.')
                numGuesses = 1
                while numGuesses <= int(maxGuess):
                    guess = ''

                    while len(guess) != int(numberDigits) or (not isOnlyDigits(guess)):
                        guess = eg.enterbox('Guess #' + str(numGuesses))

                    clue = getClues(guess, secretNum)
                    eg.msgbox(clue)
                    numGuesses += 1
                    if guess == secretNum:
                        break
                    if numGuesses > int(maxGuess):
                        eg.msgbox('You ran out of guesses.The number was ' + secretNum)
                eg.msgbox('Game over.')
            except ValueError:
                eg.msgbox('ValueError: invalid input')
            except TypeError:
                eg.msgbox('Aborted.')

        if command == 'tic-tac-toe-board':
            eg.msgbox('Tic Tac Toe Board')
            eg.msgbox('7|8|9\n------\n4|5|6\n------\n1|2|3')
            goF = random.randint(0, 1)
            if goF == 0:
                turn = 'x'
            else:
                turn = 'o'
            board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            while True:
                move = eg.buttonbox(
                    board[6] + '|' + board[7] + '|' + board[8] + '\n------\n' + board[3] + '|' + board[4] + '|' + board[
                        5] + '\n------\n' + board[2] + '|' + board[1] + '|' + board[0],
                    choices=['1', '2', '3', '4', '5', '6', '7', '8', '9'])
                board[int(move) - 1] = turn
                if isTicTacToeWin(board, turn):
                    break
                if turn == 'x':
                    turn = 'o'
                else:
                    turn = 'x'
            eg.msgbox(turn + ' wins!')

        if command == 'readme':
            try:
                os.startfile(defaultReadmeFile)
            except FileNotFoundError:
                eg.msgbox('File not found.Type the correct file name.')

        if command == 'edit':
            try:
                os.startfile(defaultNameListFile)
            except FileNotFoundError:
                eg.msgbox('File not found.Type the correct file name.')

        if command == 'about':
            about()

        if command == 're-generate':
            gen_namelist = eg.enterbox('Type the name of the generate file')
            try:
                names = generateNamelist(gen_namelist)
                nameGenerate = generateNamelist(gen_namelist)
            except FileNotFoundError:
                eg.msgbox('File not found.Type the correct file name.')

        if command == 'config':
            try:
                os.startfile('config.txt')
            except FileNotFoundError:
                eg.msgbox('config.txt not found.\nPlease check, or the program won\'t run correctly.', title='Warning')
