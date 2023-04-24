Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def create_note(number):
    title = check_len_text_input(
        input('Название заметки: '), number)
    body = check_len_text_input(
        input('Описание заметки: '), number)
    return Note.Note(title=title, body=body)
def menu():
    
SyntaxError: invalid syntax
def menu():
    print("\n Данная програима имеет следующие функции:\n\n1 - Все заметки из файла\n2 - добавление заметки\n3 - удаление заметки\n4 - редактировать заметку\n5 - Выбрать заметку по дате\n6 - Введите ID заметки\n7 - выход\n\nНомер функции: ")
    def check_len_text_input(text, n):
        hile len(text) <= n:
            
SyntaxError: invalid syntax
def check_len_text_input(text, n):
    while len(text) <= n:
         print(f'Текст должен быть больше {n} символов\n')
         text = input('Текст: ')
         else:
             
SyntaxError: invalid syntax
else:
    
SyntaxError: invalid syntax
else:
    
SyntaxError: invalid syntax
>>> def check_len_text_input(text, n):
...     while len(text) <= n:
...         print(f'Текст должен быть больше {n} символов\n')
...         text = input('Текст: ')
...         else:
...             
SyntaxError: invalid syntax
>>> text = input('Введите тескт: ')
Введите тескт: 
>>> else:
...     
SyntaxError: invalid syntax
>>> def check_len_text_input(text, n):
...     while len(text) <= n:
...         print(f'Текст должен быть больше {n} символов\n')
...         text = input('Введите текст: ')
...         else:
...             
SyntaxError: invalid syntax
>>>     else:
...         
SyntaxError: unexpected indent
>>> def check_len_text_input(text, n):
...     while len(text) <= n:
...          print(f'Текст должен быть больше {n} символов\n')
...          text = input('Введите текст: ')
...     else:
...         return text
