# XO
# Alt+3 Studio
# Илья Катков

# импорт библиотек
from tkinter import *
from tkinter import messagebox as mb
import psutil
import sys
import os
import webbrowser

i, i_r, i_i = 0, 0, 0 # счетчики для запущенных окон

# проверка на кол-во запущенных программ
# нельзя запустить больше одного приложения
for proc in psutil.process_iter():
    name = proc.name()
    if name == "xo.exe":
        i += 1
        if i > 2:
            sys.exit()

# выход из игры
def close_game():
    ans = mb.askyesno('Крестики-нолики!', 'Выйти из игры?')  # спрашиваем пользователя, собирается ли он выйти из игры
    if ans == 1:
        root.destroy()  # уничтожаем главное окно, т.е. выходим из приложения

# открыть страницу Alt+3 Studio в vk.com CLICK
def vk_alt3s(event):
    webbrowser.open_new(r"http://vk.com/alt3s")

# выход из игры ESC
def close_game_esc(event):
    close_game()

# окно правил игры F1
def rules_f1(event):

    # нельзя открыть больше одного окна правил игры
    global i_r
    i_r += 1
    if i_r > 1:
        return print("---Правила игры уже открыты!---\n")

    # выход из окна правил
    def rules_close():
        global i_r
        i_r = 0
        rules.destroy()

    # выход из окна правил ENTER
    def rules_close_enter(event):
        global i_r
        i_r = 0
        rules.destroy()

    # readme.txt
    def readme():
        try:
            os.startfile(r'readme.txt')
        except FileNotFoundError:
            return print("---Файл readme.txt не найден!---\n")
    
    # настройка окна правил
    rules = Toplevel(root, bg="white")
    rules.geometry("280x250")
    rules.resizable(0, 0)
    rules.title("Правила игры")
    rules.iconbitmap('icon.ico')
    rules.focus_set()  # ставим фокус на открытое окно
    rules.bind("<Return>", rules_close_enter)  # бинд ENTER'a на выход из окна
    rules.protocol("WM_DELETE_WINDOW", rules_close)  # обработка выхода из окна

    # установка объектов
    lt = Label(rules,
               text="XO",
               font="Calibri 36",
               bg="white",
               fg="red")  # надпись "XO"
    lt.place(x=110, y=-10)

    lt2 = Label(rules,
               text="крестики-нолики",
               font="Calibri 10",
               bg="white",
               fg="black")  # надпись "крестики-нолики"
    lt2.place(x=90, y=40)

    lrules = Label(rules,
                   text="Правила игры:\n",
                   font="Calibri 14",
                   bg="white",
                   justify=LEFT)  # надпись "Правила игры:"
    lrules.place(x=3, y=60)

    lr = Label(rules,
               text="    Игроки по очереди ставят на свободные клетки \nполя 3х3 знаки (один всегда крестики, другой всег-\nда нолики).\n    Первый, выстроивший в ряд 3 своих фигуры по \nвертикали, горизонтали или диагонали, выигрыва-\nет.\n    Первый ход делает игрок, ставящий крестики.",
               font="Calibri 9",
               bg="white",
               justify=LEFT)  # правила игры
    lr.place(x=3, y=90)

    ok_btn = Button(rules,
                    text="OK",
                    width=10,
                    font="Calibri 11",
                    fg="black", 
                    command=rules_close)  # кнопка ОК
    ok_btn.place(x=20, y=205)

    rm_btn = Button(rules,
                    text="Открыть ReadMe",
                    width=14,
                    font="Calibri 11",
                    fg="black", 
                    command=readme)  # кнопка Readme
    rm_btn.place(x=135, y=205)

