import sys
import os
from time import sleep
from pathlib import Path
import random
import colorama
from colorama import Fore, Style
from simple_term_menu import TerminalMenu

def brainfuck():
    options = ["English", "Русский"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    if options[menu_entry_index] == "Русский":
        print(f"Привет путник!")        
        hi()
        sleep(1)
        select()
    else:
        print(f"Sorry, English language is not available now :(")
        sleep(1)
        print(f"Select language")
        brainfuck()
    #print(f"U have selected {options[menu_entry_index]}!")
def hi():
    lines = [
        ("Выбери, чем хочешь заняться?", 0.05)
    ]
    #Потом обязательно разделить на несколько строк чтобы было красива
    delays = [0.1, 0.2, 0.1]

    for i, (line, char_delay) in enumerate(lines):
        style = Fore.WHITE + Style.BRIGHT
        end_style = Style.RESET_ALL
    
    for char in line:
        print(f"{style}{char}{end_style}", end="")
        sys.stdout.flush()
        sleep(char_delay)
    
    print()
    sleep(delays[i])
def bb():
    lines = [
        ("Спасибо за внимание! Пока))", 0.05)
    ]
    #Потом обязательно разделить на несколько строк чтобы было красива
    delays = [0.1, 0.1]

    for i, (line, char_delay) in enumerate(lines):
        style = Fore.MAGENTA + Style.BRIGHT
        end_style = Style.RESET_ALL
    
    for char in line:
        print(f"{style}{char}{end_style}", end="")
        sys.stdout.flush()
        sleep(char_delay)
    
    print()
    sleep(delays[i])
def select():
    options = ["Текстовый чат", "Случайный трек", "Инфа", "Выход"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    if options[menu_entry_index] == "Текстовый чат":
        sleep(1)
        print(f"В данный момент текстовый чат с Чатти разрабатвается")
        sleep(1)
        os.system("clear")
        select()
    elif options[menu_entry_index] == "Случайный трек":
        os.system("clear")
        sleep(1)
        print(f"О, давай подберём что нибудь!")
        sleep(1)
        print(f"...")
        sleep(1)
        randmus()
    elif options[menu_entry_index] == "Инфа":
        os.system("clear")
        sleep(1)
        info()
        sleep(1)
        select()
    else:
        os.system("clear")
        bb()
        sleep(2)
        os.system("clear")
        sleep(1)
def info():
    lines = [
        ("Сейчас ты находишься в консольном приложении", 0.05),
        ("TestChat", 0.05),
        ("Это простенькая игрушка для терминала, с парой полезных функций", 0.05),
        ("Например, утилита сможет порекомендовать тебе музыку", 0.05),
        ("или видео с Ютуба", 0.05),
        ("А так же впринципе может развлечь тебя", 0.05),
        ("Возможно это поднимет тебе настроение :)", 0.05),
    ]

    delays = [0.1, 0.1, 0.1, 0.1, 0.2, 0.1, 0]

    for i, (line, char_delay) in enumerate(lines):
        style = Fore.RED + Style.BRIGHT
        end_style = Style.RESET_ALL
        
        if line == "TestChat":
            style = Fore.YELLOW + Style.BRIGHT
        if line == "Это простенькая игрушка для терминала, с парой полезных функций":
            style = Fore.LIGHTYELLOW_EX + Style.BRIGHT
        if line == "Например, утилита сможет порекомендовать тебе музыку":
            style = Fore.LIGHTMAGENTA_EX + Style.BRIGHT
        if line == "Возможно это поднимет тебе настроение :)":
            style = Fore.GREEN + Style.DIM

        for char in line:
            print(f"{style}{char}{end_style}", end="")
            sys.stdout.flush()
            sleep(char_delay)
        
        print()
        sleep(delays[i])
def randmus():
    muid = random.randint(1,10)
    if muid == 1:
        print(f"хмм.. попробуй этот трек! https://music.youtube.com/watch?v=ktoo5jluVDA&si=BD67yJy9433xVCxX ")
    elif muid == 2:
        print(f"хмм.. попробуй этот трек! https://music.youtube.com/watch?v=DjSVtTau38s&si=popJ8HVKdiTXAt-w")
    elif muid == 3:
        print(f"хмм.. попробуй этот трек! https://music.youtube.com/watch?v=slmm-RTsMLs")
    elif muid == 4:
        print(f"хмм.. попробуй этот трек! https://music.youtube.com/watch?v=kYrRPsRLLtM ")
    elif muid == 5:
        print(f"хмм.. попробуй этот трек! https://music.youtube.com/watch?v=YX4E9qT2B0I ")
    elif muid == 6:
        print(f"хмм.. попробуй этот трек! https://music.youtube.com/watch?v=V8BBDl-Cg_0")
    elif muid == 7:
        print(f"хмм.. попробуй этот трек! https://music.youtube.com/watch?v=wPOF5FgG3DU")
    elif muid == 8:
        print(f"хмм.. попробуй этот трек! https://music.youtube.com/watch?v=QhTMOV31mpU")
    elif muid == 9:
        print(f"хмм.. попробуй этот трек! https://music.youtube.com/watch?v=u5Ekc9hQ_s4")
    else:
        print(f"хмм.. попробуй этот трек! Он особенный) https://music.youtube.com/watch?v=c0TYGMKfHHk ")
    sleep(1)
    print(f"Если хочешь, могу включить ещё один трек)")
    print(f"Включить?")
    options = ["Да", "Чёто не хочу пока"]
    terminal_menu = TerminalMenu(options) 
    menu_entry_index = terminal_menu.show()
    if options[menu_entry_index] == "Да":
        lmuid = random.randint(1,5)
        if lmuid == 1:
            os.system("mpv ~/testchat/1.mp3 | ls &")
        elif lmuid == 2:
            os.system("mpv ~/testchat/2.mp3 | ls &")
        elif lmuid == 3:
            os.system("mpv ~/testchat/3.mp3 | ls &")
        elif lmuid == 4:
            os.system("mpv ~/testchat/4.mp3 | ls &")
        else:
            os.system("mpv ~/testchat/5.mp3 | ls &")
        sleep(0.5)
        os.system("cava")
    else:
        os.system("clear")
        select()

print(f"Select language")
brainfuck()