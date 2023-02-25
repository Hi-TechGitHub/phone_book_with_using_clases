import main
from main import *
b = FunctionForPhoneBook('a')
class Control:


        open_file = input("Открыть файл?: да, нет: ")
        if open_file == "да":
            b.open_phone_book()
       # book.main.open_phone_book()
        show_phone_book = input("Хотите увидеть тел. книгу?: да, нет: ")
        if show_phone_book == "да":
            b.show_phone_book()
        accept_add_contact = input("Добавить контакт?: да, нет: ")
        if accept_add_contact == "да":
            b.add_phone_book()
            b.save_phone_book()
        accept_edit_contact = input("Открыть хотите изменить контакт?: да, нет: ")
        if accept_edit_contact == "да":
            b.change_phone_book()
            b.save_phone_book()
        accept_search_contact = input("Хотите найти контакт?: да, нет: ")
        if accept_search_contact == "да":
            b.search_phone_book()
        accept_delete_contact = input("Хотите удалить контакт?: да, нет: ")
        if accept_delete_contact == "да":
            b.delete_phone_book()