# окно информации об игре F2
def info_window_f2(event):
    # нельзя открыть больше одного окна информации о игре
    global i_i
    i_i += 1
    if i_i > 1:
        return print("---Информация об игре уже открыта!---\n")

    # выход из окна правил
    def info_window_close():
        global i_i
        i_i = 0
        info_window.destroy()

    # выход из окна правил ENTER
    def info_window_close_enter(event):
        global i_i
        i_i = 0
        info_window.destroy()
    
    # открыть мою страницу в vk.com CLICK
    def vk(event):
        webbrowser.open_new(r"http://vk.com/ilkatkov")

    # открыть страницу Alt+3 Studio в vk.com CLICK
    def vk_alt3s(event):
        webbrowser.open_new(r"http://vk.com/alt3s")

    # настройка окна правил
    info_window = Toplevel(root, bg="white")
    info_window.geometry("160x190")
    info_window.resizable(0, 0)
    info_window.title("Об игре")
    info_window.iconbitmap('icon.ico')
    info_window.focus_set()  # ставим фокус на открытое окно
    info_window.bind("<Return>", info_window_close_enter)  # бинд ENTER'a на выход из окна
    info_window.protocol("WM_DELETE_WINDOW", info_window_close)  # обработка выхода из окна

    # установка объектов
    lt = Label(info_window,
               text="XO",
               font="Calibri 50",
               bg="white",
               fg="red")  # надпись "XO"
    lt.place(x=40, y=-15)

    lt2 = Label(info_window,
               text="крестики-нолики",
               font="Calibri 12",
               bg="white",
               fg="black")  # надпись "крестики-нолики"
    lt2.place(x=22, y=53)

    li = Label(info_window,
               text="Автор:",
               font="Calibri 10",
               bg="white", 
               justify=CENTER)  # автор
    li.place(x=27, y=85)

    il = Label(info_window,
               text="Илья Катков",
               font="Calibri 10",
               bg="white",
               fg="blue",
               justify=CENTER)  # ilkatkov
    il.place(x=67, y=85)
    il.bind("<Button-1>", vk)

    il = Label(info_window,
               text="Alt+3 Studio",
               font="Calibri 10",
               bg="white",
               fg="blue",
               justify=CENTER)  # Alt+3 Studio
    il.place(x=50, y=105)
    il.bind("<Button-1>", vk_alt3s)

    ok_btn = Button(info_window,
                    text="OK",
                    width=10,
                    font="Calibri 11",
                    fg="black",
                    command=info_window_close)  # кнопка ОК
    ok_btn.place(x=37, y=135)

def run_game(): # начало игры
    change_symbol()

def change_symbol(): # смена хода
    global symbol
    if symbol == "X":
        lbl_step['text'] = "Ход: Нолики"
        symbol = "O"
    else:
        lbl_step['text'] = "Ход: Крестики"
        symbol = "X"

def click_pass(): # кнопки больше не работают
    pass

def refresh(): # перезапускаем игру
    global symbol, winner, count
    for i in range(1,3+1):
        for j in range(1,3+1):
            exec(f'btn_{i}_{j}[\'text\'] = \"   \"')
            exec(f'btn_{i}_{j}[\'fg\'] = \"black\"')
            exec(f'btn_{i}_{j}[\'activeforeground\'] = \"black\"')
            exec(f'btn_{i}_{j}[\'command\'] = click_btn_{i}_{j}')
    count = 0
    winner = "" 
    lbl_step['text'] = "Ход: Крестики"
    symbol = "X"       

