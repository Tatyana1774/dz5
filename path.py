'''Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.'''
tx = r'C:\Users\tata1\OneDrive\Рабочий стол\statiya.txt'

def split_path(tx: str) -> tuple():
    list_n = tx.split('\\')
    list_lst = list_n[-1].split('.')
    path = '\\'.join(list_n[0:-1])
    name = list_lst[0]
    expansion = list_lst[1]
    return path, name, expansion

print(split_path(tx))