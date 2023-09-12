from os.path import join,abspath,dirname, exists
from metods import create_note, read_note, update_note, delete_note, print_all

def menu_notes(full_name: str):
        print('Меню справочника: 1- Add note, 2 - Read, 3 - Update, 4 - Delete 5 - Print All')
        # full_name = "notes.csv"
        # notes_dir = dict()
        # key_count =1
        while True:    
                num = int(input("Введите желаемую операцию:   "))
                if num!=1 and num!=2 and num!=3 and num!=4 and num!=5 and num!=6 and num!=7:
                        break
                if num==1:
                        create_note(full_name)
                if num==2:
                        number_pos = int(input("Введите позицию:   ")) #будет время трайкеч сделать
                        read_note(number_pos, full_name)
                if num==3:
                        number_pos = int(input("Введите позицию:   ")) #будет время трайкеч сделать
                        update_note(number_pos, full_name)
                if num==4:
                        number_pos = int(input("Введите позицию:   ")) #будет время трайкеч сделать
                        delete_note(number_pos, full_name)
                        # key_count-1
                if num==5:
                        print_all(full_name)