def check_win(): # проверка на выигрыш
    win = ["XXX","OOO"]
    if (btn_1_1["text"] + btn_1_2["text"] + btn_1_3["text"]) in win:
        btn_1_1['fg'] = 'red'
        btn_1_2['fg'] = 'red'
        btn_1_3['fg'] = 'red'
        btn_1_1['activeforeground'] = 'red'
        btn_1_2['activeforeground'] = 'red'
        btn_1_3['activeforeground'] = 'red'
        if (btn_1_1["text"] + btn_1_2["text"] + btn_1_3["text"]) == "XXX":
            winner = "Крестики"
        else:
            winner = "Нолики"
        mb.showinfo("Крестики-нолики", f"{winner} победили!")
        refresh()
    elif (btn_1_1["text"] + btn_2_2["text"] + btn_3_3["text"]) in win:
        btn_1_1['fg'] = 'red'
        btn_2_2['fg'] = 'red'
        btn_3_3['fg'] = 'red'
        btn_1_1['activeforeground'] = 'red'
        btn_2_2['activeforeground'] = 'red'
        btn_3_3['activeforeground'] = 'red'
        if (btn_1_1["text"] + btn_2_2["text"] + btn_3_3["text"]) == "XXX":
            winner = "Крестики"
        else:
            winner = "Нолики"
        mb.showinfo("Крестики-нолики", f"{winner} победили!")
        refresh()
    elif (btn_1_1["text"] + btn_2_1["text"] + btn_3_1["text"]) in win:
        btn_1_1['fg'] = 'red'
        btn_2_1['fg'] = 'red'
        btn_3_1['fg'] = 'red'
        btn_1_1['activeforeground'] = 'red'
        btn_2_1['activeforeground'] = 'red'
        btn_3_1['activeforeground'] = 'red'
        if (btn_1_1["text"] + btn_2_1["text"] + btn_3_1["text"]) == "XXX":
            winner = "Крестики"
        else:
            winner = "Нолики"
        mb.showinfo("Крестики-нолики", f"{winner} победили!")
        refresh()      
    elif (btn_1_3["text"] + btn_2_2["text"] + btn_3_1["text"]) in win:
        btn_1_3['fg'] = 'red'
        btn_2_2['fg'] = 'red'
        btn_3_1['fg'] = 'red'
        btn_1_3['activeforeground'] = 'red'
        btn_2_2['activeforeground'] = 'red'
        btn_3_1['activeforeground'] = 'red'
        if (btn_1_3["text"] + btn_2_2["text"] + btn_3_1["text"]) == "XXX":
            winner = "Крестики"
        else:
            winner = "Нолики"
        mb.showinfo("Крестики-нолики", f"{winner} победили!")
        refresh()
    elif (btn_1_3["text"] + btn_2_3["text"] + btn_3_3["text"]) in win:
        btn_1_3['fg'] = 'red'
        btn_2_3['fg'] = 'red'
        btn_3_3['fg'] = 'red'
        btn_1_3['activeforeground'] = 'red'
        btn_2_3['activeforeground'] = 'red'
        btn_3_3['activeforeground'] = 'red'
        if (btn_1_3["text"] + btn_2_3["text"] + btn_3_3["text"]) == "XXX":
            winner = "Крестики"
        else:
            winner = "Нолики"
        mb.showinfo("Крестики-нолики", f"{winner} победили!")
        refresh()
    elif (btn_3_1["text"] + btn_3_2["text"] + btn_3_3["text"]) in win:
        btn_3_1['fg'] = 'red'
        btn_3_2['fg'] = 'red'
        btn_3_3['fg'] = 'red'
        btn_3_1['activeforeground'] = 'red'
        btn_3_2['activeforeground'] = 'red'
        btn_3_3['activeforeground'] = 'red'
        if (btn_3_1["text"] + btn_3_2["text"] + btn_3_3["text"]) == "XXX":
            winner = "Крестики"
        else:
            winner = "Нолики"
        mb.showinfo("Крестики-нолики", f"{winner} победили!")
        refresh()
    elif (btn_1_2["text"] + btn_2_2["text"] + btn_3_2["text"]) in win:
        btn_1_2['fg'] = 'red'
        btn_2_2['fg'] = 'red'
        btn_3_2['fg'] = 'red'
        btn_1_2['activeforeground'] = 'red'
        btn_2_2['activeforeground'] = 'red'
        btn_3_2['activeforeground'] = 'red'
        if (btn_1_2["text"] + btn_2_2["text"] + btn_3_2["text"]) == "XXX":
            winner = "Крестики"
        else:
            winner = "Нолики"
        mb.showinfo("Крестики-нолики", f"{winner} победили!")
        refresh()
    elif (btn_2_1["text"] + btn_2_2["text"] + btn_2_3["text"]) in win:
        btn_2_1['fg'] = 'red'
        btn_2_2['fg'] = 'red'
        btn_2_3['fg'] = 'red'
        btn_2_1['activeforeground'] = 'red'
        btn_2_2['activeforeground'] = 'red'
        btn_2_3['activeforeground'] = 'red'
        if (btn_2_1["text"] + btn_2_2["text"] + btn_2_3["text"]) == "XXX":
            winner = "Крестики"
        else:
            winner = "Нолики"
        mb.showinfo("Крестики-нолики", f"{winner} победили!")
        refresh()
    elif count == 9:
        mb.showinfo("Крестики-нолики", "Ничья!")
        refresh()

