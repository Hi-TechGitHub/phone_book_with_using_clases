# class Calk:
#
#     def __init__(self, a: int = 5, b: int = 5):
#         self.a = a
#         self.b = b
#     def summ(self):
#         return self.a + self.b
#     def multi(self):
#         return self.a * self.b
#     def divition(self):
#         return self.a / self.b
#
# first = int(input("Enter 1 num: "))
# second = int(input("Enter 2 num: "))
#
#
# calk = Calk(first, second)
# print(calk.summ())
# print(calk.multi())
# print(calk.divition())


phone_book = ["Владимир", "Максим", "Евгений"]
class FunctionForPhoneBook:
    def __init__(self, a):
        self.a = a
    def open_phone_book(self):
        with open('phone_book.txt', 'r', encoding='utf-8') as data:
            p_b = data.readlines()
            self.data = data.readlines
            print('Файл открыт')
            return phone_book


    def save_phone_book(self):
        with open('phone_book.txt', 'w', encoding='utf-8') as data:
            for i in phone_book:
                data.write(i + '\n')


    def show_phone_book(self):
        print(phone_book)
        if len(phone_book) == 0:
            print('Вы не открыли файл либо файл пуст')
        else:
            for i in phone_book:
                print(' '.join(i.split(';')))


    def add_phone_book(self):
        if len(phone_book) == 0:
            print('Вы не открыли файл либо файл пуст')
        else:
            user_info = input('Введите данные нового контакта: ')
            user_info = ';'.join(user_info.split(' '))
            phone_book.append('\n' + user_info)


    def change_phone_book(self):
        user_info = input('Введите номер контакта, которого вы хотите изменить: ')
        for i in range(len(phone_book)):
            if user_info in phone_book[i]:
                print(phone_book[i])
                print(i)
                new_user_info = input('Введите новый номер контакта: ')
                phone_book[i] = phone_book[i].replace(user_info, new_user_info)


    def search_phone_book(self):
        user_info = input('Введите номер контакта, по которому будем искать: ')
        for i in range(len(phone_book)):
            if user_info in phone_book[i]:
                print(phone_book[i])


    def delete_phone_book(self):
        user_info = input('Введите номер контакта, которого вы хотите удалить: ')
        for i in range(len(phone_book)):
            if user_info in phone_book[i]:
                print(phone_book[i])
                phone_book.pop(i)
                break

