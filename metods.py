# сохранением, чтением добавлением, редактированием и удалением заметок
from datetime import datetime

from os.path import join,abspath,dirname, exists

def create_note(full_name: str):
    user = list()
    with open(full_name, mode = "a+", encoding = "utf-8") as file:
        lines = file.readlines()
        keynum = lines.count+1
        user.append(str(keynum))
        user.append(input("Введите заголовок:   "))
        user.append(input("Введите саму заметку (тело):    "))
        user.append(str(datetime.now()))
        user.append(str(datetime.today()))
        with open(full_name, mode = "a", encoding = "utf-8") as file:
            # for idc, user in phone_dir.items():
            file.write(f"{user[0]}; {user[1]}; {user[2]};{user[3]};{user[4]}\n")
 
def read_note(keynum: int, full_name: str):
    if not exists(full_name):
        print("Ошибка программы! Нужно сначала создать запись перед тем как что-то прочитать")
        return
    file1 = open(full_name, "r")
    while True:
    # считываем строку
        line = file1.readline(keynum)
    # прерываем цикл, если строка пустая
        if not line:
            break
    print(line.strip())
    file1.close
    return line

def update_note (keynum: int, full_name: str):
    line =read_note(keynum, full_name)
    lst = line.strip().split(';')
    lst[1] = lst.append(input("Введите новый заголовок:   "))
    lst[2] = lst.append(input("Введите новую запись:   "))
    lst[3] = lst.append(str(datetime.now))

def delete_note (keynum: int, full_name: str):
    with open(full_name,'w') as old:
        lines = old.readlines()
        if (lines.count<=keynum): 
            print("Такой позиции в списке нет. Извините и попробуйте еще раз")
        lines.pop(keynum)
        old.writelines(lines)

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


