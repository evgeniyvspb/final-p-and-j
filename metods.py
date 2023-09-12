# сохранением, чтением добавлением, редактированием и удалением заметок
from datetime import datetime

from os.path import join,abspath,dirname, exists

def create_note(full_name: str):
    user = list()
    with open(full_name, mode = "r+", encoding = "utf-8") as file:
        lines = file.readlines()
        if len(lines)>0:
            keynum = int(lines[len(lines)-1][0])+1  # берем последнюю строчку и смотрим первый элемент
        else: keynum = 1  # берем последнюю строчку и смотрим первый элемент
        user.append(str(keynum))
        user.append(input("Введите заголовок:   "))
        user.append(input("Введите саму заметку (тело):    "))
        user.append(str(datetime.now()))
        with open(full_name, mode = "a", encoding = "utf-8") as file:
            file.write(f"{user[0]}; {user[1]}; {user[2]};{user[3]}\n")
 
def read_note(keynum: int, full_name: str):
    if not exists(full_name):
        print("Ошибка программы! Нужно сначала создать запись перед тем как что-то прочитать")
        return
    with open(full_name,'r') as file:
    # считываем строку
        lines =file.readlines()
        line = lines[keynum-1]
    print(line.strip("  "))
    return line    

def update_note (keynum: int, full_name: str):
    line =read_note(keynum, full_name)
    with open(full_name, mode = "r", encoding = "utf-8") as file:
        lines = file.readlines()
    lst=[4]
    lst[0]=str(keynum)
    lst.append(input("Введите новый заголовок:   "))
    lst.append(input("Введите новую запись:   "))
    lst.append(str(datetime.now()))
    lines[keynum-1] = lst[0]+";"+ str(lst[1])+";"+ str(lst[2]) +";"+ str(lst[3])+ "\n"
    with open(full_name, mode = "w", encoding = "utf-8") as file:
            for line in lines:
                file.write(line)

def delete_note (keynum: int, full_name: str):
    with open(full_name, mode = "r", encoding = "utf-8") as file:
        lines = file.readlines()
    lines.pop(keynum-1)
    with open(full_name, mode = "w", encoding = "utf-8") as file:
            for line in lines:
                file.write(line)

def print_all(file_name: str):
    file1 = open(file_name, "r")
    while True:
    # считываем строку
        line = file1.readline()
    # прерываем цикл, если строка пустая
        if not line:
            break
    # выводим строку
        print(line.strip()+"\n")
    # закрываем файл
    file1.close     
