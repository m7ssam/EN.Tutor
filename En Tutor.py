from os import system
from random import choice
from pyttsx3 import speak as say
from pyperclip import copy
system('cls')
score, total_positive, total_nigative, M = 0, 0, 0, 0


class local():
    def __init__(self, file='null', col='null', Wrong=[], Right=[], T='null'):
        self.file = file
        self.col = col
        self.Vlist = []
        self.Wrong = Wrong
        self.Right = Right
        self.T = T

    def get_list(self):
        from csv import reader
        try:
            file = open(self.file, 'r')
            csv_reader = reader(file)
            for i, row in enumerate(csv_reader):
                self.Vlist.append(row)
            return self.Vlist[self.col]
        except:
            return []

    def nexit(self):
        pass

    def clear(self):
        return []

    def save(self):
        from pandas import DataFrame
        from csv import writer
        self.data = [self.Right,
                     self.Wrong]
        self.a = {'Right': self.Right, 'Wrong': self.Wrong}
        self.df = DataFrame.from_dict(self.a, orient='index')
        self.df = self.df.transpose()
        self.dfn = DataFrame(self.df)
        self.dfn.to_csv('DATA.csv')
        print('_'*50)
        print('Wrong words are:')
        print(self.dfn)
        print('_'*50)
        try:
            with open('Back_up.csv', 'w', newline='') as f:
                write = writer(f)
                write.writerow(['Right', 'Wrong'])
                write.writerows(self.data)
        except:
            print('something went wrong with clearing Data')

    def deff(self):
        try:
            from PyDictionary import PyDictionary
            from pyttsx3 import speak as say
            dictionary = PyDictionary()
            d = dictionary.meaning(self.T)
            print(d)
            say(d)
            say(self.T)
        except:
            print('no definition available')
            say('sorry, no definition available')


print('''
Welcome to my EN.Tutor program for teaching the most used words in the English language.
The program is designed to be simple, easy to use and to prevent any distractions''')
print('''
 ██████████                         mohamed7ossam@outlook.com                            
░███░░░░███                                                   
░░░    ███   ██████   █████   █████   ██████   █████████████  
      ███   ███░░███ ███░░   ███░░   ░░░░░███ ░░███░░███░░███ 
     ███   ░███ ░███░░█████ ░░█████   ███████  ░███ ░███ ░███ 
    ███    ░███ ░███ ░░░░███ ░░░░███ ███░░███  ░███ ░███ ░███ 
   ███     ░░██████  ██████  ██████ ░░████████ █████░███ █████
  ░░░       ░░░░░░  ░░░░░░  ░░░░░░   ░░░░░░░░ ░░░░░ ░░EN.Tutor''')
print('_'*20)
print('''
      [1] start exercise
      [2] start exercise on unknown words
      [3] exit
      [4] clear all Data !!
      ----Note :
      !! To exit Enter: -- except in Repeat or Definition.
      !! You have one chance to repeat a word by Entering : r
      !! to get the word definition Enter: def
      !! wrong answers will be copied automatically
      ''')
print('_'*20)

m_local = local("Back_up.csv", 1)
Right = m_local.get_list()
m_local = local("Back_up.csv", 2)
Wrong = m_local.get_list()

while True:
    user_input = input('>> ')
    if user_input == '1':
        word_list = local("words.csv", 0)
        words = word_list.get_list()
        G = 0
        break
    elif user_input == '2':
        word_list = local("Back_up.csv", 2)
        words = word_list.get_list()
        if words == []:
            print('unknown list is empty')
            word_list = local("words.csv", 0)
            words = word_list.get_list()
        G, M = 0, 1
        break
    elif user_input == '3':
        m_local = local('', '', Wrong, Right)
        m_local.save()
        print('\tyou  answered: ', total_positive, ' right answers')
        print('\tyou  answered: ', total_nigative, ' wrong answers')
        print('\tyour score is: ', score)
        print('_'*50)
        G = 1
        break
    elif user_input == '4':
        print('\tare you sure you want to clear all saved Data?')
        print('\tEnter [y/n]')
        inp = input('>> ')
        if inp == 'y' or inp == 'Y':
            m_local = local()
            Right = m_local.clear()
            Wrong = m_local.clear()
            m_local = local('', '', Wrong, Right)
            m_local.save()
            G = 1
            break
    else:
        print('please Enter a valid value')

if G == 0:
    while True:
        if Wrong == [] and M == 1:
            print('list is empty')
            m_local = local('', '', Wrong, Right)
            m_local.save()
            print('\tyou  answered: ', total_positive, ' right answers')
            print('\tyou  answered: ', total_nigative, ' wrong answers')
            print('\tyour score is: ', score)
            print('_'*50)
            break
        else:
            c = choice(words)
            if c not in Right:
                print('\n\t\tyour score is: ', score)
                say(c)
                x = input('\t\tinput: ')
                if x == '-clear':
                    print('\tare you sure you want to clear all saved Data?')
                    print('\tEnter [y/n]')
                    inp = input('>> ')
                    if inp == 'y' or inp == 'Y':
                        m_local = local()
                        Right = m_local.clear()
                        Wrong = m_local.clear()
                        m_local = local('', '', Wrong, Right)
                        m_local.save()
                        break
                elif x == '--':
                    print("\t\tthe correct answer is:   ", c)
                    m_local = local('', '', Wrong, Right)
                    m_local.save()
                    print('\tyou  answered: ', total_positive, ' right answers')
                    print('\tyou  answered: ', total_nigative, ' wrong answers')
                    print('\tyour score is: ', score)
                    print('_'*50)
                    break
                elif x == c:
                    print('\n\t\tcorrect')
                    say('correct')
                    if c in Wrong:
                        Wrong.remove(c)
                    if c not in Right:
                        Right.append(c)
                    total_positive += 1
                    score += 1
                elif x == 'r':
                    say(c)
                    x = input('\t\tinput: ')
                    if x == c:
                        print('\n\t\tcorrect')
                        say('correct')
                        if c in Wrong:
                            Wrong.remove(c)
                        if c not in Right:
                            Right.append(c)
                        total_positive += 1
                        score += 1
                    else:
                        print("\t\tfail---\n")
                        print("\t\tyour wrong input is:     ", x)
                        print("\t\tthe correct answer is:   ", c)
                        say('incorrect')
                        copy(c)
                        if c not in Wrong:
                            Wrong.append(c)
                        score -= 1
                        total_nigative += 1
                elif x == 'def':
                    say(c)
                    m_local = local('', '', '', '', c)
                    m_local.deff()
                    x = input('\t\tinput: ')
                    if x == c:
                        print('\n\t\tcorrect')
                        say('correct')
                        if c in Wrong:
                            Wrong.remove(c)
                        if c not in Right:
                            Right.append(c)
                        total_positive += 1
                        score += 1
                    else:
                        print("\t\tfail---\n")
                        print("\t\tyour wrong input is:     ", x)
                        print("\t\tthe correct answer is:   ", c)
                        say('incorrect')
                        copy(c)
                        if c not in Wrong:
                            Wrong.append(c)
                        score -= 1
                        total_nigative += 1
                else:
                    print("\t\tfail---\n")
                    print("\t\tyour wrong input is:     ", x)
                    print("\t\tthe correct answer is:   ", c)
                    say('incorrect')
                    copy(c)
                    if c not in Wrong:
                        Wrong.append(c)
                    score -= 1
                    total_nigative += 1
m = input('Press Enter to exit >> ')