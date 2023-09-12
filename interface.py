from os.path import join,abspath,dirname, exists
from metods import create_note, read_note, update_note, delete_note, print_all

def menu_notes(full_name: str):
        print('Меню справочника: 1- Add note, 2 - Read, 3 - Update, 4 - Delete 5 - Print All')
        while True:    
                try: num = int(input("Введите желаемую операцию:   "))
                except: print('Неверный ввод номера действия. Возможно повезёт в следующий раз')
                if num!=1 and num!=2 and num!=3 and num!=4 and num!=5 and num!=6 and num!=7:
                        break
                if num==1:
                        create_note(full_name)
                if num==2:
                        try: number_pos = int(input("Введите позицию:   ")) #будет время трайкеч сделать
                        except: print('Ошибка! Неверный формат ввода номера позиции')
                        read_note(number_pos, full_name)
                if num==3:
                        try: number_pos = int(input("Введите позицию:   ")) #будет время трайкеч сделать
                        except: print('Ошибка! Неверный формат ввода номера позиции')
                        update_note(number_pos, full_name)
                if num==4:
                        try: number_pos = int(input("Введите позицию:   ")) #будет время трайкеч сделать
                        except: print('Ошибка! Неверный формат ввода номера позиции')
                        delete_note(number_pos, full_name)
                        # key_count-1
                if num==5:
                        print_all(full_name)