def click_btn_1_1():
    global symbol, count
    btn_1_1["text"] = symbol
    btn_1_1['command'] = click_pass
    count += 1
    change_symbol()
    check_win()

def click_btn_1_2():
    global symbol, count
    btn_1_2["text"] = symbol
    btn_1_2['command'] = click_pass
    count += 1
    change_symbol()
    check_win()

def click_btn_1_3():
    global symbol, count
    btn_1_3["text"] = symbol
    btn_1_3['command'] = click_pass
    count += 1
    change_symbol()
    check_win()

def click_btn_2_1():
    global symbol, count
    btn_2_1["text"] = symbol
    btn_2_1['command'] = click_pass
    count += 1
    change_symbol()
    check_win()

def click_btn_2_2():
    global symbol, count
    btn_2_2["text"] = symbol
    btn_2_2['command'] = click_pass
    count += 1
    change_symbol()
    check_win()

def click_btn_2_3():
    global symbol, count
    btn_2_3["text"] = symbol
    btn_2_3['command'] = click_pass
    count += 1
    change_symbol()
    check_win()

def click_btn_3_1():
    global symbol, count
    btn_3_1["text"] = symbol
    btn_3_1['command'] = click_pass
    count += 1
    change_symbol()
    check_win()

def click_btn_3_2():
    global symbol, count
    btn_3_2["text"] = symbol
    btn_3_2['command'] = click_pass
    count += 1
    change_symbol()
    check_win()

def click_btn_3_3():
    global symbol, count
    btn_3_3["text"] = symbol
    btn_3_3['command'] = click_pass
    count += 1
    change_symbol()
    check_win()

# настройка окна игры
root = Tk()
root.title("Крестики-нолики!")
root.iconbitmap('icon.ico')
root.geometry("400x300")
root.resizable(0,0)
root.bind("<F1>", rules_f1)  # окно правил игры F1
root.bind("<F2>", info_window_f2)  # окно информации об игре F2
root.bind("<Escape>", close_game_esc)  # выход из игры ESC
root.protocol("WM_DELETE_WINDOW", close_game)  # обработка выхода из приложения

# установка фона
bg_main = PhotoImage(file="images/bg.png")
bg_main_image = Label(root, image=bg_main)
bg_main_image.place(x=-2, y=-2)

# глобальные переменные
symbol = "" # О или Х
winner = "" # победитель
count = 0 # кол-во ходов

# XO крестики-нолики
lbl_xo = Label(text = "XO", font = "Calibri 50", fg = "red", bg = "white")
lbl_xo.place(x = 47, y = -8)
lbl_kn = Label(text = "крестики-нолики", font = "Calibri 12", bg = "white")
lbl_kn.place(x = 28, y = 60)
lbl_step = Label(text = "Ход: ", font = "Calibri 15", bg = "white")
lbl_step.place(x = 222, y = 32)

# Alt+3 Studio, 2019
lbl_alt3s = Label(text = "Alt+3 Studio", font = "Calibri 12", bg = "white")
lbl_alt3s.place(x = 260, y = 269)
lbl_alt3s.bind("<Button-1>", vk_alt3s)

# создание игрового поля
y = 100 # y верхнего левого угла поля
for i in range(1,3+1):
    x = 10 # x верхнего левого угла поля
    for j in range(1,3+1):
        exec(f'btn_{i}_{j} = Button(text = "      ", width = 3, bg = "white smoke", font = "Calibri 20",command = click_btn_{i}_{j})')
        exec(f'btn_{i}_{j}.place(x = {x},y = {y})')
        x += 52
    y+= 57

# начало игры
run_game()

root.mainloop()